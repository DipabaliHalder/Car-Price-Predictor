import streamlit as st
import numpy as np
import pandas as pd
import pickle


pipe=pickle.load(open('pipe.pkl','rb'))

st.header('Car Price Predictor')

# year
year = st.number_input('Year Of Manufacture',2000,2020)
# km driven
km_driven=st.number_input('KMs driven')
# fuel
fuel = st.selectbox('Fuel Type',('Diesel', 'Petrol'))
# seller type
seller_type = st.selectbox('Seller Type',('Individual', 'Dealer'))
# transmission
transmmn = st.selectbox('Transmission',('Manual', 'Automatic'))
# owner
owner = st.selectbox('Owner',('First Owner', 'Second Owner', 'Third Owner'))# mileage
mileage = st.number_input('Mileage')
# engine
engine = st.number_input('Engine', 0)
# max power
max_power=st.number_input('Max Power')
# seats
seats = st.number_input('Seats', 0, 14)
# brand
brand = st.selectbox('Brand',(np.sort(['Maruti', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra', 'Tata', 'Chevrolet', 'Volkswagen'])))

#predicted price
if st.button('Predict Price'):
    #form a numpy array(1,11)
    input = np.array([[year, kms, fuel, seller_type, transmmn, owner, mileage, engine, max_power, seats, brand]])
    input = pd.DataFrame(input,columns=['year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats','brand'])
    y_pred = pipe.predict(input)
    st.header("Rs. " + str(np.round(y_pred[0])))
