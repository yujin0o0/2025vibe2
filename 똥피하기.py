import streamlit as st
import random
import time

st.set_page_config(page_title="💩 똥 피하기 게임", page_icon="💩", layout="centered")

# -------------------------
# 초기 상태 설정
# -------------------------
if "player_pos" not in st.session_state:
    st.session_state.player_pos = 1  # 가운데
if "poop_pos" not in st.session_state:
    st.session_state.poop_pos = random.randint(0, 2)
if "falling" not in st.session_state:
    st.session_state.falling = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# -------------------------
# UI 타이틀 및 설명
# -------------------------
st.markdown("<h1 style='text-align: center;'>💩 똥 피하기 게임 💩</h1>", unsafe_allow_html=True)
with st.expander("📘 게임 방법 보기", expanded=False):
    st.markdown("""
    - 캐릭터 😊는 왼쪽 / 가운데 / 오른쪽 중 하나에 위치합니다  
    - 위에서 💩가 떨어져요!  
    - 좌/우 버튼을 눌러 피하세요  
    - 💩와 부딪히면 게임 오버!  
    - 많이 피할수록 점수가 올라가요!
    """)

# -------------------------
# 점수 표시
# -------------------------
st.markdown(f"<h3 style='text-align: center;'>점수: {st.session_state.score}</h3>", unsafe_allow_html=True)

# -------------------------
# 게임 오버 처리
# -------------------------
if st.session_state.game_over:
    st.markdown("<h2 style='text-align: center; color: red;'>💥 똥을 맞았어요! 게임 오버 💀</h2>", unsafe_allow_html=True)
    if st.button("🔄 다시 시작하기"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
    st.stop()

# -------------------------
# 캐릭터 & 똥 출력 함수
# -------------------------
def render_game(poop_stage):
    cols = st.columns(3)
    for i in range(3):
        if poop_stage == 0:
            # 초기 상태 (구름)
            emoji = "🌥️" if i == st.session_state.poop_pos else "⭐"
        elif poop_stage == 1:
            # 중간 단계
            emoji = "💩" if i == st.session_state.poop_pos else "⭐"
        elif poop_stage == 2:
            # 마지막 충돌 여부
            if i == st.session_state.poop_pos and i == st.session_state.player_pos:
                emoji = "💥"
                st.session_state.game_over = True
            elif i == st.session_state.player_pos:
                emoji = "😊"
            elif i == st.session_state.poop_pos:
                emoji = "💩"
            else:
                emoji = "⭐"
        else:
            # 일반 상태 (캐릭터만 출력)
            emoji = "😊" if i == st.session_state.player_pos else "⭐"

        cols[i].markdown(f"<h1 style='text-align: center;'>{emoji}</h1>", unsafe_allow_html=True)

# -------------------------
# 좌우 이동 함수
# -------------------------
def move_left():
    if st.session_state.player_pos > 0:
        st.session_state.player_pos -= 1

def move_right():
    if st.session_state.player_pos < 2:
        st.session_state.player_pos += 1

# -------------------------
# 이동 버튼 UI
# -------------------------
col_left, col_center, col_right = st.columns([1, 1, 1])
with col_left:
    st.button("⬅️ 왼쪽", on_click=move_left)
with col_right:
    st.button("오른쪽 ➡️", on_click=move_right)

# -------------------------
# 똥 애니메이션 처리
# -------------------------
if not st.session_state.falling:
    # 떨어지기 시작
    st.session_state.falling = True
    for stage in range(3):
        render_game(stage)
        time.sleep(0.4)
        st.experimental_rerun()

# -------------------------
# 충돌이 없었다면 다음 턴으로
# -------------------------
if st.session_state.falling and not st.session_state.game_over:
    render_game(2)
    time.sleep(0.5)
    # 다음 턴 준비
    st.session_state.score += 1
    st.session_state.poop_pos = random.randint(0, 2)
    st.session_state.falling = False
    st.experimental_rerun()
