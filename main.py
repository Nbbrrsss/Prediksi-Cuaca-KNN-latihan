import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

model = pickle.load(open('model.pkl','rb'))

#streamlit app
st.title("Prediksi Cuaca Di Indonesia")
st.write('Masukan Rincian prediksi cuaca')

#inputan
new_temp_max        = st.slider("Masukan Temperature Maximal : ", -100.0, 100.0)
new_temp_min        = st.slider("Masukan Temperature Minimal : ", -100.0, 100.0)
new_precipitation   = st.text_input("Masukan pengendapan : ")
new_wind            = st.text_input("Masukan Tekanan angin : ")

#tombol prediksi
if st.button('Prediksi'):
    if new_precipitation != '' and new_temp_max != '' and new_temp_min != '' and new_wind != '':
        new_precipitation = float(new_precipitation)
        new_temp_max = float(new_temp_max)
        new_temp_min = float(new_temp_min)
        new_wind = float(new_wind)

        prediksi = model.predict([[new_precipitation, new_temp_max, new_temp_min, new_wind]])
        if prediksi == 1 : 
            st.success("Cuaca = Mendung")
        elif prediksi == 2 : 
            st.success("Cuaca = Salju")
        elif prediksi == 3 : 
            st.success("Cuaca = Hujan")
        elif prediksi == 4 : 
            st.success("Cuaca = Cerah")
        elif prediksi == 5 : 
            st.success("Cuaca =Berkabut")
    else:
        st.write("Mohon lengkapi semua input sebelum melakukan prediksi.")