
# pylint: disable = invalid-name
import os
import uuid

import streamlit as st
from langchain_core.messages import HumanMessage

from agents.agent import Agent


def populate_envs(sender_email, receiver_email, subject):
    os.environ['FROM_EMAIL'] = sender_email
    os.environ['TO_EMAIL'] = receiver_email
    os.environ['EMAIL_SUBJECT'] = subject


def send_email(sender_email, receiver_email, subject, thread_id):
    try:
        populate_envs(sender_email, receiver_email, subject)
        config = {'configurable': {'thread_id': thread_id}}
        st.session_state.agent.graph.invoke(None, config=config)
        st.success('Email sent successfully!')
        # Clear session state
        for key in ['travel_info', 'thread_id']:
            if key in st.session_state:
                del st.session_state[key]
    except Exception as e:
        st.error(f'Error sending email: {e}')


if 'agent' not in st.session_state:
    st.session_state.agent = Agent()

# Custom CSS for styling
st.markdown(
    '''
    <style>
    .main-title {
        font-size: 2.5em;
        color: #333;
        text-align: center;
        margin-bottom: 0.5em;
        font-weight: bold;
    }
    .sub-title {
        font-size: 1.2em;
        color: #333;
        text-align: left;
        margin-bottom: 0.5em;
    }
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }
    .query-box {
        width: 80%;
        max-width: 600px;
        margin-top: 0.5em;
        margin-bottom: 1em;
    }
    .query-container {
        width: 80%;
        max-width: 600px;
        margin: 0 auto;
    }
    </style>
    ''', unsafe_allow_html=True)

# Streamlit UI
st.markdown('<div class="center-container">', unsafe_allow_html=True)
st.markdown('<div class="main-title">✈️🌍 AI Travel Agent 🏨🗺️</div>', unsafe_allow_html=True)

# Subtitle and query input box container
st.markdown('<div class="query-container">', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Enter your travel query and get flight and hotel information:</div>', unsafe_allow_html=True)
user_input = st.text_area(
    'Travel Query',
    height=200,
    key='query',
    placeholder='Type your travel query here...',
)
st.markdown('</div>', unsafe_allow_html=True)

# Button to process the query
if st.button('Get Travel Information'):
    if user_input:
        try:

            # Create a new thread ID
            thread_id = str(uuid.uuid4())
            st.session_state.thread_id = thread_id

            # Create a message from the user input
            messages = [HumanMessage(content=user_input)]
            config = {'configurable': {'thread_id': thread_id}}

            # Invoke the agent
            result = st.session_state.agent.graph.invoke({'messages': messages}, config=config)

            # Display the result
            st.subheader('Travel Information')
            st.write(result['messages'][-1].content)

            # Store the result in session state for later use
            st.session_state.travel_info = result['messages'][-1].content

        except Exception as e:
            st.error(f'Error: {e}')
    else:
        st.error('Please enter a travel query.')

# Check if travel information is available in session state
if 'travel_info' in st.session_state:
    send_email_option = st.radio('Do you want to send this information via email?', ('No', 'Yes'))
    if send_email_option == 'Yes':
        with st.form(key='email_form'):
            sender_email = st.text_input('Sender Email')
            receiver_email = st.text_input('Receiver Email')
            subject = st.text_input('Email Subject', 'Travel Information')
            body = st.session_state.travel_info
            submit_button = st.form_submit_button(label='Send Email')

        if submit_button:
            if sender_email and receiver_email and subject:
                send_email(sender_email, receiver_email, subject, st.session_state.thread_id)
            else:
                st.error('Please fill out all email fields.')

st.markdown('</div>', unsafe_allow_html=True)

# Add an image from a local file
st.sidebar.image('/Users/Nir.Bar/Documents/demos/genai/langgraph/reflection-agent/images/ai-travel.png', caption='AI Travel Assistant')
