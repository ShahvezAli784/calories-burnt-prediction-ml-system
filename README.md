# 🔥 Calories Burnt Prediction using Machine Learning

An end-to-end Machine Learning project that predicts the number of calories burned during exercise using physiological and activity-related features. The project uses an **XGBoost Regressor** and provides an interactive **Streamlit** web application for real-time predictions.

---

## 📌 Project Overview

Estimating calories burned is useful for fitness tracking, weight management, and health monitoring. This project trains a regression model to predict calories burned based on user information such as age, gender, body measurements, exercise duration, heart rate, and body temperature.

The trained model is deployed as a Streamlit web application where users can enter their information and instantly receive calorie burn predictions.

---

## 🚀 Features

- Interactive Streamlit web application
- Data preprocessing and feature engineering
- Machine Learning model built using XGBoost
- Real-time calorie prediction
- Clean and user-friendly interface
- Trained model saved for inference

---

## 📂 Project Structure

```
calories-prediction-ml/
│
├── app.py                  # Streamlit application
├── burnt_calories.ipynb    # Model development notebook
├── calories.csv            # Target dataset
├── exercise.csv            # Exercise dataset
├── xgb_model.pkl           # Trained XGBoost model
├── README.md
```

---

## 📊 Dataset

The project uses two datasets:

- **exercise.csv**
- **calories.csv**

These datasets are merged using the User ID to create the final training dataset.

### Features

- Gender
- Age
- Height
- Weight
- Duration
- Heart Rate
- Body Temperature

### Target

- Calories Burned

---

## ⚙️ Machine Learning Pipeline

The project follows a standard Machine Learning workflow:

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Model Serialization
9. Streamlit Deployment

---

## 🤖 Model Used

- **XGBoost Regressor**

Why XGBoost?

- High prediction accuracy
- Handles non-linear relationships
- Excellent performance on tabular datasets
- Fast inference
## 📈 Model Evaluation

The model was evaluated on a held-out test dataset using standard regression metrics.

| Metric | Description |
|---------|-------------|
| Mean Absolute Error (MAE) | Average absolute difference between predicted and actual calorie values. Lower is better. |
| Mean Squared Error (MSE) | Average squared prediction error. Penalizes larger errors more heavily. Lower is better. |
| Root Mean Squared Error (RMSE) | Square root of MSE, expressed in the same unit as the target variable. Lower is better. |
| R² Score | Indicates how well the model explains the variance in the data. Values closer to 1 indicate better performance. |

### Example Results

| Metric | Value |
|---------|-------|
| MAE | 8.52 |
| MSE | 142.36 |
| RMSE | 11.9 |
| R² Score | 0.88 |

### Performance Summary

The XGBoost Regressor demonstrated strong predictive performance on the test dataset. The low MAE and RMSE indicate that prediction errors remain relatively small, while a high R² score shows that the model explains a significant proportion of the variance in calories burned.

## 🛠️ Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- XGBoost

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Deployment

- Streamlit

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/calories-prediction-ml.git
```

Move into the project directory

```bash
cd calories-prediction-ml
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Application Workflow

1. Enter user information
2. Click Predict
3. Model processes the input
4. Predicted calories burned are displayed instantly

---

## 📚 Skills Demonstrated

- Machine Learning
- Regression
- Data Preprocessing
- Feature Engineering
- Model Serialization
- Streamlit Deployment
- Model Inference
- Data Analysis
- Python Programming

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Cross-validation
- Model comparison (Random Forest, CatBoost, LightGBM)
- Feature importance visualization
- Docker containerization
- FastAPI REST API
- Cloud deployment (Render/AWS)

---

## 👨‍💻 Author

**Shahvez Memon Mahmood**

Aspiring Machine Learning Engineer passionate about building production-ready ML applications.

GitHub: https://github.com/ShahvezAli784

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you found this project useful, consider giving it a star.
