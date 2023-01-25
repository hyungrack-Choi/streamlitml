# _*_ coding:utf-8 _*_

import streamlit as st

def main():
    name = 'evan'

    if st.button('submit'):
        st.write(f'name: {name.upper()}')

    status = st.radio('status', ('활성화', '비활성화'))

    if status == '활성화':
        st.success('활성화 상태')
    else:
        st.error('비활성화 상태')

    if st.checkbox('Show/Hide'):
         st.text('보여주세요')

    with st.expander('python'):
        st.text('hello python')
        st.text('hello python')
        st.text('hello python')
        st.text('hello python')

if __name__ == "__main__":
    main()

