# Crop-Production Prediction Using Machine Learning
Project Summary  
This project focuses on predicting crop production using a machine learning pipeline. It incorporates data cleaning, exploratory data analysis (EDA), data visualization, dashboard creation, and regression modeling to provide an end-to-end solution for analyzing and predicting crop yields. Below are the detailed steps of the workflow:  

---

### Steps of the Project  

#### 1. **Dataset Cleaning and Preprocessing**  
- **Tools Used:** Python, Pandas  
- Loaded the raw crop production dataset.  
- Cleaned the dataset by handling missing values, removing duplicates, and ensuring consistent formatting.  
- Preprocessed the data by encoding categorical variables, scaling numerical values, and preparing the dataset for analysis.  

#### 2. **Exploratory Data Analysis (EDA)**  
- **Tools Used:** Matplotlib, Seaborn  
- Performed detailed analysis of the cleaned dataset to identify patterns, correlations, and trends in the data.  
- Visualized relationships between variables using bar plots, scatter plots, heatmaps, and pair plots to gain insights into the dataset.  

#### 3. **Data Export for Dashboard Creation**  
- Converted the processed dataframe into a CSV file to enable external tools to utilize the dataset.  
- **Dashboard Created:** *Crops Production Analysis Dashboard*  
- **Tool Used:** Power BI  
  - Built an interactive dashboard in Power BI to visualize crop production trends, distributions, and other key metrics.  

#### 4. **Machine Learning Modeling**  
- **Tools Used:** Scikit-learn  
- Trained multiple regression models on the dataset to predict crop production:  
  - Linear Regression  
  - Random Forest Regression  
- Evaluated the models' performance using metrics like R² score.  
- Random Forest Regression performed the best and was selected as the final model.  

#### 5. **Model Deployment Preparation**  
- Saved the trained Random Forest Regression model using `joblib`.  
- The trained model was prepared for deployment by exporting it for further integration.  

#### 6. **Streamlit Application Development**  
- **Tool Used:** Streamlit  
- Created an interactive web application named *Crop Production Predict Application*.  
- Integrated the saved Random Forest model into the application to provide real-time crop production predictions.  

---

### Repository Contents  
- **`CROPS_PRODUCTION_PREDICTION.ipynb`**: Jupyter Notebook containing the data preprocessing, EDA, and machine learning model training.  
- **Power BI Dashboard File**: Power BI file for the *Crops Production Analysis Dashboard*.  
- **Trained Model File (`random_forest_model.joblib`)**: Saved Random Forest model for deployment.  
- **Streamlit App Code**: Python script for the Crop Production Predict Application.  

---

### Skills and Tools Demonstrated  
- **Data Cleaning and Preprocessing:** Python (Pandas)  
- **EDA and Visualization:** Matplotlib, Seaborn  
- **Dashboard Creation:** Power BI  
- **Machine Learning:** Scikit-learn (Regression Models)  
- **Model Deployment:** Streamlit  

This project showcases a complete workflow for crop production analysis and prediction, combining data science, machine learning, and deployment skills into one comprehensive solution.
