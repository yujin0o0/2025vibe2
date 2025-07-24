import streamlit as st
import random
import time

# 🎨 페이지 꾸미기
st.set_page_config(page_title="화려한 가위바위보 게임✨", page_icon="✊", layout="centered")
st.markdown(
    """
    <style>
    .main {
        background-color: #ffe4f2;
    }
    h1 {
        color: #ff69b4;
        text-align: center;
        font-size: 48px;
    }
    .stButton>button {
        font-size: 24px;
        height: 3em;
        width: 100%;
        margin: 5px 0px;
        background-color: #ffb6c1;
        color: white;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎉 제목
st.markdown("## 🎀 화려하고 귀여운 가위바위보 게임 🎀")

# 🎈 이모티콘
emojis = {
    "가위": "✌️",
    "바위": "✊",
    "보": "🖐️"
}

user_choice = st.radio("무엇을 낼까요? 😎", ["가위", "바위", "보"], horizontal=True)

if st.button("대결 시작! 💥"):
    st.balloons()
    st.markdown("### 🤖 상대 선택 중...")
    time.sleep(1)

    computer_choice = random.choice(["가위", "바위", "보"])
    st.markdown(f"### 🧍‍♀️ 당신: {emojis[user_choice]} **{user_choice}**")
    st.markdown(f"### 🖥️ 컴퓨터: {emojis[computer_choice]} **{computer_choice}**")

    result = ""
    if user_choice == computer_choice:
        result = "😮 비겼어요!"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "🎉 이겼어요! 대단해요!"
        st.success(result)
    else:
        result = "😭 졌어요! 다음엔 꼭 이겨봐요!"
        st.error(result)

    st.markdown("---")
    st.markdown("### 🔁 다시 도전해보세요!")

