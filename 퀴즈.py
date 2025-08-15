import streamlit as st
import random
import time # 로딩 및 애니메이션 지연을 위해 추가

# --- 1. 영화 데이터 (이모티콘 퀴즈) ---
# 영화 목록을 여기에 추가해 주세요! 이모티콘과 정답, 장르를 매칭합니다.
# 띄어쓰기나 대소문자 구별 없이 정답 처리되도록 나중에 전처리할 예정입니다.
movie_list = [
    {"emoji": "🌌👨‍🚀⏱️🪐", "answer": "인터스텔라", "genre": "SF"},
    {"emoji": "🏠🍜🍑", "answer": "기생충", "genre": "드라마"},
    {"emoji": "❄️👸☃️", "answer": "겨울왕국", "genre": "애니메이션"},
    {"emoji": "🦸‍♂️💥🌍", "answer": "어벤져스", "genre": "액션/SF"},
    {"emoji": "🕷️🕸️🌃", "answer": "스파이더맨", "genre": "액션/히어로"},
    {"emoji": "✈️😎🚀", "answer": "탑건", "genre": "액션"},
    {"emoji": "🦁👑🌅", "answer": "라이언 킹", "genre": "애니메이션"},
    {"emoji": "🏴‍☠️⚓️💰", "answer": "캐리비안의 해적", "genre": "판타지/액션"},
    {"emoji": "🦖🌿🌋", "answer": "쥬라기 공원", "genre": "SF/모험"},
    {"emoji": "🧙‍♂️⚡️🦉", "answer": "해리포터", "genre": "판타지"},
    {"emoji": "👽🚲🌕", "answer": "E.T.", "genre": "SF"},
    {"emoji": "🚢💔🌊", "answer": "타이타닉", "genre": "로맨스/드라마"},
    {"emoji": "🎈🏠👴", "answer": "업", "genre": "애니메이션"},
    {"emoji": "🤠👨‍🚀🧸", "answer": "토이 스토리", "genre": "애니메이션"},
    {"emoji": "🍌👖💛", "answer": "미니언즈", "genre": "애니메이션"},
    {"emoji": "💃🎶💫", "answer": "라라랜드", "genre": "뮤지컬/로맨스"},
    {"emoji": "🌊🐟💙", "answer": "아바타", "genre": "SF/모험"},
    {"emoji": "👮‍♂️🔪👊", "answer": "범죄도시", "genre": "액션/범죄"},
    {"emoji": "🧟‍♂️🚆💨", "answer": "부산행", "genre": "액션/재난"},
    {"emoji": "🍗👮‍♂️😂", "answer": "극한직업", "genre": "코미디/액션"},
    {"emoji": "🕵️‍♂️🎩🔎", "answer": "셜록 홈즈", "genre": "미스터리/액션"},
    {"emoji": "🍎🍎🍎📖", "answer": "백설공주", "genre": "애니메이션/판타지"},
    {"emoji": "🍳🐭👨‍🍳", "answer": "라따뚜이", "genre": "애니메이션"},
    {"emoji": "🕰️🔑🚪", "answer": "이상한 나라의 앨리스", "genre": "판타지"},
    {"emoji": "🐒🌴👦", "answer": "정글북", "genre": "모험/드라마"},
    {"emoji": "🐟🐠🐡", "answer": "니모를 찾아서", "genre": "애니메이션"},
    {"emoji": "🌊🌳🏞️", "answer": "모아나", "genre": "애니메이션"},
    {"emoji": "👽🤖🚀", "answer": "월-E", "genre": "애니메이션/SF"},
    {"emoji": "🦁🦁🦁", "answer": "라이온킹", "genre": "애니메이션"}, # 다른 이모지지만 중복영화
    {"emoji": "🎤😈🛡️✨", "answer": "케이팝 데몬 헌터스", "genre": "애니메이션/판타지/뮤지컬"}, # 🎉 새로 추가된 영화!
]

# --- 2. Streamlit 앱 설정 ---
st.set_page_config(page_title="영화관 퀴즈의 마법! 🍿", page_icon="🎬", layout="centered")

# --- 3. 영화관 테마 극대화 CSS ---
st.markdown("""
    <style>
    /* 웹폰트 - Noto Sans KR (깔끔한 한글 폰트), Bebas Neue (영화관 느낌) */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Bebas+Neue&display=swap');

    /* 전체 페이지 배경 및 기본 폰트 */
    html, body {
        font-family: 'Noto Sans KR', sans-serif;
        background: radial-gradient(circle at top, #0d0d0d 0%, #1a0000 70%, #000000 100%); /* 중앙에 집중되는 어두운 그라데이션 */
        color: #f0f0f0; /* 밝은 회색 텍스트 */
    }
    
    /* Streamlit 메인 콘텐츠 영역 스타일 */
    .main {
        background: linear-gradient(to bottom, #111111 0%, #220000 100%); /* 메인 패널 어두운 그라데이션 */
        border-radius: 25px; /* 더 둥근 모서리 */
        padding: 50px; /* 내부 여백 더 늘림 */
        box-shadow: 
            0 15px 50px rgba(0, 0, 0, 0.9), /* 더 강한 그림자 */
            0 0 40px rgba(255, 0, 0, 0.4); /* 붉은색 발광 효과 */
        border: 3px solid #8B0000; /* 깊은 붉은색 테두리 (벨벳 느낌) */
        animation: fadeInScale 1.8s ease-out forwards; /* 로드 시 부드럽게 나타나고 확대 */
    }

    .stApp {
        background-color: #050505; /* 앱 전체의 가장 바깥 배경색 - 거의 검정 */
    }

    /* 제목 스타일 */
    .cinema-title {
        font-family: 'Bebas Neue', sans-serif; /* 영화 제목 같은 폰트 */
        font-size: 7em !important; /* 이모지급으로 엄청 크게! */
        font-weight: 700;
        color: #ffda47; /* 밝은 황금색 타이틀 */
        text-align: center;
        text-shadow: 
            0 0 15px #ffd700, /* 네온 효과 더 강하게 */
            0 0 30px #ffd700,
            0 0 50px #ffcc00,
            0 0 80px #ffbb00;
        margin-bottom: 0.7em;
        animation: neonGlow 2s infinite alternate ease-in-out, bounceIn 1.5s ease-out; /* 네온 깜빡임 + 시작 시 튀어오름 */
        letter-spacing: 5px; /* 자간 늘려서 웅장하게 */
    }
    @keyframes neonGlow {
        from { text-shadow: 0 0 10px #ffda47, 0 0 20px #ffda47, 0 0 30px #ffda47; }
        to { text-shadow: 0 0 5px #ffda47, 0 0 15px #ffda47, 0 0 25px #ffda47, 0 0 45px #ffda47, 0 0 70px #ffda47; }
    }
    @keyframes bounceIn {
        0%, 20%, 40%, 60%, 80%, 100% {
            transition-timing-function: cubic-bezier(0.215, 0.610, 0.355, 1.000);
        }
        0% { opacity: 0; transform: scale3d(0.3, 0.3, 0.3); }
        20% { transform: scale3d(1.1, 1.1, 1.1); }
        40% { transform: scale3d(0.9, 0.9, 0.9); }
        60% { opacity: 1; transform: scale3d(1.03, 1.03, 1.03); }
        80% { transform: scale3d(0.97, 0.97, 0.97); }
        100% { opacity: 1; transform: scale3d(1, 1, 1); }
    }

    .subtitle {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 1.8em !important; /* 부제목도 크게 */
        color: #ffe082; /* 밝은 오렌지색 부제목 */
        text-align: center;
        margin-bottom: 3em; /* 여백 더 늘림 */
        font-weight: 700;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.7); /* 그림자 진하게 */
    }

    /* 퀴즈 번호 및 이모지 스타일 */
    .question-number {
        font-size: 2.2em; /* 더 크게 */
        color: #ffd700; /* 황금색 */
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.8em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    .emoji-clue {
        font-size: 8em; /* 이모지 엄청 크게!!! (사용자 요청) */
        text-align: center;
        margin-bottom: 1.5em;
        animation: swing 1s ease-in-out, zoomIn 0.8s ease-out; /* 스윙 + 확대 효과 */
        text-shadow: 3px 3px 8px rgba(0,0,0,0.8); /* 이모지에도 더 진한 그림자 */
        display: block; /* 가운데 정렬을 위해 */
    }
    @keyframes swing {
        20% { transform: rotate3d(0, 0, 1, 15deg); }
        40% { transform: rotate3d(0, 0, 1, -10deg); }
        60% { transform: rotate3d(0, 0, 1, 5deg); }
        80% { transform: rotate3d(0, 0, 1, -5deg); }
        100% { transform: rotate3d(0, 0, 1, 0deg); }
    }


    /* 입력 필드 */
    .stTextInput label {
        font-size: 1.4em !important;
        color: #ffebcd !important; /* 밝은 피치색 텍스트 */
        font-weight: bold !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
    }
    .stTextInput input {
        background-color: #222222; /* 더 어두운 입력 필드 */
        color: #ffffff; /* 흰색 텍스트 */
        border: 3px solid #ffcc00; /* 황금색 테두리 */
        border-radius: 12px;
        padding: 15px;
        font-size: 1.2em;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.5); /* 안쪽 그림자 */
        transition: border-color 0.3s, box-shadow 0.3s;
    }
    .stTextInput input:focus {
        border-color: #ffd700; /* 포커스 시 황금색 발광 */
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.8);
    }

    /* 버튼 스타일 */
    .stButton>button {
        background: linear-gradient(135deg, #FF0000 0%, #8B0000 100%); /* 강렬한 빨강-짙은 빨강 그라데이션 (커튼 느낌) */
        color: white;
        border: 3px solid #FFD700; /* 황금색 테두리 */
        border-radius: 15px; /* 둥근 사각형 */
        padding: 15px 30px;
        font-size: 1.5em; /* 더 크게 */
        font-weight: bold;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.7), 0 0 20px rgba(255, 0, 0, 0.6); /* 깊은 그림자 + 붉은 발광 */
        transition: all 0.3s ease-in-out;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #FF4500 0%, #CD5C5C 100%); /* 호버 시 주황-인디안레드 그라데이션 */
        border-color: #FFFFFF; /* 흰색 테두리 */
        transform: translateY(-5px) scale(1.02); /* 살짝 위로 + 확대 */
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.8), 0 0 30px rgba(255, 69, 0, 0.8); /* 그림자 + 발광 더 강하게 */
        cursor: pointer;
    }
    
    /* 힌트 버튼 스타일 */
    .hint-button>button {
        background-color: #2e8b57; /* 바다 녹색 */
        border-color: #3cb371; /* 중간 녹색 테두리 */
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.7), 0 0 20px rgba(46, 139, 87, 0.6); /* 초록 발광 */
    }
    .hint-button>button:hover {
        background-color: #3cb371;
        border-color: #ffffff;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.8), 0 0 30px rgba(60, 179, 113, 0.8);
    }


    /* 메시지 (정답/오답/점수) */
    .stSuccess, .stError, .stInfo, .stWarning {
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        font-size: 1.2em; /* 폰트 크게 */
        font-weight: bold;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5); /* 그림자 추가 */
        animation: fadeIn 0.5s ease-out; /* 나타날 때 페이드인 */
    }
    .stSuccess { background: linear-gradient(45deg, #4CAF50, #2E8B57); color: white; border-left: 8px solid #28a745; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }
    .stError { background: linear-gradient(45deg, #dc3545, #8B0000); color: white; border-left: 8px solid #dc3545; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }
    .stInfo { background: linear-gradient(45deg, #007bff, #0056b3); color: white; border-left: 8px solid #007bff; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }
    .stWarning { background: linear-gradient(45deg, #ffc107, #d39e00); color: white; border-left: 8px solid #ffc107; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }

    /* 점수판 */
    .score-board {
        font-size: 1.8em; /* 더 크게 */
        color: #ffcc00; /* 황금색 */
        text-align: center;
        margin-top: 2.5em; /* 여백 더 늘림 */
        font-weight: bold;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8), 0 0 10px #ffcc00; /* 발광하는 그림자 */
    }
    
    /* 스피너 (로딩 효과) */
    .stSpinner > div > div {
        border-top-color: #ffcc00 !important;
    }

    /* 전체 앱 로드 시 애니메이션 */
    @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }

    /* 다른 애니메이션 키프레임들 (기존 유지) */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes zoomIn {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)


# --- 4. 게임 로직 ---

# 세션 상태 초기화 (게임 상태 저장)
if 'movie_data' not in st.session_state:
    st.session_state.movie_data = random.sample(movie_list, len(movie_list)) # 영화 순서 섞기
    st.session_state.current_movie_index = 0
    st.session_state.score = 0
    st.session_state.feedback = ""
    st.session_state.attempts = 0 # 시도 횟수 (힌트/정답 제어용)
    st.session_state.hint_shown_for_current_q = False # 현재 문제에 대한 힌트 사용 여부
    st.session_state.current_hint_content = "" # 현재 보여줄 힌트 내용
    st.session_state.correctly_answered_this_turn = False # 현재 턴 정답 여부

# --- 유틸리티 함수 ---
def normalize_answer(answer):
    """정답을 비교하기 위해 모든 불필요한 문자 제거 및 소문자 변환."""
    return ''.join(filter(str.isalnum, answer)).lower()

def get_next_movie():
    """다음 영화를 가져오고 인덱스 업데이트."""
    if st.session_state.current_movie_index < len(st.session_state.movie_data) - 1: # 마지막 문제일 때 다음으로 넘어가지 않도록 -1
        st.session_state.current_movie_index += 1
        st.session_state.feedback = "" # 피드백 초기화
        st.session_state.attempts = 0 # 시도 횟수 초기화
        st.session_state.hint_shown_for_current_q = False # 힌트 사용 여부 초기화
        st.session_state.current_hint_content = "" # 힌트 내용 초기화
        st.session_state.correctly_answered_this_turn = False # 플래그 초기화
        st.rerun() # 앱을 다시 로드하여 새 문제 표시
    else:
        st.session_state.current_movie_index = len(st.session_state.movie_data) # 마지막 문제 처리 후 종료 상태로
        st.session_state.feedback = "게임 종료! 🎉"


def check_answer(user_guess):
    """사용자 답변을 확인하고 피드백 업데이트."""
    # current_movie_index는 다음 문제를 가리키기 때문에 +0
    current_movie = st.session_state.movie_data[st.session_state.current_movie_index] 
    normalized_user_guess = normalize_answer(user_guess)
    normalized_correct_answer = normalize_answer(current_movie["answer"])

    if st.session_state.correctly_answered_this_turn: # 이미 정답 처리되었으면 다시 검사하지 않음
        return

    st.session_state.attempts += 1 # 시도 횟수 증가

    if normalized_user_guess == normalized_correct_answer:
        st.session_state.score += 1
        st.session_state.feedback = f"✨ 정답입니다! **{current_movie['answer']}** 🎬"
        st.session_state.correctly_answered_this_turn = True # 정답을 맞췄다는 플래그
    else:
        if st.session_state.attempts < 2: # 2번의 기회 부여 (0, 1)
             st.session_state.feedback = f"😅 아닙니다! 다시 시도해보세요! ({st.session_state.attempts}/2)"
        else: # 2번 이상 틀리면 정답 공개
            st.session_state.feedback = f"😭 아쉽네요! 정답은 **{current_movie['answer']}** 였습니다."
            st.session_state.correctly_answered_this_turn = True # 다음 문제로 넘어가는 플래그

# --- 힌트 기능 ---
def show_hint():
    current_movie = st.session_state.movie_data[st.session_state.current_movie_index]
    st.session_state.hint_shown_for_current_q = True
    st.session_state.current_hint_content = f"장르 힌트: **{current_movie['genre']}** 💡"
    st.info(st.session_state.current_hint_content) # 힌트 내용 즉시 표시

# --- 앱 UI 구성 ---
st.markdown('<p class="cinema-title">🎬 EMOJI MOVIE QUIZ 🍿</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">이모티콘을 보고 영화 제목을 맞춰보세요!</p>', unsafe_allow_html=True)

# 게임 진행
if st.session_state.current_movie_index >= len(st.session_state.movie_data):
    # 게임 종료
    st.markdown("<h2>게임 종료! 🎉</h2>", unsafe_allow_html=True)
    st.markdown(f'<p class="score-board">최종 점수: {st.session_state.score} / {len(movie_list)}</p>', unsafe_allow_html=True)
    st.balloons() # 풍선 효과
    if st.button("🌟 마법처럼 다시 시작하기 🌟", key="restart_game_final", use_container_width=True):
        st.session_state.clear() # 세션 상태 초기화
        st.rerun() # 앱 다시 로드
else:
    # 현재 영화 정보 표시
    current_movie = st.session_state.movie_data[st.session_state.current_movie_index]

    st.markdown(f'<p class="question-number">문제 {st.session_state.current_movie_index + 1} / {len(st.session_state.movie_data)}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="emoji-clue">{current_movie["emoji"]}</p>', unsafe_allow_html=True)

    # 힌트가 이미 표시된 경우
    if st.session_state.hint_shown_for_current_q and st.session_state.current_hint_content:
        st.info(st.session_state.current_hint_content) # 힌트 내용 표시

    user_guess = st.text_input("영화 제목을 입력하세요:", key=f"guess_{st.session_state.current_movie_index}", placeholder="여기에 영화 제목을 입력...", disabled=st.session_state.correctly_answered_this_turn)

    # 정답 확인 버튼과 힌트 버튼 분리
    col_g1, col_g2 = st.columns(2) # 버튼을 2개 열로 나누기
    
    with col_g1: # 힌트 버튼은 왼쪽 열에
        if not st.session_state.hint_shown_for_current_q: # 힌트가 아직 안 보여졌을 때만 버튼 표시
            if st.button("💡 힌트 보기", key=f"hint_{st.session_state.current_movie_index}", use_container_width=True, disabled=st.session_state.correctly_answered_this_turn):
                with st.spinner('🌟 힌트 찾는 중...'):
                    time.sleep(0.5)
                    show_hint()
    with col_g2: # 정답 확인 버튼은 오른쪽 열에
        if st.button("✅ 정답 확인", key=f"check_answer_{st.session_state.current_movie_index}", use_container_width=True, disabled=st.session_state.correctly_answered_this_turn):
            if user_guess:
                with st.spinner('🤔 정답 확인 중...'):
                    time.sleep(0.8) # 로딩 효과
                    check_answer(user_guess)
            else:
                st.warning("🎬 영화 제목을 입력해주세요!")

    # 피드백 표시
    if st.session_state.feedback:
        if "정답입니다" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        elif "아쉽네요" in st.session_state.feedback:
            st.error(st.session_state.feedback)
        else: # 재시도 메시지 (info)
            st.info(st.session_state.feedback)
    
    st.markdown(f'<p class="score-board">현재 점수: {st.session_state.score} 점</p>', unsafe_allow_html=True)

    st.write("---") # 구분선

    # 다음 문제 버튼 (정답을 맞췄거나 모든 기회를 소진했을 때)
    if st.session_state.get('correctly_answered_this_turn', False):
        col_n1, col_n2, col_n3 = st.columns([1,2,1])
        with col_n2:
            # 마지막 문제일 경우 "게임 종료" 버튼으로 변경
            if st.session_state.current_movie_index == len(st.session_state.movie_data) - 1:
                if st.button("🎉 게임 결과 확인하기! 🎉", key="final_results_button", use_container_width=True):
                    get_next_movie() # 게임 종료 상태로 변경
            else:
                if st.button("👉 다음 문제로 이동", key=f"next_question_{st.session_state.current_movie_index}", use_container_width=True):
                    get_next_movie() # 다음 문제로 이동
    
# 사이드바 정보
st.sidebar.header("🕹️ 게임 가이드 - 시네마 매직! 🍿")
st.sidebar.info(
    "1. 반짝이는 이모티콘을 보고 어떤 영화인지 맞춰보세요!\n"
    "2. 영화 제목을 입력하고 '✅ 정답 확인' 버튼을 누르세요.\n"
    "3. **'💡 힌트 보기' 버튼으로 장르 힌트를 얻을 수 있어요! 한 문제당 한 번만 사용 가능해요!**\n"
    "4. 한 문제당 2번 틀리면 정답이 공개되고 다음 문제로 자동으로 넘어갈 준비를 합니다.\n"
    "5. 모든 문제를 다 풀면 '🌟 마법처럼 다시 시작하기 🌟' 버튼이 나타납니다!\n"
    "\n✨ 즐거운 영화 퀴즈 되세요! ✨"
)
