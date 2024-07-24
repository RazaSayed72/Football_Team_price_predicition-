# Create the Streamlit app script
with open('app.py', 'w') as f:
    f.write('''
import pickle
import pandas as pd
import streamlit as st

# Load your trained model
with open('regressor_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the scaler
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

def predict_value(input_data):
    # Assume input_data is a dictionary of features
    df = pd.DataFrame([input_data])
    scaled_data = scaler.transform(df)
    prediction = model.predict(scaled_data)
    return prediction[0]

... # Streamlit interface
... st.title('Value Prediction')
... st.write("Enter the details to predict the value:")
... 
... # Collect user input
... input_data = {}
... input_data['club'] = st.number_input('Club', min_value=0, max_value=19, value=9)
... input_data['age'] = st.number_input('Age', min_value=17, max_value=38, value=26)
... input_data['position'] = st.number_input('Position', min_value=0, max_value=12, value=4)
... input_data['position_cat'] = st.number_input('Position Category', min_value=1, max_value=4, value=2)
... input_data['market_value'] = st.number_input('Market Value', min_value=0.05, max_value=75000000.0, value=1100000.0, step=100000.0)
... input_data['page_views'] = st.number_input('Page Views', min_value=3, max_value=7664, value=764)
... input_data['fpl_value'] = st.number_input('FPL Value', min_value=4, max_value=13, value=6)
... input_data['fpl_sel'] = st.number_input('FPL Selection', min_value=0, max_value=1000, value=34)
... input_data['fpl_points'] = st.number_input('FPL Points', min_value=0, max_value=264, value=51)
... input_data['region'] = st.number_input('Region', min_value=0, max_value=4, value=2)
... input_data['nationality'] = st.number_input('Nationality', min_value=0, max_value=60, value=27)
... input_data['new_foreign'] = st.selectbox('New Foreign', [0, 1])
... input_data['age_cat'] = st.number_input('Age Category', min_value=1, max_value=3, value=2)
... input_data['club_id'] = st.number_input('Club ID', min_value=1, max_value=20, value=10)
... input_data['big_club'] = st.selectbox('Big Club', [0, 1])
... input_data['new_signing'] = st.selectbox('New Signing', [0, 1])
... 
... # Predict and display result
... if st.button('Predict'):
...     result = predict_value(input_data)
...     st.write(f'Predicted Value: {result}')
... ''')
