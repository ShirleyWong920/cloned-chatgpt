"""
author:ws
"""
import streamlit as st
from utils import createChain,getAIMessage

with st.sidebar:
    options = ["gpt-3.5-turbo","gpt-3.5-turbo-16k","gpt-3.5-turbo-1106"]
    md = st.radio("请输入你要使用的OpenAI模型",options)
    openai_api_key = st.text_input("请输入OpenAI密钥：",type = "password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

st.header("💬克隆ChatGPT")
renewchat = st.button("开启新对话")
if renewchat:
    if "chain" in st.session_state:
        st.session_state.pop("chain")
    if "messages" in st.session_state:
        st.session_state.pop("messages")
#human_message = st.chat_input()
#print(human_message)
if "chain" not in st.session_state:
    st.session_state["chain"] = createChain(openai_api_key)
    st.session_state["messages"] = [{"role":"ai","content":"你好，我是AI聊天助手，有什么需要我帮忙的么？"}]
#messages = st.container(height=500)
for m in st.session_state.messages:
    st.chat_message(m["role"]).write(m["content"])

human_message = st.chat_input("Say something")
if human_message :
    if not openai_api_key:
        st.info("请输入你的OpenAI API密钥")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": human_message})
    st.chat_message("human").write(f"{human_message}")
    with st.spinner("AI正在思考中，请稍等..."):
        ai_message = getAIMessage(human_message, st.session_state.chain)
        st.session_state["messages"].append({"role": "ai", "content": ai_message})
        st.chat_message("ai").write(f"{ai_message}")





