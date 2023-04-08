import os
import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib
import sys

def main():
    st.set_page_config(page_title="My Streamlit App", page_icon=None, layout="centered", initial_sidebar_state="auto")
    st.write("Streamlit app is running!")

    # Load the model
    model = joblib.load('knn_model.pkl')

    # Define the input widgets
    speed_limit = st.slider('Speed Limit', 0, 100)
    x_center = st.text_input('X Center')
    y_center = st.text_input('Y Center')
    class_names = ['Class 1', 'Class 2', 'Class 3']
    selected_class = st.selectbox('Select a Class', class_names)

    # Handle button click
    if st.button('Run Model'):
        # Convert inputs to a DataFrame
        input_df = pd.DataFrame({'speedLimit': speed_limit,
                                 'xCenter': x_center,
                                 'yCenter': y_center},
                                 index=[0])
        prediction = model.predict(input_df)
        st.write(f'The predicted class is: {prediction}')

if __name__ == "__main__":
    main()
