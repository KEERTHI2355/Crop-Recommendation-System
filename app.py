from flask import Flask, render_template, request
from crop_recomendation_model import recommend_crop
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    nitrogen = request.form['nitrogen']
    phosphorus = request.form['phosphorus']
    potassium = request.form['potassium']
    ph = request.form['ph']
    district = request.form['district'].lower()

    crop,temp,hum,rain=recommend_crop(int(nitrogen),int(phosphorus),int(potassium),float(ph),district)
    crop_info = {
            'temperature': temp,
            'humidity': hum,
            'rainfall': rain,
            'recommended_crop': crop,
            'image': crop+".jpg"
        }

    return render_template('result.html', crop_info=crop_info)

if __name__ == '__main__':
    app.run(debug=True)
