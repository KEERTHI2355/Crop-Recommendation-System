import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split 
from sklearn.feature_selection import VarianceThreshold ,f_classif ,SelectKBest
from sklearn.feature_selection import mutual_info_classif
from OPEN_METEO import get_weather


data=pd.read_csv("data/Crop_Recommendation.csv")


x=data.drop(columns="Crop",axis=1)
y=data["Crop"]
#print(np.shape(x),np.shape(y))

def recommend_crop(N,P,K,ph,city_name):
    temp,hum,rain=get_weather(city_name)

    #print("temp=",temp,"humidity=",hum,"Rain=",rain)
    
    mic=SelectKBest(score_func=mutual_info_classif,k=5)
    mic.fit(data.drop(columns="Crop").select_dtypes("number").fillna(0),data["Crop"])

    features_MI_scores=pd.Series(mic.scores_,index=data.drop(columns="Crop").select_dtypes("number").fillna(0).columns)
    features_MI_scores.sort_values(ascending=True)

    x=data.drop(columns="Crop",axis=1)
    y=data["Crop"]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,stratify=y,random_state=42)
    #print(np.shape(x_train),np.shape(x_test))
    #print(np.shape(y_train),np.shape(y_test))

    #print(features_MI_scores)

    RC1=RandomForestClassifier(random_state=42,n_jobs=-1,max_depth=5,n_estimators=100)
    RC1.fit(x_train,y_train)
    #print(f"accuracy ---->>> {RC1.score(x_test,y_test)*100:0.2f}%")

    #print(x_train)


    y_predict=RC1.predict(x_test)
    #print(np.size(y_predict))

    p=RC1.predict([[N,P,K,temp,hum,ph,rain]])
    #print("crop=",p[[0]])
    return p[0],temp,hum,rain

#recommend_crop(104,18,30,6.7,"Ballari")


