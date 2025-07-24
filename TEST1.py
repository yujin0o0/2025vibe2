import streamlit as st
import random

# ----------------------
# 귀엽고 깜찍한 배경 색 / 테마 스타일 지정
st.set_page_config(page_title="💖MBTI 공부 성향 분석기💖", page_icon="🎀", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #fff0f6;
    }
    .stApp {
        background: linear-gradient(145deg, #ffe4ec, #ffe8f0);
        color: #5c3d57;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------
# MBTI 학습 성향 데이터
mbti_data = {
    "INTJ": {
        "emoji": "🧠📈",
        "style": "전략적이고 조용한 환경에서 집중하는 걸 좋아해요.",
        "tip": "계획표를 짜고, 방해 없는 공간에서 혼자 공부해보세요! 🪄",
        "avoid": "시끌벅적한 조별과제 ❌",
        "keyword": "📊 논리적 / 🧍 혼자 / 📅 계획적"
    },
    "INFP": {
        "emoji": "🎨📖",
        "style": "감성 자극이 있어야 공부가 잘돼요!",
        "tip": "예쁜 노트나 감성 BGM과 함께하면 몰입도가 UP! 🌈",
        "avoid": "딱딱하고 틀에 박힌 공부 ❌",
        "keyword": "💭 감정 몰입 / 🌸 의미 중심 / ✏️ 창의적"
    },
    "ESTJ": {
        "emoji": "📋✅",
        "style": "계획 세우고 그대로 실천하는 걸 잘해요!",
        "tip": "To-Do 리스트와 타이머로 효율을 뽑아보세요. ⏰",
        "avoid": "즉흥적인 공부 ❌",
        "keyword": "📌 구조적 / 🧱 단단함 / 🛠 실용적"
    },
    "ENFP": {
        "emoji": "🔥🦄",
        "style": "에너지 넘치고, 다양하게 배우는 걸 좋아해요!",
        "tip": "친구랑 스터디하거나, 색깔 있는 마인드맵 활용! 🎨",
        "avoid": "지루한 반복문제 ❌",
        "keyword": "🌟 다채로움 / 💬 말하기 / 💡 아이디어"
    },
    # 더 추가 가능
}

# ----------------------
# 타이틀 영역
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>💖 나의 MBTI 공부 성향은? 💖</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>나를 더 잘 알고 ✨맞춤 전략✨으로 공부해보자! 🐣</h4>", unsafe_allow_html=True)
st.markdown("---")

# MBTI 선택
mbti_types = list(mbti_data.keys())
selected_mbti = st.selectbox("👇 내 MBTI를 골라볼까요?", mbti_types)

if selected_mbti:
    data = mbti_data[selected_mbti]
    st.markdown(f"### {data['emoji']} {selected_mbti}형의 공부 스타일은...")
    
    st.markdown(
        f"""
        <div style="background-color: #fff5fb; padding: 20px; border-radius: 20px; box-shadow: 2px 2px 10px #f3d1e0;">
            <p><strong>💡 공부 스타일:</strong><br>{data['style']}</p>
            <p><strong>🌟 추천 전략:</strong><br>{data['tip']}</p>
            <p><strong>🚫 비추천 환경:</strong><br>{data['avoid']}</p>
            <p><strong>🔑 키워드:</strong><br>{data['keyword']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()
    st.markdown("#### 🎀 오늘도 나답게, 즐겁게 공부해요! ✨")

# ----------------------
# 하단 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 13px;'>Made with 🐰 by ChatGPT | Powered by Streamlit 🎈</p>", unsafe_allow_html=True)
