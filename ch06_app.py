# _*_ coding:utf-8 _*_

import streamlit as st

def main():
    fname = st.text_input('이름 입력')
    st.title(fname)

    msg = st.text_area('입력', height=100)
    st.write(msg)

    number = st.number_input('숫자입력')
    st.write(number)

    date = st.date_input('날짜')
    st.write(date)

    mytime = st.time_input('시간')
    st.write(mytime)

    color = st.color_picker('색상 선택')
    st.write(color)

if __name__ == "__main__":
    main()
