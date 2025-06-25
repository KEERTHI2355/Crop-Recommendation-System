# Crop-Recommendation-System

The Crop Recommendation System is an advanced machine learning-based model designed to assist farmers in making informed decisions regarding crop selection. With the increasing unpredictability of climate conditions, selecting the optimal crop for a given season and region has become a significant challenge for farmers. This system addresses this challenge by leveraging historical weather data, soil characteristics, and crop yield information to predict the most suitable crops for a specific location. By integrating various machine learning algorithms such as regression, classification, and ensemble methods, the model analyzes complex interactions between environmental factors and crop performance. The system is deployed as a user-friendly web and mobile application, allowing farmers to input local data and receive precise crop recommendations. The ultimate goal is to enhance agricultural productivity and sustainability by providing actionable insights based on robust data analysis.

## Overview
This is a web-based crop recommendation system built using Flask, a Python web framework. The system takes in user input for nitrogen, phosphorus, potassium, pH, and district, and recommends a suitable crop based on these parameters.

## Objectives

The primary objective of the Crop Recommendation System is to support farmers in making data-driven decisions about crop selection to maximize yield and resource utilization. Specific objectives include:
1.	Accurate Crop Prediction: Utilize historical weather, soil, and crop yield data to accurately predict the most suitable crops for upcoming seasons.
2.	User-Friendly Interface: Develop a web and mobile application that is easy to use, enabling farmers to input local data and receive crop recommendations with minimal effort.
3.	Enhanced Agricultural Productivity: Increase crop yields and optimize resource use by providing farmers with precise, actionable insights tailored to their specific environmental conditions.
4.	Integration of Advanced Machine Learning Techniques: Apply a range of machine learning algorithms, including Random Forest, Gradient Boosting, and Neural Networks, to analyse complex interactions and improve prediction accuracy.
5.	Scalability and Adaptability: Ensure the system can be scaled and adapted to different geographical regions, integrating real-time data from IoT sensors for continuous improvement of prediction accuracy.
6.	Sustainable Farming Practices: Promote sustainable farming by guiding farmers towards crop choices that are best suited to their environmental conditions, thereby reducing waste and improving ecological balance.
By achieving these objectives, the Crop Recommendation System aims to provide a valuable tool for farmers, helping them navigate the uncertainties of climate variability and make more informed agricultural decisions.

## Files and Folders
`app.py`
This is the main application file that defines the Flask app and its routes. It handles HTTP requests and responses, and interacts with the crop_recomendation_model module to recommend crops.

`crop_recomendation_model.py`
This module contains the logic for recommending crops based on the input parameters. It takes in nitrogen, phosphorus, potassium, pH, and district as inputs and returns the recommended crop, temperature, humidity, and rainfall.

`templates`
This folder contains the HTML templates for the application.

`index.html`
This is the main landing page of the application, where users can input their parameters.

`result.html`
This template displays the recommended crop and its corresponding temperature, humidity, and rainfall.

`static`
This folder contains static assets such as images.

`crop_images`
This folder contains images of different crops, which are displayed on the result page.

## File Structure
```
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
requirements.txt
README.md
```
## How to Run
- Install the required dependencies by running pip install -r requirements.txt.
- Run the application by executing python app.py.
- Open a web browser and navigate to http://localhost:5000 to access the application.

## How to Use
- Enter the nitrogen, phosphorus, potassium, pH, and district values in the input fields on the index page.
- Click the "Recommend Crop" button to submit the form.
- The application will display the recommended crop, temperature, humidity, and rainfall on the result page.

## Prerequisites
- Python 3.8 or higher
- Flask 2.0 or higher
- A web browser (e.g. Google Chrome, Mozilla Firefox)

## Installation
- Install Python from the official Python website if you haven't already.
- Install Flask by running pip install flask in your `terminal/command prompt`.
- Clone this repository by running
   ```
  git clone https://github.com/KEERTHI2355/Crop-Recommendation-System
  ```
- Navigate to the project directory by running
  ```
  cd crop-recommendation-system
  ```
- Install the required dependencies by running
  ```
  pip install -r requirements.txt
  ```

## How to Contribute
Feel free to submit issues and enhancement requests or fork the repository and submit pull requests. Contributions are welcome!

1. Fork it (https://github.com/KEERTHI2355/Crop-Recommendation-System/fork)
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add some new feature`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Note
- This application assumes that the crop_recomendation_model module is implemented and functional. You may need to modify the app.py file to accommodate any changes to the model's API.
- Crate an account in open-meteo by visiting https://open-meteo.com
- You will get an API key, copy that API key and past the API key in the OPEN_METEO.py file in the place of "XXXXXXXXXXXXXX."
