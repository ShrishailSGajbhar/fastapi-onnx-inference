import json
import streamlit as st
import requests

def main():
    st.title("Sentiment Analysis demo")
    st.subheader("Built using FastAPI and Streamlit")

    with st.form("sentiment"):
        phrase = st.text_input(label="Enter your sentiment here: ")

        submitted = st.form_submit_button(label="Prediction")
    
    # check if form is submitted    
    if submitted:
        # payload
        payload = {"phrase": phrase}
        # make an API call
        response = requests.post("http://192.168.31.147:8001/predict", json=payload)

        if response.status_code==200:
            prediction = response.json()
            if prediction['sentiment']=="positive":
                st.success("The phrase is classified as positive.")
            else:
                st.success("The phrase is classified as negative.")
        else:
            st.error("Failed to get prediction. Please try again.")


if __name__=="__main__":
    main()