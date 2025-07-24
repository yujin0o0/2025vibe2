import streamlit as st
import random
import time

# 🧸 페이지 설정
st.set_page_config(page_title="화려한 가위바위보 ⚔️", page_icon="🎀", layout="centered")

# 🖌️ 스타일 커스터마이징
st.markdown("""
    <style>
    .main {
        background-color: #fff0f5;
    }
    h1 {
        font-size: 60px;
        color: #ff1493;
        text-align: center;
        animation: glow 1.5s infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #ff69b4; }
        to { text-shadow: 0 0 30px #ff69b4; }
    }
    .result {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
    }
    .rps-button button {
        font-size: 26px !important;
        height: 3em !important;
        width: 100% !important;
        margin: 8px 0px !important;
        background-color: #ffb6c1 !important;
        color: white !important;
        border-radius: 15px !important;
        border: 2px solid #ff69b4 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 🎀 제목
st.markdown("# 🌟 화려한 가위바위보 챌린지 🌟")
st.markdown("## 🧚‍♀️ 귀엽고 긴장감 넘치는 승부의 세계로!")

# 🎮 이모지 매핑
emojis = {
    "가위": "✌️",
    "바위": "✊",
    "보": "🖐️"
}

# 🌈 사용자 선택
with st.container():
    st.markdown("### 🤔 당신의 선택은?")
    user_choice = st.radio("가위✌️, 바위✊, 보🖐️ 중 하나를 골라주세요!", ["가위", "바위", "보"], horizontal=True)

# 🕹️ 게임 시작
if st.button("💥 대결 시작! 💥", type="primary"):
    with st.spinner("상대방을 찾는 중... 😈"):
        time.sleep(1.5)

    # 긴장감 주는 카운트다운
    for i in ["3️⃣", "2️⃣", "1️⃣", "🎯"]:
        st.markdown(f"<h1>{i}</h1>", unsafe_allow_html=True)
        time.sleep(0.6)

    # 컴퓨터 선택
    computer_choice = random.choice(["가위", "바위", "보"])

    # 🎭 결과 출력
    st.markdown("---")
    st.markdown(f"### 🙋‍♀️ 당신: {emojis[user_choice]} **{user_choice}**")
    st.markdown(f"### 🖥️ 컴퓨터: {emojis[computer_choice]} **{computer_choice}**")
    st.markdown("---")

    result = ""
    win = False

    if user_choice == computer_choice:
        result = "😮 **비겼어요!** 아슬아슬한 승부였네요!"
        st.info(result)
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "🎉 **이겼어요!!** 천재인가요? 🧠"
        st.balloons()
        st.success(result)
        win = True
    else:
        result = "💀 **졌어요...** 다음엔 이길 수 있을 거예요!"
        st.snow()
        st.error(result)

    # 🌟 결과 강조 텍스트
    st.markdown(f"<div class='result'>{result}</div>", unsafe_allow_html=True)

    # 🔊 음향 효과 링크 (직접 재생은 불가)
    if win:
        st.markdown("🔊 [🎵 축하 음악 듣기 (클릭!)](https://www.youtube.com/watch?v=ZbZSe6N_BXs)")
    else:
        st.markdown("🔊 [💔 패배 음악 듣기 (클릭!)](https://www.youtube.com/watch?v=2ZIpFytCSVc)")

    # 🔁 재도전 유도
    st.markdown("---")
    st.markdown("## 🔁 다시 한번 도전해보세요! 운명을 바꿔봐요!")

