import streamlit as st

st.checkbox("チェックボックス")
st.button("ボタン")
st.selectbox("メニューリスト", ("選択肢1","選択肢2","選択肢3"))
st.multiselect("メニューリスト(複数選択可)", ("選択肢1","選択肢2","選択肢3"))
st.radio("ラジオボタン",("選択肢1","選択肢2","選択肢3"))
st.sidebar.text_input("文字入力欄")
st.sidebar.text_area("テキストエリア")