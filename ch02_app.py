# _*_ coding:utf-8 _*_

import streamlit as st
import pandas as pd

def main():
    data = pd.read_csv('data/iris.csv')

    st.title('데이터확인')
    st.dataframe(data, 400, 200)

    st.title("Adding color")
    st.dataframe(data.style.highlight_max(axis=0))

    st.title("table")
    st.table(data.head())

    mycode = """
    def hello():
        print("hello world!!")
    end
    """
    st.code(mycode, language='python')

if __name__ == "__main__":
    main()