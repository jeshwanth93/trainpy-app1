import streamlit as st
import requests

st.title("🐍 TrainPy - Python AI Assistant")

# Directly using token (not recommended for production)
HF_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/jeshwanth93/TrainPy"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

user_input = st.text_input("You:")

if user_input:
    with st.spinner("TrainPy is thinking..."):
        output = query({"inputs": user_input})
        if isinstance(output, dict) and "error" in output:
            st.error(f"❌ Error: {output['error']}")
        else:
            st.write("🤖:", output)
