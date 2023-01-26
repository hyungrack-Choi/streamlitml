# _*_ coding:utf-8 _*_

import streamlit as st
import utils
import pandas as pd                 #데이터 가공
import matplotlib.pyplot as plt     #static 시각화
import seaborn as sns               #static 시각화
import plotly.express as px         #dynamic 시각화
import numpy as np

def run_eda_app():
    st.write('탐색적 자료 분석')
    
    with st.expander('데이터셋 정보'):
        st.markdown(utils.attrib_info)

    iris_df = pd.read_csv('data/iris.csv')
    #st.write(iris_df.head())

    submenu_lists = ['','기술통계량', '그래프']
    submenu = st.sidebar.selectbox('EDA 메뉴', submenu_lists)

    if submenu == '기술통계량':
        st.subheader('데이터 통계량을 배우자')
        st.dataframe(iris_df)

        with st.expander('Data Types'):
            result = pd.DataFrame(iris_df.dtypes).transpose()
            result.index = ['구분']
            st.dataframe(result)
        with st.expander('기술 통계량'):
            result = pd.DataFrame(iris_df.describe()).transpose()
            st.dataframe(result)
        with st.expander('타겟분포'):
            st.dataframe(iris_df['species'].value_counts())
            
        map_data = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon'])
        
        x = st.slider('x')  # 👈 this is a widget
        st.write(x, 'squared is', x * x)

        st.map(map_data)

    elif submenu == '그래프':
        st.subheader('시각화를 그리자')
        
        with st.expander('산점도'):
            fig1 = px.scatter(iris_df,
                               x = 'sepal_width',
                              y= 'sepal_length',
                              color = 'species',
                              size = 'petal_width',
                              hover_data=['petal_length'],
                              title='산점도')
            st.plotly_chart(fig1)

        col1, col2 = st.columns(2)
        with col1:
            with st.expander('박스플롯 with seaborn'):
                fig, ax = plt.subplots()
                sns.boxplot(iris_df, x = 'species', y = 'sepal_length', ax=ax)
                st.pyplot(fig)
        with col2:
            with st.expander('히스토그램'):

                fig, ax = plt.subplots()
                ax.hist(iris_df['sepal_length'], color = 'green')
                st.pyplot(fig)

        tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
        with tab1:
            
            species_lists = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
            select_species = st.selectbox('종을 선택하세요',species_lists)
            
            result = iris_df[iris_df['species'] == select_species]
            st.dataframe(result)

            fig1 = px.scatter(result,
                               x = 'sepal_width',
                              y= 'sepal_length',
                              size = 'petal_width',
                              hover_data=['petal_length'],
                              title='산점도')
            st.plotly_chart(fig1)

        with tab2:
            if st.checkbox('Show dataframe'):
                chart_data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c'])

                chart_data
                
            # Add a slider to the sidebar:
            add_slider = st.sidebar.slider(
                'Select a range of values',
                0.0, 100.0, (25.0, 75.0)
            )
                    
            left_column, right_column = st.columns(2)
            # You can use a column just like st.sidebar:
            left_column.button('Press me!')

            # Or even better, call Streamlit functions inside a "with" block:
            with right_column:
                chosen = st.radio(
                    'Sorting hat',
                    ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
                st.write(f"You are in {chosen} house!")
            pass
    else:
        pass