# ✈️🧳 AI Travel Agent - Powered by LangGraph: A Practical Use Case 🌍
Welcome to the AI Travel Agent repository! This project demonstrates how to leverage LangGraph for building a smart travel assistant that uses multiple language models (LLMs) to handle tasks such as finding flights, booking hotels, and sending personalized emails. The agent is designed to interact with users, invoke necessary tools, and provide a seamless travel planning experience.

## **Features**

- **Stateful Interactions**: The agent remembers user interactions and continues from where it left off, ensuring a smooth user experience.
- **Human-in-the-Loop**: Users have control over critical actions, like reviewing travel plans before emails are sent.
- **Dynamic LLM Usage**: The agent intelligently switches between different LLMs for various tasks, like tool invocation and email generation.
- **Email Automation**: Automatically generates and sends detailed travel plans to users via email.

## Getting Started
Clone the repository, set up the virtual environment, and install the required packages

1. git clone git@github.com:nirbar1985/country-compass-ai.git

1. ( In case you have python version 3.11.9 installed in pyenv)
   ```shell script
   pyenv local 3.11.9
   ```

1. Install dependencies
    ```shell script
    poetry install --sync
    ```

1. Enter virtual env by:
    ```shell script
    poetry shell
    ```

## **Store Your API Keys**

1. Create a `.env` file in the root directory of the project.
2. Add your API keys and environment variables to the `.env` file:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    SERPAPI_API_KEY=your_serpapi_api_key
    SENDGRID_API_KEY=your_sendgrid_api_key

    # Observability variables
    LANGCHAIN_API_KEY=your_langchain_api_key
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_PROJECT=ai_travel_agent
    ```

Make sure to replace the placeholders (`your_openai_api_key`, `your_serpapi_api_key`, `your_langchain_api_key`, `your_sendgrid_api_key`) with your actual keys.
This version includes the necessary environment variables for OpenAI, SERPAPI, LangChain, and SendGrid and the LANGCHAIN_TRACING_V2 and LANGCHAIN_PROJECT configurations.

## Running the AI Travel Agent
### Kick of the chatbot by running:
```
streamlit run app.py
```

## License
Distributed under the MIT License. See LICENSE.txt for more information.
