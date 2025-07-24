import streamlit as st
import random
import time

st.set_page_config(page_title="🎬 Emoji Movie Quiz!", page_icon="🍿", layout="centered")

# --------------------
# 🎨 CSS for sparkles & animation
st.markdown("""
    <style>
        .emoji-box {
            font-size: 80px;
            text-align: center;
            animation: pulse 2s infinite;
        }

        .correct {
            color: #00FFAA;
            font-size: 60px;
            animation: pop 0.7s ease-in-out;
        }

        .wrong {
            color: #FF6666;
            font-size: 40px;
            animation: shake 0.4s ease-in-out;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        @keyframes pop {
            0% { transform: scale(0.5); opacity: 0.2; }
            50% { transform: scale(1.2); opacity: 1; }
            100% { transform: scale(1); }
        }

        @keyframes shake {
            0% { transform: translateX(0); }
            25% { transform: translateX(-8px); }
            50% { transform: translateX(8px); }
            75% { transform: translateX(-4px); }
            100% { transform: translateX(0); }
        }

        .stTextInput>div>div>input {
            font-size: 24px;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------
# 🎥 Quiz Data
quiz_data = [
    {"emoji": "🦁👑", "answer": "라이언 킹"},
    {"emoji": "🧑‍🚀🌕", "answer": "인터스텔라"},
    {"emoji": "🧙‍♂️💍", "answer": "반지의 제왕"},
    {"emoji": "❄️👭", "answer": "겨울왕국"},
    {"emoji": "🐟🔍", "answer": "니모를 찾아서"},
    {"emoji": "🧑🏻🕷️", "answer": "스파이더맨"},
    {"emoji": "🤖🚗", "answer": "트랜스포머"},
    {"emoji": "🧑🏻⚡", "answer": "해리포터"},
    {"emoji": "👸🍎", "answer": "백설공주"},
    {"emoji": "🐉👦", "answer": "드래곤 길들이기"},
]

st.markdown("<h1 style='text-align:center;'>🍿 이모지 퀴즈: 무슨 영화일까요?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:20px;'>이모지를 보고 떠오르는 영화를 맞혀보세요!</p>", unsafe_allow_html=True)

# --------------------
# 🔁 상태 관리
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = random.randint(0, len(quiz_data) - 1)
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "last_correct" not in st.session_state:
    st.session_state.last_correct = None

# 현재 문제
current = quiz_data[st.session_state.quiz_index]

st.markdown(f"<div class='emoji-box'>{current['emoji']}</div>", unsafe_allow_html=True)

# 입력 & 제출
answer = st.text_input("🎯 정답은?", key="input_answer")

if st.button("✅ 제출하기"):
    if answer.strip().lower() == current["answer"].lower():
        st.session_state.show_result = True
        st.session_state.last_correct = True
        st.session_state.score += 1
    else:
        st.session_state.show_result = True
        st.session_state.last_correct = False

# --------------------
# 🎉 정답 피드백
if st.session_state.show_result:
    if st.session_state.last_correct:
        st.markdown("<p class='correct'>🎉 정답입니다! 풍선 퐁퐁~</p>", unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown("<p class='wrong'>😭 땡! 정답은 <b>{}</b>입니다!</p>".format(current["answer"]), unsafe_allow_html=True)

    time.sleep(1.5)
    st.session_state.quiz_index = random.randint(0, len(quiz_data) - 1)
    st.session_state.show_result = False
    st.experimental_rerun()  # 지금은 여긴 괜찮음. 그래도 필요하면 제거 가능

# --------------------
# 점수
st.markdown(f"<hr><h3 style='text-align:center;'>✨ 현재 점수: {st.session_state.score} 점 ✨</h3>", unsafe_allow_html=True)
