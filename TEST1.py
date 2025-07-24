import streamlit as st
import random

# 다양한 풍선 이모지 효과
balloon_effects = ["🎈", "🎉", "💫", "✨", "🎊", "🪩", "🌈", "🌟"]

# 전체 MBTI 16유형 데이터
mbti_data = {
    "INTJ": {"emoji": "🧠📈", "style": "전략적이고 혼자 집중하는 학습을 선호해요.",
             "tip": "장기 목표를 세우고, 조용한 공간에서 계획적으로 공부해요!",
             "avoid": "즉흥적이고 무계획한 공부 ❌",
             "keyword": "📊 계획적 / 🧍 독립형 / 🎯 목표 지향",
             "music": ["🎧 Hans Zimmer - Time", "🎧 Lofi Beats for Deep Focus", "🎧 Bach - The Well-Tempered Clavier"]},
    "INTP": {"emoji": "🧪🔍", "style": "개념 탐구와 깊이 있는 이해를 추구해요.",
             "tip": "왜?라는 질문으로 지식을 연결해가며 공부해보세요!",
             "avoid": "얕은 암기식 공부 ❌",
             "keyword": "🧠 분석적 / ❓ 호기심 / ⚗️ 논리적",
             "music": ["🎧 Ludovico Einaudi - Nuvole Bianche", "🎧 White Noise", "🎧 Deep Focus Spotify"]},
    "ENTJ": {"emoji": "📣📊", "style": "효율과 성과 중심으로 학습해요.",
             "tip": "목표를 세우고 데드라인 기반으로 밀도 있게 공부해요!",
             "avoid": "비체계적인 학습 ❌",
             "keyword": "🚀 실행력 / 📈 전략형 / 🗂 조직적",
             "music": ["🎧 Motivational Epic Music", "🎧 Power Beats", "🎧 Alan Walker - Spectre"]},
    "ENTP": {"emoji": "💡🎙️", "style": "아이디어와 토론을 통한 학습을 선호해요.",
             "tip": "친구와 말하면서 개념을 정리해보세요!",
             "avoid": "지루하고 반복적인 학습 ❌",
             "keyword": "🌪️ 즉흥적 / 💬 말하기 / 🌈 창의적",
             "music": ["🎧 Childish Gambino - Redbone", "🎧 Bazzi - Paradise", "🎧 Pop Energetic Playlist"]},
    "INFJ": {"emoji": "🌙📚", "style": "깊이 있는 의미와 목표를 찾는 공부를 해요.",
             "tip": "마인드맵과 다이어리형 노트로 정리해보세요!",
             "avoid": "가벼운 잡담식 학습 ❌",
             "keyword": "🔮 몰입형 / ✨ 직관적 / 🧘 차분함",
             "music": ["🎧 Piano for Meditation", "🎧 Cinematic Calm", "🎧 Aurora - Runaway"]},
    "INFP": {"emoji": "🎨📖", "style": "감정이입과 상상력 중심의 학습을 좋아해요.",
             "tip": "감성적인 자료나 영상과 함께하면 좋아요!",
             "avoid": "틀에 박힌 공부 방식 ❌",
             "keyword": "🌸 감성 몰입 / ✏️ 창의력 / 💭 상상력",
             "music": ["🎧 IU - Love Poem", "🎧 Billie Eilish - Ocean Eyes", "🎧 Rainy Mood + Jazz"]},
    "ENFJ": {"emoji": "🎤💞", "style": "사람들과 함께하며 배우는 것을 좋아해요.",
             "tip": "스터디 그룹에서 설명하면서 공부해보세요!",
             "avoid": "고립된 환경 ❌",
             "keyword": "🤝 공감형 / 📚 설명형 / 🎯 지도력",
             "music": ["🎧 Troye Sivan - Youth", "🎧 Feel-Good Indie", "🎧 Acoustic Pop Chill"]},
    "ENFP": {"emoji": "🔥🦄", "style": "다양하고 흥미로운 방식으로 배워요.",
             "tip": "컬러풀한 노트와 이야기식 학습이 잘 맞아요!",
             "avoid": "지루한 반복 문제 ❌",
             "keyword": "🌟 창의력 / 💬 외향적 / 🎨 다양성",
             "music": ["🎧 IU - Palette", "🎧 Red Velvet - Feel My Rhythm", "🎧 Upbeat Study Vibes"]},
    "ISTJ": {"emoji": "📘📐", "style": "정해진 틀과 규칙에 따라 차분히 공부해요.",
             "tip": "체크리스트와 일정표를 활용해보세요!",
             "avoid": "즉흥적인 환경 ❌",
             "keyword": "🧱 규칙적 / 🗂 정확함 / 📅 루틴",
             "music": ["🎧 Classic Study Focus", "🎧 Mozart Effect", "🎧 Tchaikovsky - Swan Lake"]},
    "ISFJ": {"emoji": "🧸📎", "style": "조용하고 안정된 환경에서 집중해요.",
             "tip": "복습과 정리 위주의 학습이 잘 맞아요!",
             "avoid": "변화 많은 환경 ❌",
             "keyword": "🎀 책임감 / 🪄 성실 / 🛏️ 안정감",
             "music": ["🎧 윤하 - 사건의 지평선", "🎧 Day6 - You Were Beautiful", "🎧 Gentle Piano Music"]},
    "ESTJ": {"emoji": "📋✅", "style": "실용적이고 계획적인 학습을 선호해요.",
             "tip": "To-Do 리스트와 타이머로 학습을 관리해보세요!",
             "avoid": "비효율적인 환경 ❌",
             "keyword": "📌 체계적 / 🔧 실용적 / 💼 실행력",
             "music": ["🎧 Corporate Focus Beats", "🎧 Daft Punk - Harder Better", "🎧 Synthwave Drive"]},
    "ESFJ": {"emoji": "💁📒", "style": "다른 사람과 소통하며 배우는 걸 좋아해요.",
             "tip": "서로 가르치며 공부하는 방식이 효과적이에요!",
             "avoid": "혼자 오랜 시간 공부 ❌",
             "keyword": "🌼 협동 / 📣 대화형 / ✨ 배려",
             "music": ["🎧 K-pop Study Playlist", "🎧 Taylor Swift - Enchanted", "🎧 Chillhop Essentials"]},
    "ISTP": {"emoji": "🔧🧩", "style": "직접 해보며 체험하는 학습이 잘 맞아요.",
             "tip": "실습 기반 문제풀이 위주로 공부해보세요!",
             "avoid": "이론만 나열된 강의 ❌",
             "keyword": "🎮 실용형 / 🛠️ 도전형 / 📦 분석력",
             "music": ["🎧 Game OST Focus", "🎧 Synthwave Coding", "🎧 Lo-fi for Builders"]},
    "ISFP": {"emoji": "🍃🎵", "style": "감성적인 분위기에서 차분히 공부해요.",
             "tip": "감성 음악과 함께 예쁜 노트로 정리해보세요!",
             "avoid": "딱딱하고 경직된 환경 ❌",
             "keyword": "🌷 감성형 / 🎧 분위기 중시 / 📓 시각형",
             "music": ["🎧 Studio Ghibli Piano", "🎧 Acoustic Rain", "🎧 Lofi + Nature"]},
    "ESTP": {"emoji": "🏃💥", "style": "활동적이고 즉각적인 피드백이 좋아요.",
             "tip": "게임처럼 목표를 설정하고 도전해보세요!",
             "avoid": "지루한 반복학습 ❌",
             "keyword": "🎲 활동적 / 🚀 즉흥형 / 🏆 도전형",
             "music": ["🎧 Fast-paced Workout", "🎧 EDM Study Set", "🎧 Upbeat Coding Mix"]},
    "ESFP": {"emoji": "🎉🎬", "style": "즐겁고 생생한 콘텐츠로 학습해요.",
             "tip": "영상, 노래, 퀴즈 등 체험형 학습이 잘 맞아요!",
             "avoid": "지루하고 반복적인 암기 ❌",
             "keyword": "🌈 외향적 / 🎤 체험형 / 🎁 즉흥적",
             "music": ["🎧 High School Musical", "🎧 Fun Retro Mix", "🎧 Bright Mood Playlist"]}
}

# Streamlit 앱
st.set_page_config(page_title="MBTI 공부 성향 분석기", page_icon="🧠", layout="centered")
st.title("📚 MBTI 공부 성향 분석기")
st.markdown("당신의 MBTI에 따라 맞춤형 💡 공부 스타일과 🎧 음악을 추천해드려요!")

selected = st.selectbox("당신의 MBTI를 선택해 주세요 👇", list(mbti_data.keys()))

if selected:
    data = mbti_data[selected]

    st.markdown(f"## {data['emoji']} {selected}형 공부 성향")
    st.markdown(
        f"""
        <div style="background-color:#fff0f6; padding:20px; border-radius:15px; box-shadow: 2px 2px 8px #e2c4d5;">
            <p><strong>💡 학습 스타일:</strong> {data['style']}</p>
            <p><strong>🌟 공부 꿀팁:</strong> {data['tip']}</p>
            <p><strong>🚫 피해야 할 환경:</strong> {data['avoid']}</p>
            <p><strong>🔑 키워드:</strong> {data['keyword']}</p>
            <p><strong>🎵 추천 음악:</strong><br>{"<br>".join(data['music'])}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 랜덤 풍선 출력
    emoji = random.choice(balloon_effects)
    st.markdown(f"<h2 style='text-align:center;'>{emoji * random.randint(6, 10)}</h2>", unsafe_allow_html=True)
    st.markdown("### 오늘도 나답게, 즐겁게 공부해요! ✨🎀")

else:
    st.info("MBTI를 선택해 주세요.")
