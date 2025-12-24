# 🌾 Crop Recommendation System  

The **Crop Recommendation System** is an advanced machine learning-based model that helps farmers choose optimal crops by leveraging historical weather data, soil characteristics, and crop yield information to predict the most suitable crops for a specific location. It addresses the growing challenge of climate unpredictability by applying algorithms such as regression, classification, and ensemble methods to analyze complex interactions between environmental factors and crop performance. Deployed as a user-friendly web and mobile application, it allows farmers to input local data and receive precise crop recommendations, with the ultimate goal of enhancing agricultural productivity and sustainability through actionable, data-driven insights.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-Queries-blue?logo=postgresql)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Model-blue?logo=scikit-learn)
![API](https://img.shields.io/badge/API-Backend-blue?logo=fastapi)
![EDA](https://img.shields.io/badge/EDA-Data%20Analysis-blue?logo=tableau)
![Web Development](https://img.shields.io/badge/Web%20Development-Frontend%2FBackend-blue?logo=google-chrome)
![Status](https://img.shields.io/badge/Project-Completed-success)


## 🧭 Overview  

This is a web-based crop recommendation system built using **Flask**, a Python web framework. The system takes in user input for **nitrogen, phosphorus, potassium, pH, and district**, and recommends a suitable crop based on these parameters.  


## 🎯 Objectives  

The primary objective of the **Crop Recommendation System** is to support farmers in making data-driven decisions about crop selection to maximize yield and resource utilization.  

Specific objectives include:  

1. **Accurate Crop Prediction**  
   Utilize historical weather, soil, and crop yield data to accurately predict the most suitable crops for upcoming seasons.  

2. **User-Friendly Interface**  
   Develop a web and mobile application that is easy to use, enabling farmers to input local data and receive crop recommendations with minimal effort.  

3. **Enhanced Agricultural Productivity**  
   Increase crop yields and optimize resource use by providing farmers with precise, actionable insights tailored to their specific environmental conditions.  

4. **Integration of Advanced Machine Learning Techniques**  
   Apply a range of machine learning algorithms, including Random Forest, Gradient Boosting, and Neural Networks, to analyse complex interactions and improve prediction accuracy.  

5. **Scalability and Adaptability**  
   Ensure the system can be scaled and adapted to different geographical regions, integrating real-time data from IoT sensors for continuous improvement of prediction accuracy.  

6. **Sustainable Farming Practices**  
   Promote sustainable farming by guiding farmers towards crop choices that are best suited to their environmental conditions, thereby reducing waste and improving ecological balance.  

By achieving these objectives, the Crop Recommendation System aims to provide a valuable tool for farmers, helping them navigate the uncertainties of climate variability and make more informed agricultural decisions.  


## 🗂️ Files and Folders  

`app.py` - This is the main application file that defines the Flask app and its routes. It handles HTTP requests and responses, and interacts with the `crop_recomendation_model` module to recommend crops.  

`crop_recomendation_model.py` - This module contains the logic for recommending crops based on the input parameters. It takes in nitrogen, phosphorus, potassium, pH, and district as inputs and returns the recommended crop, temperature, humidity, and rainfall.  

`templates` - This folder contains the HTML templates for the application.  

`index.html` - This is the main landing page of the application, where users can input their parameters.  

`result.html` - This template displays the recommended crop and its corresponding temperature, humidity, and rainfall.  

`static` - This folder contains static assets such as images.  

`crop_images` - This folder contains images of different crops, which are displayed on the result page.  


## 📁 File Structure  

```text
Crop Recommendation System/
  app.py
  crop_recomendation_model.py
  templates/
    index.html
    result.html
  static/
    crop_images/
      crop1.jpg
      crop2.jpg
      ...
      ...
      cropn.jpg
  requirements.txt
  README.md
```


## 🚀 How to Run  

- Install the required dependencies by running:  
  ```bash
  pip install -r requirements.txt
  ```
- Run the application by executing:  
  ```bash
  python app.py
  ```
- Open a web browser and navigate to `http://localhost:5000` to access the application.  


## 🌱 How to Use  

- Enter the **nitrogen, phosphorus, potassium, pH, and district** values in the input fields on the index page.  
- Click the **"Recommend Crop"** button to submit the form.  
- The application will display the **recommended crop, temperature, humidity, and rainfall** on the result page.  


## ⚙️ Prerequisites  

- Python 3.8 or higher  
- Flask 2.0 or higher  
- A web browser (e.g. Google Chrome, Mozilla Firefox)  


## 🛠 Installation  

- Install Python from the official Python website if you haven't already.  
- Install Flask by running:  
  ```bash
  pip install flask
  ```
- Clone this repository by running:  
  ```bash
  git clone https://github.com/KEERTHI2355/Crop-Recommendation-System
  ```
- Navigate to the project directory by running:  
  ```bash
  cd crop-recommendation-system
  ```
- Install the required dependencies by running:  
  ```bash
  pip install -r requirements.txt
  ```


## 🤝 How to Contribute  

Feel free to submit issues and enhancement requests or fork the repository and submit pull requests. Contributions are welcome!  

1. Fork it:  
   `https://github.com/KEERTHI2355/Crop-Recommendation-System/fork`  
2. Create your feature branch:  
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -am "Add some new feature"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/new-feature
   ```
5. Create a new Pull Request  


## 📄 License  

This project is licensed under the **MIT License** – see the `LICENSE` file for details.  


## 📝 Note  

- This application assumes that the `crop_recomendation_model` module is implemented and functional. You may need to modify the `app.py` file to accommodate any changes to the model's API.  
- Crate an account in open-meteo by visiting:  
  `https://open-meteo.com`  
- You will get an API key; copy that API key and past the API key in the `OPEN_METEO.py` file in the place of `"XXXXXXXXXXXXXX."`


## 👤 Author

**K Keerthi**  
Data Science Engineering Student  
Aspiring Python Developer / Data Analyst  


---

<p align="center">
  🛠 Built by <a href="https://github.com/KEERTHI2355">@Keerthi2355</a> 
  <br>
  <a href="#-the-vault">Back to Top</a>
</p>
