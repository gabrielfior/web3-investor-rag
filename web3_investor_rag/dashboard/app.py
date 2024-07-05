import os

import dotenv

dotenv.load_dotenv()
import streamlit as st

from web3_investor_rag.dashboard.app_functions import build_report

st.title("Web3 Investor")

st.text_input(
    "OpenAI API key",
    key="openai_api_key",
    value=os.getenv("OPENAI_API_KEY"),
    type="password",
)

st.button(
    "generate report", on_click=build_report, args=[st.session_state.openai_api_key]
)

if "report" in st.session_state:
    st.markdown(st.session_state.report)
