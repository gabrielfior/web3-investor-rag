import os

import streamlit as st

from web3_investor_rag.dashboard.agent import AgentHandler


def build_report(openai_api_key: str | None) -> str:
    if not openai_api_key:
        st.error("OpenAI key not provided")
        return ""
    agent = AgentHandler(
        openai_api_key=openai_api_key, serper_api_key=os.environ["SERPER_API_KEY"]
    )
    agent.build_agent()
    report = agent.generate_markdown_report()
    st.session_state["report"] = report
