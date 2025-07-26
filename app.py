import streamlit as st
import requests

st.title("AI Coding Assistance")

language = st.selectbox("Select Programming Language", ["Python", "JavaScript", "Java", "C++", "Ruby"])
topic = st.text_input("Enter Topic or Concept")
level = st.selectbox("Select Level of Detail", ["beginner", "intermediate", "advanced"])

def featch_response(endpoint, payload):
    try:
        response = requests.post(f"{API_URL}/{endpoint}", json=payload)
        responce_data = response.json()
        if "response" in responce_data:
            return responce_data["response"]
        else:
            st.error(f"Full backend response: {responce_data}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {str(e)}")
        return None
    

whatTodo = st.selectbox("What do you want to do?", ["Explain Code", "Generate Code", "Debug Code"])
st.subheader(whatTodo)

API_URL = "http://127.0.0.1:8000/"

code_to_debug = None
if whatTodo == "Debug Code":
    code_to_debug = st.text_area("Enter Code Snippet to Debug")

if st.button("Enter"):
    if whatTodo == "Explain Code":
        explanation = featch_response("explain", {
            "language": language,
            "topic": topic,
            "level": level
        })
        if explanation:
            st.subheader("Explanation:")
            st.write(explanation)
    elif whatTodo == "Generate Code":
        generated_code = featch_response("generate", {
            "language": language,
            "topic": topic,
            "level": level
        })
        if generated_code:
            st.subheader("Generated Code:")
            st.code(generated_code, language=language.lower())
    elif whatTodo == "Debug Code":
        if code_to_debug:
            debugged_code = featch_response("debug", {
                "language": language,
                "topic": code_to_debug
            })
            if debugged_code:
                st.subheader("Debugged Code:")
                st.code(debugged_code, language=language.lower())
        else:
            st.warning("Please enter code to debug.")
