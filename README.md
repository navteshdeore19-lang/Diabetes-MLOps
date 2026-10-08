### **# 🩺 Diabetes Prediction — End-to-End MLOps Project**



An end-to-end Machine Learning and MLOps project that predicts diabetes using Logistic Regression and demonstrates model deployment, containerization, cloud deployment, CI, monitoring, data drift detection, and model retraining.



##### \## 📌 Project Overview



This project takes a machine learning model from development to deployment and monitoring.



The system allows users to enter patient information through a Streamlit interface. The request is sent to a FastAPI backend, which loads the trained Logistic Regression model and returns a diabetes prediction.



The project also demonstrates important MLOps practices such as Docker, Git/GitHub, CI, prediction logging, data drift detection, model retraining, and model comparison.



###### \## 🏗️ Architecture



```text

User

&#x20; │

&#x20; ▼

Streamlit UI

&#x20; │

&#x20; ▼

FastAPI API

&#x20; │

&#x20; ▼

Logistic Regression Model

&#x20; │

&#x20; ▼

Prediction

&#x20; │

&#x20; ├──► Prediction Logging

&#x20; │

&#x20; └──► Monitoring

&#x20;         │

&#x20;         ▼

&#x20;     Data Drift

&#x20;         │

&#x20;         ▼

&#x20;     Retraining

&#x20;         │

&#x20;         ▼

&#x20;  Model Comparison

&#x20;         │

&#x20;         ▼

&#x20;   Champion Model

```



###### \## 🛠️ Technologies Used



\* Python

\* Pandas

\* Scikit-learn

\* Joblib

\* FastAPI

\* Uvicorn

\* Streamlit

\* Requests

\* Docker

\* Git

\* GitHub

\* GitHub Actions

\* Render

\* SciPy



###### \## 📂 Project Structure



```text

Logistic Regression/

│

├── Diabetes Prediction System.ipynb

├── diabetes.csv

├── diabetes\_model.pkl

├── diabetes\_model\_new.pkl

├── main.py

├── app.py

├── requirements.txt

├── Dockerfile

├── .gitignore

│

└── .github/

&#x20;   └── workflows/

&#x20;       └── ci.yml

```



###### \## 🧠 Machine Learning Model



The project uses \*\*Logistic Regression\*\* for binary classification.



The model predicts:



```text

0 → No Diabetes

1 → Diabetes

```



The model uses the following features:



\* Pregnancies

\* Glucose

\* Blood Pressure

\* Skin Thickness

\* Insulin

\* BMI

\* Diabetes Pedigree Function

\* Age



###### \## ⚡ FastAPI



FastAPI is used to expose the machine learning model as an API.



\### API Endpoints



\### Home



```text

GET /

```



Checks whether the API is running.



\### Health Check



```text

GET /health

```



Returns the API and model health status.



\### Prediction



```text

POST /predict

```



Accepts patient information and returns the prediction.



Example response:



```json

{

&#x20; "prediction": 1,

&#x20; "result": "Diabetes"

}

```



###### \## 🎨 Streamlit



Streamlit provides a simple web interface where users can enter patient information and request a prediction from the FastAPI backend.



###### \## 🐳 Docker



The FastAPI application is containerized using Docker.



\### Build Docker Image



```bash

docker build -t diabetes-api .

```



\### Run Container



```bash

docker run -d -p 8000:8000 --name diabetes-container diabetes-api

```



\### Check Running Containers



```bash

docker ps

```



\### Stop Container



```bash

docker stop diabetes-container

```



###### \## ☁️ Cloud Deployment



The FastAPI application was deployed using \*\*Render\*\* with Docker.



The deployment demonstrates how a containerized machine learning API can be made available through a public cloud endpoint.



###### \## 🔄 CI with GitHub Actions



GitHub Actions is used for Continuous Integration.



The workflow:



1\. Checks out the repository.

2\. Sets up Python.

3\. Installs project dependencies.

4\. Checks Python files for syntax errors.



Workflow file:



```text

.github/workflows/ci.yml

```



###### \## 📊 Prediction Monitoring



The FastAPI application records prediction information for monitoring.



The monitoring workflow records:



\* Timestamp

\* Glucose

\* BMI

\* Age

\* Prediction



This provides a basic way to observe incoming prediction data.



###### \## 📈 Data Drift Detection



Data drift occurs when the distribution of incoming production data becomes different from the training data.



For demonstration, production-like data was created by modifying the glucose distribution.



\### Training Data



```text

Glucose Mean ≈ 121.68

```



\### Simulated Production Data



```text

Glucose Mean ≈ 171.13

```



A Kolmogorov-Smirnov (KS) test was used to compare the distributions.



```text

KS Statistic ≈ 0.6015

p-value ≈ 1.86 × 10⁻⁵⁴

```



The result provided strong evidence that the two distributions were significantly different, demonstrating data drift.



###### \## 🔄 Model Retraining



After detecting drift, a new Logistic Regression model was trained as a challenger model.



The new model was evaluated against the existing production model using the same test data.



\### Model Comparison



| Model          | Accuracy |

| -------------- | -------: |

| Existing Model |   71.43% |

| New Model      |   70.78% |



Since the new model performed slightly worse, the existing model was retained as the production model.



```text

Existing Model → 🏆 Champion

New Model      → 🥊 Challenger

```



The challenger model was saved separately as:



```text

diabetes\_model\_new.pkl

```



This prevents an experimental model from accidentally replacing the production model.



###### \## 🔀 Git \& GitHub



Git is used for version control and GitHub is used to store the project remotely.



The project uses commits to track changes and GitHub Actions to perform automated CI checks.



###### \## 🚀 Running the Project Locally



\### 1. Create and activate virtual environment



```bash

python -m venv venv

```



PowerShell:



```powershell

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\\venv\\Scripts\\Activate.ps1

```



\### 2. Install dependencies



```bash

pip install -r requirements.txt

```



\### 3. Run FastAPI



```bash

python -m uvicorn main:app --reload

```



FastAPI will be available at:



```text

http://127.0.0.1:8000

```



Swagger documentation:



```text

http://127.0.0.1:8000/docs

```



\### 4. Run Streamlit



Open another terminal and run:



```bash

streamlit run app.py

```



Streamlit will open in the browser.



###### \## 🎯 MLOps Concepts Demonstrated



This project demonstrates:



\* Machine Learning model development

\* Model serialization

\* API deployment

\* FastAPI

\* Streamlit

\* Docker

\* Cloud deployment

\* Git and GitHub

\* Continuous Integration

\* Prediction logging

\* Monitoring

\* Data drift detection

\* KS statistical test

\*Model retraining

\*Model evaluation

\*Model versioning

\*Champion-challenger model comparison



##### 👨‍💻 Author



###### **Navtesh Deore**



###### **GitHub: navteshdeore19-lang**

