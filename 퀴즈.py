import streamlit as st
import random
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="🎨 이모지 퀴즈!", page_icon="✨", layout="centered")

# -------------------- 데이터 --------------------
emoji_quiz = [
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

# -------------------- 초기 설정 --------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = random.choice(emoji_quiz)
    st.session_state.result = None
    st.session_state.input = ""

st.markdown("<h1 style='text-align:center; color:#ff66c4;'>🎨 이모지 퀴즈!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>이 이모지 조합이 나타내는 영화/노래/유명인을 맞혀보세요! 🎬🎶</h3>", unsafe_allow_html=True)

# -------------------- 퀴즈 표시 --------------------
st.markdown(f"<div style='font-size:60px; text-align:center;'>{st.session_state.quiz['emoji']}</div>", unsafe_allow_html=True)

# -------------------- 입력 --------------------
st.session_state.input = st.text_input("정답을 입력하세요! 😊", key="answer_input")

if st.button("제출하기 🎯"):
    user_answer = st.session_state.input.strip().lower()
    correct_answer = st.session_state.quiz["answer"].strip().lower()

    if user_answer == correct_answer:
        st.success("🎉 정답입니다! 멋져요!")
        rain(
            emoji="🎉",
            font_size=54,
            falling_speed=8,
            animation_length=3,
        )
    else:
        st.error("😭 오답이에요! 다시 시도해보세요!")
        rain(
            emoji="💧",
            font_size=30,
            falling_speed=10,
            animation_length=2,
        )

    # 다음 퀴즈로 갱신 버튼
    if st.button("🔄 다음 문제로!"):
        st.session_state.quiz = random.choice(emoji_quiz)
        st.session_state.input = ""
        st.rerun()

# -------------------- 꾸미기 --------------------
st.markdown(
    """
    <style>
        .stTextInput>div>div>input {
            font-size: 20px;
            padding: 10px;
        }
        .stButton>button {
            background-color: #ff66c4;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
