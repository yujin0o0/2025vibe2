import streamlit as st
import random

st.set_page_config(page_title="🌟 이모지 퀴즈 게임", page_icon="🎨", layout="centered")

# 🎬 퀴즈 데이터
quiz_data = [
    {"emoji": "🦁👑", "answer": "라이언킹"},
    {"emoji": "🧑‍🚀🌕", "answer": "아폴로 11"},
    {"emoji": "❄️⛄️", "answer": "겨울왕국"},
    {"emoji": "🧙‍♂️🪄⚡", "answer": "해리포터"},
    {"emoji": "🐟🔍", "answer": "니모를 찾아서"},
    {"emoji": "🚢🧊💔", "answer": "타이타닉"},
    {"emoji": "🎤🕺", "answer": "보헤미안 랩소디"},
    {"emoji": "🎭🤡", "answer": "조커"},
    {"emoji": "🧑‍🔬👨‍👩‍👧‍👦🧬", "answer": "기생충"},
]

# 🎈 상태 초기화
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = random.randint(0, len(quiz_data) - 1)
    st.session_state.input = ""
    st.session_state.result = None

quiz = quiz_data[st.session_state.quiz_index]

# 🎀 제목
st.markdown("""
    <h1 style='text-align:center; color:#ff6ec7; font-size:60px; text-shadow: 2px 2px #ffb3ec;'>🌟 이모지 퀴즈 🌟</h1>
    <h4 style='text-align:center; color:#9f5fdf;'>이 이모지가 의미하는 영화/노래/인물을 맞혀보세요! 💡</h4>
""", unsafe_allow_html=True)

# 🧩 이모지 문제
st.markdown(f"<div style='font-size:80px; text-align:center;'>{quiz['emoji']}</div>", unsafe_allow_html=True)

# 🎯 정답 입력
user_input = st.text_input("정답을 입력하세요 ✨", value=st.session_state.input)

# 🎁 제출 버튼
if st.button("💖 제출하기"):
    st.session_state.input = user_input
    if user_input.strip().lower() == quiz["answer"].lower():
        st.session_state.result = "correct"
    else:
        st.session_state.result = "wrong"

# 🎉 결과 표시
if st.session_state.result == "correct":
    st.success("🌈 정답이에요! 멋져요! 🎉")
    st.markdown("<div style='font-size:40px; text-align:center;'>🎆✨🎇💖🌟✨🎉</div>", unsafe_allow_html=True)
elif st.session_state.result == "wrong":
    st.error("😭 오답이에요! 다시 시도해보세요!")
    st.markdown("<div style='font-size:30px; text-align:center;'>💧💧💧</div>", unsafe_allow_html=True)

# 🔁 다음 문제 버튼
if st.session_state.result:
    next_q = st.button("🔮 다음 문제로!")

    if next_q:
        st.session_state.quiz_index = random.randint(0, len(quiz_data) - 1)
        st.session_state.input = ""
        st.session_state.result = None
        st.experimental_rerun()

# 🦄 CSS 꾸미기
st.markdown("""
<style>
    .stTextInput > div > div > input {
        font-size: 20px;
        padding: 0.75em;
        border-radius: 10px;
        border: 2px solid #ff6ec7;
        background-color: #fff0f9;
    }

    .stButton > button {
        font-size: 18px;
        background-color: #ff6ec7;
        color: white;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        transition: 0.3s ease;
        border: none;
    }

    .stButton > button:hover {
        background-color: #ff94da;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)
