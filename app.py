import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib

model = joblib.load('knn_model.pkl')

speed_limit = st.slider('Speed Limit', 0, 100)

x_center = st.text_input('X Center')
y_center = st.text_input('Y Center')

class_names = ['Class 1', 'Class 2', 'Class 3']
selected_class = st.selectbox('Select a Class', class_names)

if st.button('Run Model'):
    # Convert inputs to a DataFrame
    input_df = pd.DataFrame({'speedLimit': speed_limit,
                             'xCenter': x_center,
                             'yCenter': y_center},
                             index=[0])
    
    prediction = model.predict(input_df)
    
    st.write(f'The predicted class is: {prediction}')