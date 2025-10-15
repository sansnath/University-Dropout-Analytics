import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Prediksi Status Mahasiswa", page_icon="🎓", layout="wide")

st.markdown("""
    <h1 style='text-align: center;'>🎓 Prediksi Status Mahasiswa</h1>
    <p style='text-align: center; color: gray;'>
        Model berbasis <b>PCA + XGBoost</b> dengan fitur demografis, akademik, dan sosial-ekonomi.
    </p>
""", unsafe_allow_html=True)

model = joblib.load("model/best_xgb_model.joblib")
pca = joblib.load("model/pca_model.pkl")
scaler = joblib.load("model/scaler.pkl")
important_features = joblib.load("model/important_features.pkl")

if hasattr(scaler, "feature_names_in_"):
    all_features = scaler.feature_names_in_
else:
    all_features = important_features

marital_status_options = {
    1: "Single", 2: "Married", 3: "Widower", 4: "Divorced",
    5: "Facto Union", 6: "Legally Separated"
}
application_mode_options = {
    1: "1st phase - general contingent", 2: "Ordinance No. 612/93",
    5: "Special contingent (Azores)", 7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99", 15: "International student (bachelor)",
    16: "Special contingent (Madeira)", 17: "2nd phase - general",
    18: "3rd phase - general", 26: "Ordinance 533-A/99 (Diff. Plan)",
    27: "Ordinance 533-A/99 (Other Inst.)", 39: "Over 23 years old",
    42: "Transfer", 43: "Change of course", 44: "Tech diploma holders",
    51: "Change of institution/course", 53: "Short cycle diploma",
    57: "Intl. change of course"
}
course_options = {
    33: "Biofuel Tech", 171: "Animation & Multimedia", 8014: "Social Serv (Evening)",
    9003: "Agronomy", 9070: "Comm Design", 9085: "Vet Nursing", 9119: "Info Engineering",
    9130: "Equinculture", 9147: "Management", 9238: "Social Service",
    9254: "Tourism", 9500: "Nursing", 9556: "Oral Hygiene",
    9670: "Advert & Mktg Mgmt", 9773: "Journalism & Comm", 9853: "Basic Education",
    9991: "Mgmt (Evening)"
}
previous_qualification_options = {
    1: "Secondary education", 2: "Bachelor", 3: "Degree", 4: "Master", 5: "Doctorate",
    6: "Freq. of higher education", 9: "12th year - not completed", 10: "11th year - not completed",
    12: "Other - 11th year", 14: "10th year", 15: "10th year - not completed",
    19: "Basic education 3rd cycle", 38: "Basic education 2nd cycle",
    39: "Technological specialization", 40: "Degree (1st cycle)",
    42: "Prof. higher technical", 43: "Master (2nd cycle)"
}
nationality_options = {
    1: "Portuguese", 2: "German", 6: "Spanish", 11: "Italian", 13: "Dutch",
    14: "English", 17: "Lithuanian", 21: "Angolan", 22: "Cape Verdean",
    24: "Guinean", 25: "Mozambican", 26: "Santomean", 32: "Turkish",
    41: "Brazilian", 62: "Romanian", 100: "Moldovan", 101: "Mexican",
    103: "Ukrainian", 105: "Russian", 108: "Cuban", 109: "Colombian"
}
binary_options = {1: "Yes", 0: "No"}
gender_options = {1: "Male", 0: "Female"}
daytime_options = {1: "Daytime", 0: "Evening"}

st.markdown("### 👤 Informasi Demografis")
col1, col2, col3 = st.columns(3)
user_input = {}

with col1:
    user_input["Gender"] = st.selectbox("Gender", list(gender_options.keys()), format_func=lambda x: gender_options[x])
    user_input["Marital_status"] = st.selectbox("Marital Status", list(marital_status_options.keys()), format_func=lambda x: marital_status_options[x])
    user_input["Nacionality"] = st.selectbox("Nationality", list(nationality_options.keys()), format_func=lambda x: nationality_options[x])

with col2:
    user_input["Age_at_enrollment"] = st.number_input("Age at Enrollment", 15, 70, 19)
    user_input["International"] = st.selectbox("International", list(binary_options.keys()), format_func=lambda x: binary_options[x])
    user_input["Displaced"] = st.selectbox("Displaced", list(binary_options.keys()), format_func=lambda x: binary_options[x])

with col3:
    user_input["Scholarship_holder"] = st.selectbox("Scholarship Holder", list(binary_options.keys()), format_func=lambda x: binary_options[x])
    user_input["Educational_special_needs"] = st.selectbox("Special Needs", list(binary_options.keys()), format_func=lambda x: binary_options[x])

st.markdown("---")
st.markdown("### 🎓 Informasi Akademik")
col4, col5 = st.columns(2)
with col4:
    user_input["Application_mode"] = st.selectbox("Application Mode", list(application_mode_options.keys()), format_func=lambda x: application_mode_options[x])
    user_input["Application_order"] = st.number_input("Application Order (0–9)", 0, 9, 0)
    user_input["Course"] = st.selectbox("Course", list(course_options.keys()), format_func=lambda x: course_options[x])
    user_input["Daytime/evening_attendance"] = st.selectbox("Attendance", list(daytime_options.keys()), format_func=lambda x: daytime_options[x])

with col5:
    user_input["Previous_qualification"] = st.selectbox("Previous Qualification", list(previous_qualification_options.keys()), format_func=lambda x: previous_qualification_options[x])
    user_input["Previous_qualification_grade"] = st.number_input("Previous Qualification Grade", 0.0, 200.0, 150.0)
    user_input["Admission_grade"] = st.number_input("Admission Grade", 0.0, 200.0, 150.0)

st.markdown("---")
st.markdown("### 📚 Data Nilai Akademik per Semester")
for sem in ["1st", "2nd"]:
    st.markdown(f"**Semester {sem}**")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        user_input[f"Curricular_units_{sem}_sem_credited"] = st.number_input(f"Credited ({sem})", 0, 10, 0)
        user_input[f"Curricular_units_{sem}_sem_approved"] = st.number_input(f"Approved ({sem})", 0, 10, 5)
    with col_b:
        user_input[f"Curricular_units_{sem}_sem_enrolled"] = st.number_input(f"Enrolled ({sem})", 0, 10, 6)
        user_input[f"Curricular_units_{sem}_sem_evaluations"] = st.number_input(f"Evaluations ({sem})", 0, 10, 6)
    with col_c:
        user_input[f"Curricular_units_{sem}_sem_grade"] = st.number_input(f"Avg Grade ({sem})", 0.0, 20.0, 14.0)
        user_input[f"Curricular_units_{sem}_sem_without_evaluations"] = st.number_input(f"Without Eval ({sem})", 0, 10, 0)

st.markdown("---")
st.markdown("### 💰 Sosial Ekonomi")
col7, col8, col9 = st.columns(3)
with col7:
    user_input["Debtor"] = st.selectbox("Debtor", list(binary_options.keys()), format_func=lambda x: binary_options[x])
with col8:
    user_input["Tuition_fees_up_to_date"] = st.selectbox("Tuition Fees Up To Date", list(binary_options.keys()), format_func=lambda x: binary_options[x])
with col9:
    user_input["GDP"] = st.number_input("GDP (%)", -10.0, 10.0, 2.5)

col10, col11 = st.columns(2)
with col10:
    user_input["Unemployment_rate"] = st.number_input("Unemployment Rate (%)", 0.0, 100.0, 6.5)
with col11:
    user_input["Inflation_rate"] = st.number_input("Inflation Rate (%)", 0.0, 50.0, 1.8)


st.markdown("---")
st.markdown("## 🚀 Hasil Prediksi")

if st.button("🔮 Prediksi Status Mahasiswa", use_container_width=True):
    user_df = pd.DataFrame([user_input])

    for col in all_features:
        if col not in user_df.columns:
            user_df[col] = 0
    user_df = user_df[all_features]

    user_scaled = scaler.transform(user_df)
    scaled_subset = pd.DataFrame(user_scaled, columns=all_features)[important_features]
    user_pca = pca.transform(scaled_subset)

    prediction = model.predict(user_pca)
    prediction_proba = model.predict_proba(user_pca)[0]

    label_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}

    st.success(f"🎯 **Prediksi Status Mahasiswa:** {label_map.get(prediction[0], prediction[0])}")

    st.progress(float(prediction_proba[prediction[0]]))
    st.write("### Probabilitas Tiap Kelas:")
    for label, prob in zip(label_map.values(), prediction_proba):
        st.write(f"- **{label}:** {prob:.4f}")

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("📘 Dibuat oleh Samuel Nathanael")
