import streamlit as st
from streamlit_option_menu import option_menu

from aws import aws_s3

with st.sidebar:
    opcao = option_menu("StarLord", ["AWS S3", 'Settings'], 
        icons=['cloud', 'gear'], menu_icon="cast", default_index=1)
    
if opcao == "AWS S3":
    aws_s3()