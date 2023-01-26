# _*_ coding:utf-8 _*_

import streamlit as st
import joblib
import os
import numpy as np
import utils

def run_ml_app():
    st.subheader('머신러닝 데모 페이지')

    with st.expander('데이터셋 정보'):
        st.markdown(utils.attrib_info)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('수치를 입력해주세요!')

        # 슬라이더
        sepal_Length = st.select_slider('Sepal Length', options=np.arange(1, 11))
        sepal_Width = st.select_slider('Sepal Width', options=np.arange(1, 11))
        Petal_Length = st.select_slider('Petal length', options=np.arange(1, 11))
        Petal_Width = st.select_slider('Petal Width', options=np.arange(1, 11))

        sample = [sepal_Length, sepal_Width, Petal_Length, Petal_Width]
        st.write(sample)

    with col2:
        st.subheader('모델 결과를 확인해주세요')

        input_preds = np.array(sample).reshape(1, -1)
        st.write(input_preds)
        model_file = './models/logis_iris_model_230126.pkl'
        loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
        
        
        #st.write(loaded_model)
        prediction = loaded_model.predict(input_preds)
        st.write(prediction)

        pred_prob = loaded_model.predict_proba(input_preds)
        st.write(pred_prob)

        if prediction == 0:
            st.success('Setosa 종입니다.')
            pred_proba_scores = {
                'Setosa 확률' : pred_prob[0][0] * 100,
                'ver 확률' : pred_prob[0][1] * 100,
                'Vir 확률' : pred_prob[0][2] * 100,
            }
            st.write(pred_proba_scores)
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/220px-Irissetosa1.jpg')
        
        elif prediction == 1:
            st.success("Versicolor 종입니다.")
            pred_proba_scores = {"Setosa 확률": pred_prob[0][0]*100, 
                                 "Versicolor 확률": pred_prob[0][1]*100, 
                                 "Virginica 확률": pred_prob[0][2]*100}
            st.write(pred_proba_scores)
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/220px-Blue_Flag%2C_Ottawa.jpg')
        
        elif prediction == 2:
            st.success("Virginica 종입니다.")
            pred_proba_scores = {"Setosa 확률": pred_prob[0][0]*100, 
                                 "Versicolor 확률": pred_prob[0][1]*100, 
                                 "Virginica 확률": pred_prob[0][2]*100}
            st.write(pred_proba_scores)
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/220px-Iris_virginica_2.jpg')
        else:
            st.warning("판별 불가")   











