import streamlit as st
from agents.analyzer import analyze_contract
from utils.gantt import render_gantt

st.set_page_config(page_title="ShieldContract 2", layout="wide")
st.title("🛡️ ShieldContract 2: Freelance Contract Guardian")

uploaded = st.file_uploader("Upload your contract (PDF or TXT)", type=["pdf", "txt"])
if uploaded:
    if uploaded.type == "application/pdf":
        import fitz  # PyMuPDF
        doc = fitz.open(stream=uploaded.read(), filetype="pdf")
        text = "\n".join([page.get_text() for page in doc])
    else:
        text = uploaded.read().decode("utf-8", errors="ignore")

    st.subheader("📜 Contract Preview")
    st.text_area("Content", text, height=300)

    if st.button("🧠 Analyze Contract"):
        with st.spinner("Thinking..."):
            summary, tasks = analyze_contract(text)
            st.success("Contract analyzed.")

        st.subheader("🔍 Summary / Legal Flags")
        st.markdown(summary)

        st.subheader("📆 Project Timeline (Gantt)")
        render_gantt(tasks)
