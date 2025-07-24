import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="🌟 가위바위보 대전 🌟", layout="centered", page_icon="🎤")

# 캐릭터 설정
characters = {
    "🐰 토끼": {
        "intro": "💬 토끼: '히힛! 이겨버릴 거야~!'",
        "win": "💬 토끼: '이겼다! 당근 간식 받아야지! 🥕'",
        "lose": "💬 토끼: '에에에~ 다음엔 꼭 이긴다구!'",
        "tie": "💬 토끼: '우리 통했나봐~ 😳'"
    },
    "🐱 고양이": {
        "intro": "💬 고양이: '흥, 별 거 아니네. 한 판 붙자.'",
        "win": "💬 고양이: '봤냐? 내가 고양이계의 천재라고 😼'",
        "lose": "💬 고양이: '…기억해둬라. 다음엔 안 져.'",
        "tie": "💬 고양이: '우연의 일치군. 🐾'"
    },
    "🦄 유니콘": {
        "intro": "💬 유니콘: '반짝이는 마법으로 승리를~✨'",
        "win": "💬 유니콘: '승리는 언제나 찬란하게! 🌈'",
        "lose": "💬 유니콘: '오늘은 별이 흐렸던 날이군요... 🌙'",
        "tie": "💬 유니콘: '조화로운 무승부... 아름다워요 ✨'"
    },
    "🐉 드래곤": {
        "intro": "💬 드래곤: '감히 나에게 도전하는 자가 있느냐! 🐲'",
        "win": "💬 드래곤: '이것이 진정한 힘이다! 으하하하🔥'",
        "lose": "💬 드래곤: '…크윽… 다음엔 불태워주지…'",
        "tie": "💬 드래곤: '잠깐 숨 고르기지… 후후…'"
    }
}

themes = {
    "🌌 밤하늘": "#1e0034",
    "🌵 사막": "#fceec0",
    "🎤 아이돌 무대": "#ffe4f2",
    "🎀 핑크 천국": "#ffddee"
}

# 선택
character = st.selectbox("🎭 캐릭터를 고르세요!", list(characters.keys()))
theme = st.selectbox("🖼️ 무대를 고르세요!", list(themes.keys()))

# 배경색 커스터마이징 (페이지 전체는 제한적이라, 컨테이너처럼 느낌만 주기)
st.markdown(f"""
    <style>
    .custom-box {{
        background-color: {themes[theme]};
        padding: 30px;
        border-radius: 20px;
    }}
    h1 {{
        text-align: center;
        font-size: 50px;
        color: #ff66cc;
        animation: glow 1.5s infinite alternate;
    }}
    @keyframes glow {{
        from {{ text-shadow: 0 0 15px #ff66cc; }}
        to {{ text-shadow: 0 0 40px #ff33aa; }}
    }}
    .bubble {{
        background-color: #ffffffcc;
        border-radius: 15px;
        padding: 1em;
        margin: 1em 0;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        animation: pop 0.8s ease-in;
    }}
    @keyframes pop {{
        0% {{ transform: scale(0.5); opacity: 0; }}
        100% {{ transform: scale(1); opacity: 1; }}
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"<div class='custom-box'>", unsafe_allow_html=True)

# 제목 및 소개
st.markdown(f"# 🌟 가위바위보  🌟")
st.markdown(f"### 🎤 {character} 등장! — {characters[character]['intro']}")

# 유저 선택
emojis = {"가위": "✌️", "바위": "✊", "보": "🖐️"}
user_choice = st.radio("무엇을 낼까요?", ["가위", "바위", "보"], horizontal=True)

# 대결 버튼
game_start = st.button("✨ 쇼타임! 대결 GO! ✨")

if game_start:
    with st.spinner("🎶 귀요미 컴퓨터와 함께 전투 중..."):
        time.sleep(1.5)

    for i in ["3️⃣", "2️⃣", "1️⃣", "🎵"]:
        st.markdown(f"<h1>{i}</h1>", unsafe_allow_html=True)
        time.sleep(0.5)

    computer_choice = random.choice(["가위", "바위", "보"])

    st.markdown("---")
    st.markdown(f"### 👑 당신: {emojis[user_choice]} **{user_choice}**")
    st.markdown(f"### 🤖 상대: {emojis[computer_choice]} **{computer_choice}**")
    st.markdown("---")

    # 판정
    if user_choice == computer_choice:
        result = "😮 **무승부!** 같은 생각이라니 놀라워요!"
        line = characters[character]['tie']
        st.info(result)
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "🎉 **당신이 이겼어요!!** 관객들의 환호가 쏟아집니다!"
        line = characters[character]['win']
        st.success(result)
        st.balloons()
    else:
        result = "💥 **졌습니다...! 하지만 무대는 계속됩니다.**"
        line = characters[character]['lose']
        st.error(result)
        st.snow()

    # 캐릭터 대사 출력
    st.markdown(f"<div class='bubble'>{line}</div>", unsafe_allow_html=True)
    st.markdown("🔁 다시 도전해 보세요! 무대는 당신의 것 💖")

st.markdown("</div>", unsafe_allow_html=True)
