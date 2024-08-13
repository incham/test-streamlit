import streamlit as st
from dotenv import load_dotenv
from llm import get_ai_response


st.set_page_config(page_title="소득세 챗봇")

st.title("소득세 챗봇")
# 환경 변수를 로드합니다.
load_dotenv()

# Initialize chat history
if "message_list" not in st.session_state:
    st.session_state.message_list = []

# Display chat messages from history on app rerun
for message_list in st.session_state.message_list:
    with st.chat_message(message_list["role"]):
        st.markdown(message_list["content"])



# Accept user input
if user_question := st.chat_input(placeholder='소득세에 관련된 질문을 적어주세요!'):
  # Display user message in chat message container
  with st.chat_message("user"):
    st.write(user_question)
  # Add user message to chat history
  st.session_state.message_list.append({"role": "user", "content": user_question})

  with st.spinner("답변을 생성하는 중입니다."):
    ai_message = get_ai_response(user_question)
    with st.chat_message("ai"):
      st.write_stream(ai_message)
    # Add user message to chat history
    st.session_state.message_list.append({"role": "ai", "content":ai_message})
