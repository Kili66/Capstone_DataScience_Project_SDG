import joblib
import streamlit as st 
import streamlit_option_menu
from streamlit_option_menu import option_menu 
import numpy as np
import pickle

#load the models

#diabetes_model= pickle.load(open('diabetes_model.sav','rb'))
# heart_model= pickle.load(open('mymodels/heart_model.sav','rb'))
# parkinson_model= pickle.load(open('mymodels/parkinson_model.sav','rb'))
diabetes_model= joblib.load(open('diabetes_model.joblib','rb'))
heart_model= joblib.load(open('heart_model.joblib','rb'))
parkinson_model= joblib.load(open('parkinson_model.joblib','rb'))
with st.sidebar:
    selected= option_menu('Multiple Chronic Disease Prediction System',
                          ['Diabetes Disease Prediction',
                          'Heart Disease Prediction',
                          'Parkinson Disease Prediction'
                          ], icons=['activity','heart-pulse','person'], default_index= 0)
### Diabetes Disease-----------------------------------------------
if selected=='Diabetes Disease Prediction':
    st.title('Diabetes Disease Prediction') # page title
    # User inputs
    col1, col2, col3=st.columns(3)
    
    with col1:
        Pregnancies= st.text_input("Number of times pregnant")
    with col2:
        Glucose=  st.text_input(" glucose concentration")
    with col3:
        BloodPressure= st.text_input("blood pressure (mm Hg)")
    with col1:
        SkinThickness= st.text_input("Triceps skin fold thickness (mm)")
    with col2:
        Insulin=st.text_input(" insulin (mu U/ml)")
    with col3:
        BMI= st.text_input("Enter Body mass index of Patient")
    with col1:
        DiabetesPedigreeFunction= st.text_input("Diabetes pedigree function value")
    with col2:
        Age= st.text_input("Enter the age of the patient")
    #Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
    # Prediction for diabets disease
    diab_diagnosis=''

#if st.button("Diabetes Test result"):
    
#     diabete_pred=diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
#     if (diabete_pred[0]==1):
#         diab_diagnosis="The person is diabetic"
#     else:
#         diab_diagnosis="The person is not diabetic"
# st.success(diab_diagnosis)
# Prediction

    if st.button("Diabetes Test result"):
        try:
        # Convert input features to numeric values
            features = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            features = [float(feature) for feature in features]

            # Predict using XGBoost model
            diabete_pred = diabetes_model.predict([features])

            # Update diagnosis based on prediction
            if diabete_pred == 1:
                diab_diagnosis = "The person is diabetic"
            else:
                diab_diagnosis = "The person is not diabetic"

        except Exception as e:
            st.error(f"Error predicting diabetes: {e}")
            diab_diagnosis = "Prediction error"

    st.success(diab_diagnosis)
### Heart Disease-----------------------------------------
if selected=='Heart Disease Prediction':
    st.title("Heart Disease Prediction ") #page TiTLE
    #user inputs
    col1, col2, col3=st.columns(3)
    #age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal
    with col1:
        age= st.text_input("Age of the person")
    with col2:
        sex=  st.text_input("sex")
    with col3:
        cp= st.text_input("cheast pain value")
    with col1:
        trestbps= st.text_input("resting blood pressure(trestbps)value")
    with col2:
        chol=st.text_input("serum cholestoral in mg/dl value")
    with col3:
        fbs= st.text_input("fasting blood sugar > 120 mg/dl of Patient")
    with col1:
        restecg= st.text_input("resting electrocardiographic results (values 0,1,2)")
    with col2:
        thalach= st.text_input("Enter the maximum heart rate achieved")
    with col3:
        exang= st.text_input("exercise induced angina value")
    with col1:
        oldpeak= st.text_input("Enter the oldpeak = ST depression induced by exercise relative to rest")
    with col2:
        slope= st.text_input("Enter the slope of the peak exercise ST segment")
    with col3:
        ca= st.text_input("number of major vessels (0-3) colored by flourosopy")
    with col1:
        thal= st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
    heart_diagnosis=' '
    if st.button("Heart Disease Test result"):
        
        try:
        # Convert input features to numeric values
            features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            features = [float(feature) for feature in features]

            # Predict using XGBoost model
            heart_pred = heart_model.predict([features])

            # Update diagnosis based on prediction
            if heart_pred == 1:
                heart_diagnosis = "The person has heart disease"
            else:
                heart_diagnosis = "The person doesn't have heart disease"

        except Exception as e:
            st.error(f"Error predicting diabetes: {e}")
            heart_diagnosis = "Prediction error"

    st.success(heart_diagnosis)
        
        
## Parkinson---------------------------------------------     
if selected=='Parkinson Disease Prediction':
    st.title("Parkinson Disease Prediction ") #PAGE TILE
    col1, col2, col3, col4, col5=st.columns(5)
    #MDVP:Fo(Hz)         0
        # MDVP:Fhi(Hz)        0
        # MDVP:Flo(Hz)        0
        # MDVP:Jitter(%)      0
        # MDVP:Jitter(Abs)    0
        # MDVP:RAP            0
        # MDVP:PPQ            0
        # Jitter:DDP          0
        # MDVP:Shimmer        0
        # MDVP:Shimmer(dB)    0
        # Shimmer:APQ3        0
        # Shimmer:APQ5        0
        # MDVP:APQ            0
        # Shimmer:DDA         0
        # NHR                 0
        # HNR                 0
        # status              0
        # RPDE                0
        # DFA                 0
        # spread1             0
        # spread2             0
        # D2                  0
        # PPE 
    with col1:
        MDVP_Fo= st.text_input("MDVP_Fo-Avg vocal fund freq")
    with col2:
        MDVP_Fhi=  st.text_input("MDVP:Fhi-Max vocal fund freq")
    with col3:
        MDVP_Flo= st.text_input("MDVP:Flo-Min vocal fund freq")
    with col4:
        MDVP_Jitter= st.text_input("MDVP:Jitter-mesr1 of var in fund. freq.")
    with col5:
        MDVP_Jitter_Abs=st.text_input("MDVP_Abs-mesr2 of var in fund. freq.")
    with col1:
        MDVP_RAP= st.text_input("DVP_RAP-mesr3 of var in fund. freq.")
    with col2:
        MDVP_PPQ= st.text_input("MDVP:PPQ-mesr4 of var in fund. freq.")
    with col3:
        Jitter_DDP= st.text_input("Jitter:DDP-mesr5 of var in fund. freq.")
    with col4:
        MDVP_Shimmer= st.text_input("MDVP_Shimmer-mesr1 of var in amp")
    with col5:
        MDVP_Shimmer_dB= st.text_input("MDVP_Shimmer_dB-mesr2 of var in amp")
    with col1:
        Shimmer_APQ3= st.text_input("slopeShimmer_APQ3-mesr3 of var in amp")
    with col2:
        Shimmer_APQ5= st.text_input("Shimmer:APQ5_mesr4 of var in amp")
    with col3:
        MDVP_APQ= st.text_input("MDVP:APQ_mesr6 of var in fund. freq.")
    with col4:
        Shimmer_DDA= st.text_input(" Shimmer:DDA-mesr5 of var in amp")
    with col5:
        NHR = st.text_input("NHR-mesur1 of the ratio of noise in voice")
    with col1:
        HNR = st.text_input("HNR- measure2 of the ratio of noise to tonal comp in the voice")
    with col2:
        RPDE= st.text_input("RPDE-nonlinear dynamic complex mesr1")
    with col3:
        DFA= st.text_input("DFA-nonlinear dynamic complex meas2")
    with col4:
        spread1= st.text_input("spread1-nonlinear mesr1 of fund. freq.var")
    with col5:
        spread2= st.text_input("spread2-nonlinear mesr2 of fund. freq.var")
    with col1:
        D2= st.text_input("nonlinear dynamic complex mesr2")
    with col2:
        PPE= st.text_input("nonlinear mesr3 of fund freq var")
        
    park_diagnosis=' '
    if st.button("Parkinson Disease Test result"):
        
        try:
        # Convert input features to numeric values
            features = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            features = [float(feature) for feature in features]

            # Prediction
            park_pred = parkinson_model.predict([features])

            # Update diagnosis based on prediction
            if park_pred == 1:
                park_diagnosis = "The person has Parkinson disease"
            else:
                park_diagnosis = "The person doesn't have Parkinson disease"

        except Exception as e:
            st.error(f"Error predicting diabetes: {e}")
            park_diagnosis = "Prediction error"

    st.success(park_diagnosis)
