import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="💫 궁극의 가위바위보 💫", layout="centered", page_icon="🧚")

# 🎭 캐릭터와 🖼️ 배경 설정
characters = {
    "🐰 토끼": "귀엽고 민첩한 토끼!",
    "🐱 고양이": "영리한 고양이~",
    "🦄 유니콘": "신비한 힘의 유니콘!",
    "🐉 드래곤": "불을 뿜는 강력 드래곤🔥"
}
themes = {
    "🌌 밤하늘": "#0f0523",
    "🌵 사막": "#f4e2ae",
    "🎤 아이돌 무대": "#ffe4f2",
    "🎀 핑크 천국": "#ffe5ec"
}

# 유저 선택
character = st.selectbox("🎭 캐릭터를 선택하세요!", list(characters.keys()))
theme = st.selectbox("🖼️ 배경 테마를 골라주세요!", list(themes.keys()))

# 배경색 스타일 지정
st.markdown(
    f"""
    <style>
    .main {{
        background-color: {themes[theme]};
    }}
    h1 {{
        color: #ff1493;
        text-align: center;
        animation: glow 1.5s infinite alternate;
    }}
    @keyframes glow {{
        from {{ text-shadow: 0 0 10px #ff69b4; }}
        to {{ text-shadow: 0 0 30px #ff69b4; }}
    }}
    .rps-button > button {{
        font-size: 26px !important;
        padding: 0.7em 1em !important;
        background: linear-gradient(45deg, #ff69b4, #ffb6c1, #ff69b4);
        background-size: 300% 300%;
        color: white;
        border: none;
        border-radius: 15px;
        animation: shine 3s infinite linear;
    }}
    @keyframes shine {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 제목
st.markdown(f"# 🌟 궁극의 가위바위보 대결 🌟")
st.markdown(f"### 당신의 캐릭터: {character} — {characters[character]}")

# 가위바위보 선택
emojis = {"가위": "✌️", "바위": "✊", "보": "🖐️"}
user_choice = st.radio("🤔 무엇을 내시겠습니까?", ["가위", "바위", "보"], horizontal=True)

# 게임 시작 버튼
with st.container():
    game = st.button("💥 대결 시작 💥", key="fight")

# 게임 실행
if game:
    with st.spinner("상대방과 접속 중..."):
        time.sleep(1.5)

    for i in ["3️⃣", "2️⃣", "1️⃣", "🎯"]:
        st.markdown(f"<h1>{i}</h1>", unsafe_allow_html=True)
        time.sleep(0.6)

    computer_choice = random.choice(["가위", "바위", "보"])

    st.markdown("---")
    st.markdown(f"### 🧍‍♀️ 당신: {emojis[user_choice]} **{user_choice}**")
    st.markdown(f"### 🤖 컴퓨터: {emojis[computer_choice]} **{computer_choice}**")
    st.markdown("---")

    # 결과 판단
    if user_choice == computer_choice:
        result = "🌫️ **무승부!** 오늘은 평화롭군요!"
        st.info(result)
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "🎉 **당신의 승리!** 이건 전설이야!"
        st.success(result)
        st.markdown("🎇 승리의 불꽃놀이 발사!")
        st.balloons()
    else:
        result = "💥 **졌습니다...!** 다음엔 이길 거예요!"
        st.error(result)
        st.markdown("❄️ 패배의 눈보라가 몰아칩니다...")
        st.snow()

    st.markdown(f"<h2 style='text-align:center;'>{result}</h2>", unsafe_allow_html=True)
    st.markdown("🔁 다시 도전해보세요! 운명을 바꿀 수 있어요 ✨")

