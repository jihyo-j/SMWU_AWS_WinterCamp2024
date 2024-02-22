import openai
import streamlit as st
from streamlit_chat import message
from streamlit_folium import folium_static
import requests
import pandas as pd
import random
import time
import numpy as np
from PIL import Image
import folium
import streamlit.components.v1 as components
from elasticsearch import Elasticsearch

st.image('elasooktic.png', width=150)
        

with st.sidebar:
    # App Gallery 메뉴
     choose = st.selectbox("Elasooktic Smart Farm", ["Fruit Searching", "ChatBot", "Fruit Recommendation", "DataFrame"],
                         index=0,
                         format_func=lambda x: f"✨ {x}" if x == "Fruit Searching" else f"🤖 {x}" if x == "ChatBot" else f"🍓 {x}" if x == "Fruit Recommendation" else f"👓 {x}")

if choose == "Fruit Searching":
        
        
    # Elasticsearch 호스트 및 포트 설정
        es = Elasticsearch(['포트'], http_auth=('ElasticId', 'ElasticPassword'))

    # Streamlit 애플리케이션 UI 구성
        st.title('새로운 신품종 검색🫧')
        st.write('----------------------------')
        search_query = st.text_input('원하는 과일을 입력하면 신품종을 추천해드립니다!')

    # Elasticsearch에 쿼리를 보내고 결과를 표시
        if st.button('검색'):
            res = es.search(index="new_variety", body={"query": {"match": {"type": search_query}}}, size=50)

            for hit in res['hits']['hits']:
            # 각 결과를 카드 형태로 표시
                st.markdown(f"## {hit['_source']['title']}", unsafe_allow_html=True)
                st.image(hit['_source']['img'], caption="이미지", use_column_width=True, width=20)
        
                # 기능과 종류 표시
                st.markdown(f"**기능:** {hit['_source']['fuction']}", unsafe_allow_html=True)
                st.markdown(f"**종류:** {hit['_source']['type']}", unsafe_allow_html=True)
        
                # 'see more' 버튼 추가
                with st.expander("View more details!"):
                    st.write(f"[Download about this fruit!!]({hit['_source']['url']})")
                st.write('----------------------------')
