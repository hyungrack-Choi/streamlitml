# -*- coding: utf-8 -*-

import streamlit as st

def main():    
    st.title('BMI 계산기')

    weight = st.number_input('몸무게를 입력해주세요. (kg)')

    h_format = st.radio('키 입력 단위 설정:', ('cm', 'm', 'feet'))

    if h_format =='cm':
        height = st.number_input('센티미터 입력')
        try:
            bmi_result = weight/((height / 100)**2)
        except:
            st.text('0또는 숫자 입력하지 마세요...!')
    else:
        pass
    
    if  (st.button('BMI 계산기')):
        st.text(bmi_result)
        if bmi_result >= 40:
            st.error('심각하게 병원 방문 요망')
        elif bmi_result > 20:
            st.success('정상임')
        else:
            st.warning('음식을 더 드세요')

if __name__ == "__main__":
    main()