import streamlit as st
import random

st.set_page_config(page_title="🎨 이모지 퀴즈!", page_icon="✨", layout="centered")

# -------------------- 퀴즈 데이터 --------------------
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

# -------------------- 초기 상태 --------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = random.choice(quiz_data)
    st.session_state.input = ""
    st.session_state.result = None

# -------------------- 제목 --------------------
st.markdown("""
    <h1 style='text-align:center; color:#ff69b4;'>✨ 이모지 퀴즈 게임 ✨</h1>
    <h4 style='text-align:center;'>이 이모지가 의미하는 영화/노래/인물을 맞혀보세요! 🎬🎶</h4>
""", unsafe_allow_html=True)

# -------------------- 이모지 퀴즈 --------------------
st.markdown(f"<div style='font-size:70px; text-align:center;'>{st.session_state.quiz['emoji']}</div>", unsafe_allow_html=True)

# -------------------- 사용자 입력 --------------------
user_input = st.text_input("👇 정답을 입력하세요:", value=st.session_state.input)

# -------------------- 제출 버튼 --------------------
if st.button("🎯 제출하기"):
    st.session_state.input = user_input
    correct = st.session_state.quiz['answer'].strip().lower()
    if user_input.strip().lower() == correct:
        st.session_state.result = "correct"
    else:
        st.session_state.result = "wrong"

# -------------------- 결과 출력 --------------------
if st.session_state.result == "correct":
    st.success("🎉 정답입니다! 멋져요! 🎉")
    st.markdown("<div style='font-size:40px; text-align:center;'>🌈✨💖🎊✨🌈</div>", unsafe_allow_html=True)
elif st.session_state.result == "wrong":
    st.error("😭 오답이에요! 다시 시도해보세요!")
    st.markdown("<div style='font-size:30px; text-align:center;'>💧💧💧</div>", unsafe_allow_html=True)

# -------------------- 다음 문제 --------------------
if st.session_state.result:
    if st.button("🔁 다음 문제"):
        st.session_state.quiz = random.choice(quiz_data)
        st.session_state.input = ""
        st.session_state.result = None
        st.experimental_rerun()

# -------------------- 스타일 --------------------
st.markdown("""
<style>
    .stTextInput > div > div > input {
        font-size: 20px;
        padding: 0.75em;
        border-radius: 10px;
    }
    .stButton > button {
        font-size: 18px;
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        padding: 0.5em 1.5em;
    }
</style>
""", unsafe_allow_html=True)
