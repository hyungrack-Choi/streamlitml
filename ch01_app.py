# _*_ coding:utf-8 _*_

import streamlit as st

def main():

    st.title('hello world')

    st.header('This is header')

    st.subheader('this is sub header')

    st.markdown('# this is heading1')
    st.markdown('## this is heading1')
    st.markdown('### this is heading1')

    st.success("성공")
    st.warning("경고")
    st.info("정보")
    st.error("에러")
    st.exception("예외처리")

    st.write("텍스트")
    st.write(2)
    st.write(2+5)
    st.write(dir(str))
    

if __name__ == "__main__":
    main()