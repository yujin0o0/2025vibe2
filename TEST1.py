import streamlit as st

st.set_page_config(page_title="💖MBTI 공부 성향 분석기💖", page_icon="🧠", layout="centered")

# 스타일 설정
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe0f0, #fff5fa);
        color: #4e3b47;
        font-family: "Comic Sans MS", cursive;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "emoji": "🧠📈",
        "style": "전략적이고 혼자 집중하는 학습을 선호해요.",
        "tip": "장기 목표를 세우고, 조용한 공간에서 계획적으로 공부해요!",
        "avoid": "즉흥적이고 무계획한 공부 ❌",
        "keyword": "📊 계획적 / 🧍 독립형 / 🎯 목표 지향"
    },
    "INTP": {
        "emoji": "🧪🔍",
        "style": "이론과 개념을 깊이 탐구하는 걸 좋아해요.",
        "tip": "왜?라는 질문을 하며 지식을 연결하며 학습하세요!",
        "avoid": "얕고 반복적인 암기 ❌",
        "keyword": "🧠 논리적 / ❓호기심 / ⚗️ 분석적"
    },
    "ENTJ": {
        "emoji": "📣📊",
        "style": "효율과 성과 중심으로 공부해요!",
        "tip": "목표 설정 후 데드라인 정해서 밀도 있게 공부해봐요!",
        "avoid": "비체계적이고 산만한 환경 ❌",
        "keyword": "🚀 리더형 / 🧩 전략적 / 📈 실행력"
    },
    "ENTP": {
        "emoji": "💡🎙️",
        "style": "토론과 아이디어를 통해 배워요!",
        "tip": "브레인스토밍이나 친구와 이야기하며 정리하는 게 좋아요.",
        "avoid": "지루한 반복 학습 ❌",
        "keyword": "🌪️ 즉흥적 / 💬 말하기 / 🌈 창의적"
    },
    "INFJ": {
        "emoji": "🌙📚",
        "style": "깊이 있는 의미와 목표가 있는 공부를 좋아해요.",
        "tip": "조용한 환경에서 마인드맵과 다이어리형 노트 추천!",
        "avoid": "가벼운 잡담 위주의 스터디 ❌",
        "keyword": "🔮 직관적 / ✨몰입형 / 🧘 차분함"
    },
    "INFP": {
        "emoji": "🎨📖",
        "style": "감정이입과 의미 중심 학습을 선호해요.",
        "tip": "예쁜 문구류, 감성적인 자료와 함께 공부하면 좋아요!",
        "avoid": "틀에 박힌 공식 위주 학습 ❌",
        "keyword": "🌸 감성 몰입 / ✏️ 창의력 / 💭 상상력"
    },
    "ENFJ": {
        "emoji": "🎤💞",
        "style": "타인과 협력하며 배우는 걸 좋아해요!",
        "tip": "스터디 그룹에서 설명하며 복습하는 게 효과적이에요!",
        "avoid": "혼자 오래 공부하는 환경 ❌",
        "keyword": "🤝 공감형 / 📚 설명력 / 🎯 목표지향"
    },
    "ENFP": {
        "emoji": "🔥🦄",
        "style": "흥미와 다양성이 있어야 집중이 잘돼요!",
        "tip": "다채로운 형식(영상, 그림 등)으로 학습하세요!",
        "avoid": "지루한 반복 문제 ❌",
        "keyword": "🌟 창의력 / 💬 외향적 / 🎨 다양성"
    },
    "ISTJ": {
        "emoji": "📘📐",
        "style": "정해진 틀 안에서 체계적으로 공부해요.",
        "tip": "노트를 정리하고 계획표를 지키면 성취감이 높아요!",
        "avoid": "계획 없는 즉흥 학습 ❌",
        "keyword": "🧱 규칙적 / 🗂 정확함 / 📅 루틴"
    },
    "ISFJ": {
        "emoji": "🧸📎",
        "style": "조용한 환경에서 성실하게 공부해요.",
        "tip": "반복 정리와 복습을 활용한 공부가 잘 맞아요!",
        "avoid": "갑작스러운 변화나 경쟁적 분위기 ❌",
        "keyword": "🎀 책임감 / 🪄 성실 / 🛏️ 안정감"
    },
    "ESTJ": {
        "emoji": "📋✅",
        "style": "실용적이고 계획적인 학습을 선호해요.",
        "tip": "To-Do 리스트와 타이머로 집중 시간을 관리해요!",
        "avoid": "비효율적이고 어수선한 환경 ❌",
        "keyword": "🔧 실용성 / 📈 체계 / 📊 리더십"
    },
    "ESFJ": {
        "emoji": "💁📒",
        "style": "다른 사람과 함께하면서 배우는 걸 좋아해요.",
        "tip": "스터디 모임에서 발표하거나 질문하는 학습이 효과적이에요!",
        "avoid": "고립된 학습 ❌",
        "keyword": "🌼 협동 / 📣 대화형 / ✨배려"
    },
    "ISTP": {
        "emoji": "🔧🧩",
        "style": "직접 해보면서 배우는 학습을 선호해요.",
        "tip": "실습, 문제풀이 중심으로 손으로 익히는 게 좋아요!",
        "avoid": "긴 강의, 이론만 가득한 공부 ❌",
        "keyword": "🎮 실용형 / 🛠️ 도전적 / 📦 분석력"
    },
    "ISFP": {
        "emoji": "🍃🎵",
        "style": "감성적이면서도 조용한 공간에서 공부를 잘해요.",
        "tip": "분위기 있는 음악과 함께 노트 정리를 해보세요.",
        "avoid": "복잡한 경쟁 구도 ❌",
        "keyword": "🌷 감성형 / 🎧 분위기 중시 / 📓 시각형"
    },
    "ESTP": {
        "emoji": "🏃💥",
        "style": "에너지 넘치고 실전형 학습을 좋아해요!",
        "tip": "게임식 문제풀이, 타이머 챌린지 같은 공부가 좋아요!",
        "avoid": "긴 이론 설명 ❌",
        "keyword": "🎲 활동적 / 🚀 즉흥형 / 🏆 도전형"
    },
    "ESFP": {
        "emoji": "🎉🎬",
        "style": "즐겁고 생동감 있는 환경에서 학습 효과가 높아요!",
        "tip": "영상 학습, 친구와 퀴즈식 학습 추천!",
        "avoid": "딱딱하고 정적인 환경 ❌",
        "keyword": "🌈 외향적 / 🎤 즉각 반응 / 🎁 체험형"
    }
}

# UI
st.markdown("<h1 style='text-align:center;'>📚 MBTI 공부 성향 분석기</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>MBTI별 공부 스타일을 알아보고 ✨나만의 전략✨을 세워보세요!</h4>", unsafe_allow_html=True)
st.markdown("---")

mbti_list = list(mbti_data.keys())
selected = st.selectbox("당신의 MBTI를 선택해보세요 👇", mbti_list)

if selected:
    data = mbti_data[selected]
    st.markdown(f"## {data['emoji']} {selected}형의 공부 스타일")
    st.markdown(
        f"""
        <div style="background-color:#fff0f6; padding:20px; border-radius:15px; box-shadow: 2px 2px 8px #e2c4d5;">
            <p><strong>💡 학습 스타일:</strong> {data['style']}</p>
            <p><strong>🌟 공부 꿀팁:</strong> {data['tip']}</p>
            <p><strong>🚫 피해야 할 환경:</strong> {data['avoid']}</p>
            <p><strong>🔑 키워드:</strong> {data['keyword']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()
    st.markdown("#### 🎀 나에게 딱 맞는 방식으로 공부하면 능률도 쑥쑥! ✨")

st.markdown("---")
st.caption("Made with 💕 by ChatGPT | Powered by Streamlit 🎈")
