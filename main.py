import streamlit as st
import pandas as pd
from PIL import Image
import sqlite3
import time
import json
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide",page_title="Bizcard_EasyOCR",page_icon=Image.open('media/bizcard.jpg'))

st.sidebar.title("BUSINESS CARD..")
menu = ["Home", "Upload & View","Search",]
choice = st.sidebar.selectbox("Menu",menu)

def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

if choice == "Home":
    st.title("Biz_card Extraction using EasyOCR")
    col1,col2 = st.columns(2)
    with col1:
        lottie1 = load_lottiefile("media/biz.json")
        st_lottie(lottie1, height=500)
    with col2:
        st.subheader("Business card extraction is the process of digitizing the information on a physical business card and transferring it to a digital format."
                 " This allows the information to be easily stored, organized, and shared electronically."
                     "There are several methods for extracting information from a business card. One option is to manually enter the information into a digital contact management system, such as Microsoft Outlook or Google Contacts."
                     " However, this can be time-consuming and prone to errors.")
    col1,col2 = st.columns(2)
    with col1:
        st.title("**EASY_OCR**")
        st.subheader("Another option is to use a mobile app or software program specifically designed for business card extraction."
                     " These apps use optical character recognition (OCR) technology to scan the business card and extract the relevant information."
                     " Some apps also allow users to add notes, tags, or other details to the digital contact record.")
    with col2:
        lottie2 = load_lottiefile("media/ocr.json")
        st_lottie(lottie2, height=400)
    col1,col2 = st.columns(2)
    with col1:
        lottie3 = load_lottiefile("media/sql.json")
        st_lottie(lottie3, height=700)
    with col2:
        st.title("**SQLite**")
        st.subheader("Once the data has been formatted correctly, it can be inserted into the SQLite database using SQL commands such as INSERT or UPDATE."
                     " The specific syntax for these commands will depend on the structure of the database table and the format of the extracted data."
                     "Overall, updating OCR data into a SQLite database requires careful attention to detail and a solid understanding of SQL and database management principles."
                     " When done correctly, it can provide a powerful tool for managing and organizing contact information and other types of data.")

if choice == "Upload & View":
    # getting csv file from user
    file = st.file_uploader("Upload File", type=["csv", "xlsx", "xls"])
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Upload into Database"):
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)

            df = pd.read_csv(file)
            conn = sqlite3.connect('bizcard.db')
            df.to_sql('bizcard', conn, if_exists='replace', index=False)
            conn.close()
            st.success("Data Uploaded Successfully")
    with col2:
        if st.button("View csv file"):
            df = pd.read_csv(file)
            st.dataframe(df)

if choice == "Search":
    conn = sqlite3.connect('bizcard.db')
    df = pd.read_sql_query("SELECT * FROM bizcard", conn)

    st.title("Serach busiess card data from database")
    col1, col2 = st.columns(2)
    with col1:
        menu = ["","Name","Designation","Domain","District","State"]
        choice = st.selectbox("Search by",menu)
    with col2:
        if choice == "Name":
            st.subheader("Search by Name")
            name = st.text_input("Enter Name")
            df = pd.read_sql_query("select * from bizcard where name like '%"+name+"%'", conn)
            st.dataframe(df)
            if st.button("View details"):
                df_dict = df.to_dict("records")
                st.write("Name: ",df_dict[0]["Name"])
                st.write("Designation: ",df_dict[0]["Designation"])
                st.write("Domain: ",df_dict[0]["Domain"])
                st.write("Contact number: ",df_dict[0]["Contact"])
                st.write("E-mail: ",df_dict[0]["E-mail"])
                st.write("Website: ",df_dict[0]["Website"])
                st.write("Address: ",df_dict[0]["Address"])
                st.write("District: ",df_dict[0]["District"])
                st.write("State: ",df_dict[0]["State"])
                st.write("Pincode: ",df_dict[0]["Pincode"])
        if choice == "Designation":
            st.subheader("Search by Designation")
            designation = st.text_input("Enter Designation")
            df = pd.read_sql_query("select * from bizcard where designation like '%"+designation+"%'", conn)
            st.dataframe(df)
            if st.button("View details"):
                df_dict = df.to_dict("records")
                st.write("Name: ", df_dict[0]["Name"])
                st.write("Designation: ", df_dict[0]["Designation"])
                st.write("Domain: ", df_dict[0]["Domain"])
                st.write("Contact number: ", df_dict[0]["Contact"])
                st.write("E-mail: ", df_dict[0]["E-mail"])
                st.write("Website: ", df_dict[0]["Website"])
                st.write("Address: ", df_dict[0]["Address"])
                st.write("District: ", df_dict[0]["District"])
                st.write("State: ", df_dict[0]["State"])
                st.write("Pincode: ", df_dict[0]["Pincode"])
        if choice == "Domain":
            st.subheader("Search by Domain")
            domain = st.text_input("Enter Domain")
            df = pd.read_sql_query("select * from bizcard where domain like '%"+domain+"%'", conn)
            st.dataframe(df)
            if st.button("View details"):
                df_dict = df.to_dict("records")
                st.write("Name: ", df_dict[0]["Name"])
                st.write("Designation: ", df_dict[0]["Designation"])
                st.write("Domain: ", df_dict[0]["Domain"])
                st.write("Contact number: ", df_dict[0]["Contact"])
                st.write("E-mail: ", df_dict[0]["E-mail"])
                st.write("Website: ", df_dict[0]["Website"])
                st.write("Address: ", df_dict[0]["Address"])
                st.write("District: ", df_dict[0]["District"])
                st.write("State: ", df_dict[0]["State"])
                st.write("Pincode: ", df_dict[0]["Pincode"])
        if choice == "District":
            st.subheader("Search by District")
            district = st.text_input("Enter District")
            df = pd.read_sql_query("select * from bizcard where district like '%"+district+"%'", conn)
            st.dataframe(df)
            if st.button("View details"):
                df_dict = df.to_dict("records")
                st.write("Name: ", df_dict[0]["Name"])
                st.write("Designation: ", df_dict[0]["Designation"])
                st.write("Domain: ", df_dict[0]["Domain"])
                st.write("Contact number: ", df_dict[0]["Contact"])
                st.write("E-mail: ", df_dict[0]["E-mail"])
                st.write("Website: ", df_dict[0]["Website"])
                st.write("Address: ", df_dict[0]["Address"])
                st.write("District: ", df_dict[0]["District"])
                st.write("State: ", df_dict[0]["State"])
                st.write("Pincode: ", df_dict[0]["Pincode"])
        if choice == "State":
            st.subheader("Search by State")
            state = st.text_input("Enter State")
            df = pd.read_sql_query("select * from bizcard where state like '%"+state+"%'", conn)
            st.dataframe(df)
            if st.button("View details"):
                df_dict = df.to_dict("records")
                st.write("Name: ", df_dict[0]["Name"])
                st.write("Designation: ", df_dict[0]["Designation"])
                st.write("Domain: ", df_dict[0]["Domain"])
                st.write("Contact number: ", df_dict[0]["Contact"])
                st.write("E-mail: ", df_dict[0]["E-mail"])
                st.write("Website: ", df_dict[0]["Website"])
                st.write("Address: ", df_dict[0]["Address"])
                st.write("District: ", df_dict[0]["District"])
                st.write("State: ", df_dict[0]["State"])
                st.write("Pincode: ", df_dict[0]["Pincode"])















