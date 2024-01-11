#Start Import Library
import streamlit as st #Library buat class streamlit
import pandas as pd #Library buat membaca dataset
import numpy as np
import pickle

#End Of Import

#Start Load Dataset
df = pd.read_csv("prediksicuaca.csv") #untuk membaca data
#st.dataframe(df)
#End Load Dataset

#Start Load Model
model = pickle.load(open('model.pkl','rb')) #untuk membaca model
#End Load Model

#Start Navbar
tab1,tab2,tab3,tab4 = st.tabs(["Menu Utama","Analisis Cuaca","Dataset","App"])
#End navbar

#Start Halaman Menu Utama
with tab1:
    st.image('Banner_cuaca.jpg')
    st.header("Perubahan Cuaca Selama 3 Tahun")
    st.write("Nibras Bahy Ardyansyah (A11.2021.13515)")
    st.divider()
    st.write("Perubahan cuaca adalah fenomena alam yang terus-menerus memengaruhi kondisi atmosfer di seluruh dunia. Cuaca dapat berubah dari satu hari ke hari berikutnya, dan ini dipengaruhi oleh berbagai faktor seperti suhu, tekanan udara, kelembaban, dan arah angin. Dalam cuaca, terdapat beragam kondisi yang dapat kita temui, seperti kabut (fog), hujan (rain), matahari (sun), gerimis (drizzle), dan salju (snow).")

    st.write("Kabut, misalnya, adalah kondisi di mana partikel air sangat kecil mengambang di udara dan mengurangi jarak pandang, sering terjadi di pagi hari saat suhu udara dingin. Hujan adalah turunnya butiran-butiran air dari atmosfer yang dapat muncul dalam berbagai intensitas, dari gerimis hingga hujan lebat. Matahari adalah sumber cahaya dan panas utama bagi planet kita yang mendukung kehidupan. Gerimis adalah hujan ringan yang terdiri dari tetesan air kecil, sering kali cukup untuk membuat permukaan tanah menjadi basah. Salju adalah kristal es yang turun dari langit dan dapat menciptakan pemandangan yang indah saat menutupi permukaan bumi.")

    st.write("Semua perubahan cuaca ini memiliki dampak yang berbeda pada kehidupan kita dan ekosistem di sekitar kita, dan pemahaman tentang fenomena cuaca ini penting untuk mengatasi tantangan yang terkait dengan perubahan iklim dan adaptasi di era modern ini.")
#End Halaman Menu Utama

#Start Halaman Analisis Cuaca
with tab2:
    st.header("Analisis Cuaca 2012 - 2015")
    st.write("Nibras Bahy Ardyansyah (A11.2021.13515)")
    st.divider()
    st.write("Dari dataset yang didapatkan dari pembuat,ada beberapa hal yang dapat diulas dari dataset Prediksi cuaca 2012-2015. Mulai dari yang pertama yaitu Analisis Frekuensi cuaca.")

    Dataku = df["weather"].value_counts()
    st.bar_chart(Dataku)
    st.write("Pada 3 tahun terahkir 2012-2015, cuaca yang sering dijumpai ialah hujan dan matahari. Dari kedua cuaca in menunjukkan bahwa 2 cuaca tersebut dominan di bulan bulan tertentu, sedangkan berkabut gerimis dan bersalju sangat jarang")

#End Halaman Analisis Cuaca
    
#Start Halaman Dataset
with tab3:
    st.header("Tentang dataset : Prediksi Cuaca")
    st.write("Nibras Bahy Ardyansyah (A11.2021.13515)")
    st.divider()
    st.write("Data set tentang 'Prediksi Cuaca' berisikan data yang mengenai time series dari tahun 2012 hingga tahun 2015. Tidak hanya waktunya saja, melainkan juga faktor faktor yang mempengaruhi hasil cuaca tersebut. Atribut tersebut diantaranya ada pengendapat, temperatur maksimal, temperatur minimal dan kecepatan angin. Dari hasil dataset yang ada, berisikan data sebanyak 1460 buah data dari tahun 2012 hingga 2015")
    
    st.dataframe(df,width=1500,height=500,hide_index=True)
    st.write("Berikut adalah Deskripsi dari atribut atribut yang ada pada dataset")

    datanama = pd.DataFrame([
        {"Atribut":"Date","Deskripsi":"Tanggal kejadian cuaca tersebut"},
        {"Atribut":"precipitation","Deskripsi":"Tingkat curah hujan pada hari itu"},
        {"Atribut":"temp_max","Deskripsi":"Temperatur maksimal pada hari itu"},
        {"Atribut":"temp_min","Deskripsi":"Temperatur minimal pada hari itu"},
        {"Atribut":"wind","Deskripsi":"Kecepatan angin di hari itu"},
        {"Atribut":"weather","Deskripsi":"Nama cuaca"},
        {"Atribut":"Prediciton","Deskripsi":"label dari nama cuaca"},
    ])
    st.dataframe(datanama,width=1500, height=280, hide_index=True)

    st.write("Dari dataset diatas, dataset ini tergolong dataset yang bersih, dimana tidak mengandung missing value sama sekali. Akan tetapi data ini mengandung data yang tidak seimbang yang dimana jumlah klasifikasi antar kelas jumlahnya tidak sama/ tidak seimbang. Bila tidak memiliki dataset, silahkan download di tombol ini !")

    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    csv = convert_df(df)

    st.download_button(
        label="Download dataset",
        data=csv,
        file_name='prediksicuaca.csv',
        mime='text/csv',
    )

    st.write("Link dataset di Kaggle : https://www.kaggle.com/datasets/ananthr1/weather-prediction ")
#End Halaman Dataset

#Start Halaman App
with tab4:
    st.header("Prediksi cuaca hari ini")
    st.write("Nibras Bahy Ardyansyah (A11.2021.13515)")
    st.divider()
    st.write("Halo! Sekarang kamu ada pada halaman prediksi cauca yang telah dibuat oleh penulis kode ini. Silahkan masukan aspek aspek yang ada kolom dibawah ini. Setelah kalian memasukkan data data yang dibutuhkan oleh prediksi cuaca ini, silahkan kalian tekan tombol prediksi cuaca. Nanti hasil prediksi akan muncul di sebelah kanan pada halaman ini. Selamat mencoba")
    colform1,colform2 = st.columns(2)
    #inputan
    with colform1:
        new_precipitation   = st.number_input("Masukan pengendapan : ")
        new_temp_max        = st.number_input("Masukan Temperature Maximal : ")
       
    with colform2:
        new_wind            = st.number_input("Masukan Tekanan angin : ")
        new_temp_min        = st.number_input("Masukan Temperature Minimal : ")
        

    if st.button('Prediksi'):
        if new_precipitation != '' and new_temp_max != '' and new_temp_min != '' and new_wind != '':
            new_precipitation = float(new_precipitation)
            new_temp_max = float(new_temp_max)
            new_temp_min = float(new_temp_min)
            new_wind = float(new_wind)

            prediksi = model.predict([[new_precipitation, new_temp_max, new_temp_min, new_wind]])
            if prediksi == 1 :
                st.header("Cuaca = :red[Mendung] :sunglasses:") 
            elif prediksi == 2 :
                st.header("Cuaca = :violet[Salju] :sunglasses:") 
            elif prediksi == 3 : 
                st.header("Cuaca = :blue[Hujan] :sunglasses:")
            elif prediksi == 4 : 
                st.header("Cuaca = :orange[Cerah] :sunglasses:")
            elif prediksi == 5 : 
                st.header("Cuaca = :violet[Berkabut] :sunglasses:")
        else:
            st.write("Mohon lengkapi semua input sebelum melakukan prediksi.")
#End Halaman App