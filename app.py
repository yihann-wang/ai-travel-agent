# pylint: disable = invalid-name
import os
import uuid
from collections import defaultdict

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

from agents.agent import Agent


def initialize_agent_and_session():
    if 'agent' not in st.session_state:
        st.session_state.agent = Agent()
    if 'thread_id' not in st.session_state:
        st.session_state.thread_id = str(uuid.uuid4())
    if 'messages' not in st.session_state:
        st.session_state.messages = []


def render_custom_css():
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 2.5em;
            color: #333;
            text-align: center;
            margin-bottom: 1em;
            font-weight: bold;
        }
        .stChatMessage {
            text-align: left;
        }
        .st-emotion-cache-janbn0 {
            flex-direction: row-reverse;
            text-align: right;
        }
        </style>
        """, unsafe_allow_html=True)


def display_messages():
    for msg in st.session_state.messages:
        st.chat_message(msg.type).write(msg.content)


def process_and_display_response(user_input):
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.chat_message('human').write(user_input)

    config = {'configurable': {'thread_id': st.session_state.thread_id}}
    response = st.session_state.agent.graph.invoke({'messages': [HumanMessage(content=user_input)]}, config=config)
    
    # Assuming the response contains the message content directly
    # You might need to adjust this based on the actual structure of the response
    msg_content = response['messages'][-1].content
    
    st.session_state.messages.append(AIMessage(content=msg_content))
    st.chat_message('ai').write(msg_content)


def main():
    st.sidebar.image('images/ai-travel.png', caption='AI Travel Assistant')
    st.markdown('<div class="main-title">✈️🌍 AI Travel Agent 🏨🗺️</div>', unsafe_allow_html=True)
    
    initialize_agent_and_session()
    render_custom_css()
    display_messages()

    if prompt := st.chat_input():
        process_and_display_response(prompt)


if __name__ == '__main__':
    main()