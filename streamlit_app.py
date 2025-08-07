import streamlit as st
import requests

st.set_page_config(page_title="Obesity Prediction App", layout="centered")

st.title("Prediksi Tingkat Obesitas")
st.write("Masukkan data berikut untuk memprediksi tingkat obesitas:")

# Form input pengguna
with st.form("prediction_form"):
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", min_value=1, max_value=100)
    Height = st.number_input("Height (meter)", min_value=1.0, max_value=2.5)
    Weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0)
    family_history_with_overweight = st.selectbox("Family History with Overweight", ["yes", "no"])
    FAVC = st.selectbox("Frequent consumption of high caloric food", ["yes", "no"])
    FCVC = st.slider("Frequency of consumption of vegetables (0–3)", 0.0, 3.0, 1.0)
    NCP = st.slider("Number of main meals", 1.0, 5.0, 3.0)
    CAEC = st.selectbox("Consumption of food between meals", ["no", "Sometimes", "Frequently", "Always"])
    SMOKE = st.selectbox("Do you smoke?", ["yes", "no"])
    CH2O = st.slider("Daily water intake (liters)", 0.0, 3.0, 1.0)
    SCC = st.selectbox("Calories consumption monitoring", ["yes", "no"])
    FAF = st.slider("Physical activity frequency (hours per week)", 0.0, 5.0, 1.0)
    TUE = st.slider("Time using technology devices (hours)", 0.0, 5.0, 1.0)
    CALC = st.selectbox("Alcohol consumption", ["no", "Sometimes", "Frequently", "Always"])
    MTRANS = st.selectbox("Transportation used", ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"])

    submit = st.form_submit_button("Predict")

# Jika form disubmit
if submit:
    # Data dalam format JSON untuk dikirim ke API
    input_data = {
        "Gender": Gender,
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "family_history_with_overweight": family_history_with_overweight,
        "FAVC": FAVC,
        "FCVC": FCVC,
        "NCP": NCP,
        "CAEC": CAEC,
        "SMOKE": SMOKE,
        "CH2O": CH2O,
        "SCC": SCC,
        "FAF": FAF,
        "TUE": TUE,
        "CALC": CALC,
        "MTRANS": MTRANS
    }

    try:
        # Kirim POST request ke backend FastAPI
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediksi: {result['predicted_class']}")
        else:
            st.error("Gagal memproses prediksi. Pastikan API sedang berjalan dan data valid.")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
