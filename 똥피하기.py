import streamlit as st
import random
import time

st.set_page_config(page_title="💩 똥 피하기 게임", page_icon="💩", layout="centered")

# --- 초기화 ---
if "player_pos" not in st.session_state:
    st.session_state.player_pos = 1  # 가운데 (0:왼쪽, 1:가운데, 2:오른쪽)
if "poop_pos" not in st.session_state:
    st.session_state.poop_pos = random.randint(0, 2)
if "poop_stage" not in st.session_state:
    st.session_state.poop_stage = 0  # 똥 떨어지는 단계
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# --- 타이틀 ---
st.markdown("<h1 style='text-align: center;'>💩 똥 피하기 게임 💩</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>움직여서 떨어지는 똥을 피하세요! 😱</h4>", unsafe_allow_html=True)

# --- 점수 ---
st.markdown(f"<h3 style='text-align: center;'>점수: {st.session_state.score}</h3>", unsafe_allow_html=True)

# --- 게임 종료 ---
if st.session_state.game_over:
    st.markdown("<h2 style='text-align: center; color: red;'>💥 똥을 맞았어요! 게임 오버 💀</h2>", unsafe_allow_html=True)
    if st.button("🔄 다시 시작하기"):
        st.session_state.player_pos = 1
        st.session_state.poop_pos = random.randint(0, 2)
        st.session_state.poop_stage = 0
        st.session_state.score = 0
        st.session_state.game_over = False
    st.stop()

# --- 게임 보드 출력 ---
def render_board():
    columns = st.columns(3)
    for i in range(3):
        if st.session_state.poop_stage == 0:
            emoji = "🌥️"  # 구름 (초기)
        elif st.session_state.poop_stage == 1:
            emoji = "💩" if i == st.session_state.poop_pos else "⭐"
        elif st.session_state.poop_stage == 2:
            emoji = "💩" if i == st.session_state.poop_pos else "⭐"
        elif st.session_state.poop_stage == 3:
            # 충돌 체크
            if i == st.session_state.poop_pos and i == st.session_state.player_pos:
                emoji = "💥"  # 폭발
                st.session_state.game_over = True
            elif i == st.session_state.player_pos:
                emoji = "😊"
            elif i == st.session_state.poop_pos:
                emoji = "💩"
            else:
                emoji = "⭐"
        else:
            if i == st.session_state.player_pos:
                emoji = "😊"
            else:
                emoji = "⭐"
        columns[i].markdown(f"<h1 style='text-align: center;'>{emoji}</h1>", unsafe_allow_html=True)

# --- 조작 버튼 ---
def move_left():
    if st.session_state.player_pos > 0:
        st.session_state.player_pos -= 1

def move_right():
    if st.session_state.player_pos < 2:
        st.session_state.player_pos += 1

# --- 게임 흐름 처리 ---
render_board()

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.button("⬅️ 왼쪽", on_click=move_left)
with col3:
    st.button("오른쪽 ➡️", on_click=move_right)

# --- 똥 떨어지는 애니메이션 효과 ---
if st.session_state.poop_stage < 4:
    time.sleep(0.5)
    st.session_state.poop_stage += 1
    st.experimental_rerun()
else:
    # 똥이 다 떨어지고 충돌 없으면 다음 턴으로
    if not st.session_state.game_over:
        st.session_state.poop_pos = random.randint(0, 2)
        st.session_state.poop_stage = 0
        st.session_state.score += 1
        st.experimental_rerun()
