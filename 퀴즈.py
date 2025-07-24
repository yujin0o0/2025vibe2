import streamlit as st
import random

st.set_page_config(page_title="🎬 Emoji Movie Quiz!", page_icon="🍿", layout="centered")
st.markdown("<p style='text-align:center; color:red;'>⚠️ 버튼은 가끔 한 번에 안 먹을 수 있어요!<br><b>‘제출하기’와 ‘다음 문제’ 버튼은 두 번씩 눌러주세요 💡</b></p>", unsafe_allow_html=True)
# --------------------
# 🎨 CSS for 화려한 애니메이션
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
# 퀴즈 데이터
quiz_data = [
    {"emoji": "🦁👑", "answer": "라이언 킹", "level": 1},
    {"emoji": "🧑‍🚀🌕", "answer": "인터스텔라", "level": 2},
    {"emoji": "🧙‍♂️💍", "answer": "반지의 제왕", "level": 2},
    {"emoji": "❄️👭", "answer": "겨울왕국", "level": 1},
    {"emoji": "🐟🔍", "answer": "니모를 찾아서", "level": 1},
    {"emoji": "🧑🏻🕷️", "answer": "스파이더맨", "level": 1},
    {"emoji": "🧑🏻⚡", "answer": "해리포터", "level": 1},
    {"emoji": "👸🍎", "answer": "백설공주", "level": 1},
    {"emoji": "🐉👦", "answer": "드래곤 길들이기", "level": 2},
    {"emoji": "🐼🥋", "answer": "쿵푸 팬더", "level": 1},
    {"emoji": "🎭🃏", "answer": "조커", "level": 2},
    {"emoji": "🧑‍🚀🤖🌍", "answer": "월E", "level": 1},
    {"emoji": "👽🚲🌕", "answer": "E.T.", "level": 2},
    {"emoji": "🍫👦🏭", "answer": "찰리와 초콜릿 공장", "level": 1},
    {"emoji": "💞💔🚢", "answer": "타이타닉", "level": 1},
    {"emoji": "🌪️🏠🧙‍♀️", "answer": "오즈의 마법사", "level": 3},
    {"emoji": "🧞‍♂️🕌", "answer": "알라딘", "level": 1},
    {"emoji": "🌊👸🐚", "answer": "인어공주", "level": 1},
    {"emoji": "🐸👑💋", "answer": "공주와 개구리", "level": 2},
    {"emoji": "🚗🏁", "answer": "카", "level": 1},
    {"emoji": "🌹⏰🕯️", "answer": "미녀와 야수", "level": 1},
    {"emoji": "🐘🎪", "answer": "덤보", "level": 1},
    {"emoji": "🎤👹🎵🐅🕺", "answer": "케이팝 데몬 헌터스", "level": 2},
]

# --------------------
# 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = random.randint(0, len(quiz_data)-1)
if "answered" not in st.session_state:
    st.session_state.answered = False
if "correct" not in st.session_state:
    st.session_state.correct = False

# --------------------
# UI 표시
st.markdown("<h1 style='text-align:center;'>🍿 이모지 퀴즈: 무슨 영화일까요?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:20px;'>이모지를 보고 떠오르는 영화를 맞혀보세요!</p>", unsafe_allow_html=True)

current = quiz_data[st.session_state.quiz_index]

st.markdown(f"<div class='emoji-box'>{current['emoji']}</div>", unsafe_allow_html=True)

# --------------------
# 정답 입력
if not st.session_state.answered:
    answer = st.text_input("🎯 정답은?", key="answer_input")
    if st.button("✅ 제출하기"):
        if answer.strip().lower() == current["answer"].lower():
            st.session_state.correct = True
            st.session_state.score += 1
        else:
            st.session_state.correct = False
        st.session_state.answered = True
        st.experimental_set_query_params(dummy=random.randint(0, 10000))  # 강제 refresh 없이 키값 변화 유도
        st.stop()

# --------------------
# 결과 표시
if st.session_state.answered:
    if st.session_state.correct:
        st.markdown("<p class='correct'>🎉 정답입니다! 풍선 퐁퐁~</p>", unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown(f"<p class='wrong'>😭 땡! 정답은 <b>{current['answer']}</b>입니다!</p>", unsafe_allow_html=True)

    if st.button("🔄 다음 문제"):
        st.session_state.quiz_index = random.randint(0, len(quiz_data)-1)
        st.session_state.answered = False
        st.session_state.correct = False
        st.experimental_set_query_params(refresh=random.randint(0, 10000))  # 강제 refresh 유도
        st.experimental_rerun()

# --------------------
# 점수
st.markdown(f"<hr><h3 style='text-align:center;'>✨ 현재 점수: {st.session_state.score} 점 ✨</h3>", unsafe_allow_html=True)
