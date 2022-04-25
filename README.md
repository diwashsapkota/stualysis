## Deploying ML Model using Flask
This is a simple project to elaborate how to deploy a Machine Learning model using Flask API

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

Flask version: 0.12.2
conda install flask=0.12.2  (or) pip install Flask==0.12.2

### Project Structure
This project has four major parts :
1. model.py - This contains code for the Machine Learning model to predict the final exam result of grade-12 students using the 'studentdataset.csv' file.
2. app.py - This contains Flask APIs that receives student details through GUI or API calls, computes the precited value based on the model and returns it.
3. template - This folder contains the HTML template (index.html) to allow student to interact and displays the predicted score.
4. static - This folder contains the css folder with style.css file which has the styling required for the index.html file.

### Running the project

1. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

2. Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000

You should be able to view the homepage.

Enter valid numerical values in all the input fields and hit 'Predict My Score'.

If everything goes well, you should  be able to see the predcited score value on top of the HTML page!
check the output here: http://127.0.0.1:5000/predict

