import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(
    page_title="🎬 영화 이모티콘 퀴즈 🍿",
    page_icon="🎬",
    layout="wide"
)

# 영화관 스타일 CSS 추가
st.markdown("""
<style>
    .main {
        background-color: #0d1117;
        color: white;
    }
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url('https://img.freepik.com/free-photo/cinema-elements-red-background-with-copy-space_23-2148457853.jpg');
        background-size: cover;
    }
    .title {
        color: #FFD700;
        text-align: center;
        font-size: 50px;
        text-shadow: 2px 2px 4px #000000;
    }
    .emoji-display {
        background-color: rgba(0,0,0,0.7);
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0px;
        border: 2px solid #FFD700;
    }
    .score-board {
        background-color: rgba(128, 0, 0, 0.7);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: white;
        border: 2px solid #FFD700;
    }
    .stButton>button {
        background-color: #FFD700;
        color: #000000;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: rgba(255,255,255,0.9);
        color: black;
        border: 2px solid #FFD700;
    }
    .category-header {
        background-color: rgba(139, 0, 0, 0.8);
        color: #FFD700;
        padding: 5px 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .movie-screen {
        background-color: rgba(0,0,0,0.8);
        border: 3px solid #8B0000;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
    }
    .popcorn {
        position: fixed;
        bottom: 20px;
        right: 20px;
        font-size: 40px;
        animation: bounce 2s infinite;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        background-color: #f00;
        animation: confetti 5s ease-in-out infinite;
    }
    @keyframes confetti {
        0% { transform: translateY(0) rotate(0deg); }
        100% { transform: translateY(100vh) rotate(720deg); }
    }
</style>
""", unsafe_allow_html=True)

# 영화 데이터 (이모티콘, 영화 제목, 힌트, 카테고리)
movies = [
    # 일반 인기 영화
    {"emoji": "👸❄️⛄", "title": "겨울왕국", "hint": "디즈니 애니메이션, 'Let It Go' 주제가로 유명해요", "category": "디즈니"},
    {"emoji": "🧙‍♂️💍🌋", "title": "반지의 제왕", "hint": "반지를 파괴하기 위한 대장정", "category": "판타지"},
    {"emoji": "🦁👑🌴", "title": "라이온 킹", "hint": "사자 왕자의 성장 이야기", "category": "디즈니"},
    {"emoji": "🚢❄️💔", "title": "타이타닉", "hint": "빙산과 충돌한 비극적 사랑 이야기", "category": "로맨스"},
    {"emoji": "👨‍🚀🌌👽", "title": "인터스텔라", "hint": "우주 여행과 시간의 상대성", "category": "SF"},
    {"emoji": "🧙‍♂️⚡👓", "title": "해리 포터", "hint": "마법 학교의 소년 마법사", "category": "판타지"},
    {"emoji": "🤖❤️🌱", "title": "월-E", "hint": "외로운 로봇의 사랑 이야기", "category": "픽사"},
    {"emoji": "🦖🦕🏝️", "title": "쥬라기 공원", "hint": "공룡들이 살아있는 테마파크", "category": "모험"},
    {"emoji": "🦇👨🃏", "title": "다크나이트", "hint": "배트맨과 조커의 대결", "category": "슈퍼히어로"},
    {"emoji": "🔍🐠🌊", "title": "니모를 찾아서", "hint": "아빠 물고기가 아들을 찾아 떠나는 여정", "category": "픽사"},
    
    # 케이팝 데몬 헌터스
    {"emoji": "👩‍🎤🎸👹⚔️", "title": "케이팝 데몬 헌터스", "hint": "K-pop 아이돌들이 악마 사냥꾼으로 활약하는 영화", "category": "K-콘텐츠"},
    {"emoji": "🎤👹🔪🇰🇷", "title": "케이팝 데몬 헌터스: 악의 부활", "hint": "악마 사냥꾼 아이돌의 두 번째 이야기", "category": "K-콘텐츠"},
    {"emoji": "👯‍♀️🔮👺🎵", "title": "케이팝 데몬 헌터스: 최후의 전투", "hint": "데몬 헌터스 시리즈의 완결편", "category": "K-콘텐츠"},
    
    # 디즈니 영화 추가
    {"emoji": "🧜‍♀️🐠🌊👑", "title": "인어공주", "hint": "바다 속 공주의 인간 세계 모험", "category": "디즈니"},
