import streamlit as st
import random
import time # 스피너 효과를 위해 추가

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
st.set_page_config(page_title="이모티콘 영화 맞추기! 🍿", page_icon="🎬", layout="centered")

# --- 3. 영화관 테마 CSS --- (기존 CSS에 힌트 관련 스타일 추가)
st.markdown("""
    <style>
    /* 웹폰트 - Noto Sans KR (깔끔한 한글 폰트) */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Bebas+Neue&display=swap');

    /* 전체 페이지 배경 및 기본 폰트 */
    html, body {
        font-family: 'Noto Sans KR', sans-serif;
        background: linear-gradient(to top, #000000 0%, #1a0000 50%, #330000 100%); /* 어두운 극장 분위기 그라데이션 */
        color: #e0e0e0; /* 밝은 회색 텍스트 */
    }
    
    /* Streamlit 메인 콘텐츠 영역 스타일 */
    .main {
        background: linear-gradient(to bottom, #111111 0%, #220000 100%); /* 메인 패널 어두운 그라데이션 */
        border-radius: 20px; /* 둥근 모서리 */
        padding: 40px; /* 내부 여백 */
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7); /* 깊은 그림자 효과 */
        border: 2px solid #550000; /* 극장 커튼 같은 테두리 */
        animation: fadeIn 1.5s ease-out; /* 로드 시 부드럽게 나타나기 */
    }

    .stApp {
        background-color: #0d0d0d; /* 전체 앱의 배경색 - 더 어둡게 */
    }

    /* 제목 스타일 */
    .cinema-title {
        font-family: 'Bebas Neue', sans-serif; /* 영화 제목 같은 폰트 */
        font-size: 6em !important; /* 엄청 크게 */
        font-weight: 700;
        color: #ffcc00; /* 황금색 타이틀 */
        text-align: center;
        text-shadow: 
            0 0 10px #ffaa00, /* 네온 효과 */
            0 0 20px #ffaa00,
            0 0 30px #ffaa00,
            0 0 40px #ffaa00;
        margin-bottom: 0.5em;
        animation: neonGlow 2s infinite alternate; /* 네온 깜빡임 효과 */
    }
    @keyframes neonGlow {
        from { text-shadow: 0 0 10px #ffaa00, 0 0 20px #ffaa00, 0 0 30px #ffaa00, 0 0 40px #ffaa00; }
        to { text-shadow: 0 0 5px #ffaa00, 0 0 15px #ffaa00, 0 0 25px #ffaa00, 0 0 35px #ffaa00, 0 0 60px #ffaa00; }
    }

    .subtitle {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 1.5em !important;
        color: #ffa500; /* 오렌지색 부제목 */
        text-align: center;
        margin-bottom: 2em;
        font-weight: 700;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    /* 퀴즈 번호 및 이모지 스타일 */
    .question-number {
        font-size: 1.8em;
        color: #cccccc;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .emoji-clue {
        font-size: 5em; /* 이모지 크게 */
        text-align: center;
        margin-bottom: 1em;
        animation: zoomIn 0.8s ease-out; /* 이모지 나타날 때 확대 효과 */
        text-shadow: 2px 2px 5px rgba(0,0,0,0.5); /* 이모지에도 그림자 */
    }

    /* 입력 필드 */
    .stTextInput label {
        font-size: 1.2em !important;
        color: #f0f0f0 !important;
        font-weight: bold !important;
    }
    .stTextInput input {
        background-color: #333333; /* 어두운 입력 필드 */
        color: #eeeeee; /* 밝은 텍스트 */
        border: 2px solid #666666; /* 회색 테두리 */
        border-radius: 8px;
        padding: 10px;
        font-size: 1.1em;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background-color: #880000; /* 강렬한 빨간색 버튼 (극장 커튼 색) */
        color: white;
        border: 2px solid #ffcc00; /* 황금색 테두리 */
        border-radius: 10px;
        padding: 12px 25px;
        font-size: 1.3em;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #ff4500; /* 호버 시 주황색 */
        border-color: #ffffff; /* 흰색 테두리 */
        transform: translateY(-3px); /* 살짝 위로 */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.7);
    }
    
    /* 힌트 버튼 스타일 */
    .hint-button>button {
        background-color: #004d40; /* 짙은 녹색 */
        color: white;
        border: 2px solid #00c853; /* 밝은 녹색 테두리 */
    }
    .hint-button>button:hover {
        background-color: #00796b;
        border-color: #ffffff;
    }


    /* 메시지 (정답/오답/점수) */
    .stSuccess, .stError, .stInfo {
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        font-size: 1.1em;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    .stSuccess { background-color: #28a745; color: white; border-left: 5px solid #1a8a36; }
    .stError { background-color: #dc3545; color: white; border-left: 5px solid #a72a39; }
    .stInfo { background-color: #007bff; color: white; border-left: 5px solid #0056b3; }
    .stWarning { background-color: #ffc107; color: white; border-left: 5px solid #d39e00;}

    /* 점수판 */
    .score-board {
        font-size: 1.5em;
        color: #ffcc00; /* 황금색 */
        text-align: center;
        margin-top: 2em;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    }
    
    /* 스피너 (로딩 효과) */
    .stSpinner > div > div {
        border-top-color: #ffcc00 !important;
    }

    /* 애니메이션 키프레임 */
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

# --- 유틸리티 함수 ---
def normalize_answer(answer):
    """정답을 비교하기 위해 모든 불필요한 문자 제거 및 소문자 변환."""
    return ''.join(filter(str.isalnum, answer)).lower()

def get_next_movie():
    """다음 영화를 가져오고 인덱스 업데이트."""
    if st.session_state.current_movie_index < len(st.session_state.movie_data):
        st.session_state.current_movie_index += 1
        st.session_state.feedback = "" # 피드백 초기화
        st.session_state.attempts = 0 # 시도 횟수 초기화
        st.session_state.hint_shown_for_current_q = False # 힌트 사용 여부 초기화
        st.session_state.current_hint_content = "" # 힌트 내용 초기화
        st.rerun() # 앱을 다시 로드하여 새 문제 표시
    else:
        st.session_state.feedback = "게임 종료! 🎉"


def check_answer(user_guess):
    """사용자 답변을 확인하고 피드백 업데이트."""
    # current_movie_index는 다음 문제를 가리키기 때문에 -1
    current_movie = st.session_state.movie_data[st.session_state.current_movie_index] 
    normalized_user_guess = normalize_answer(user_guess)
    normalized_correct_answer = normalize_answer(current_movie["answer"])

    st.session_state.attempts += 1 # 시도 횟수 증가

    if normalized_user_guess == normalized_correct_answer:
        st.session_state.score += 1
        st.session_state.feedback = f"✨ 정답입니다! **{current_movie['answer']}** 🎬"
        # 정답 시 다음 문제로 바로 넘어가는 버튼 준비 (UI 업데이트용)
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
    if st.button("다시 시작하기", key="restart_game_final", use_container_width=True):
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

    user_guess = st.text_input("영화 제목을 입력하세요:", key=f"guess_{st.session_state.current_movie_index}", placeholder="여기에 영화 제목을 입력...")

    # 정답 확인 버튼과 힌트 버튼 분리
    col_g1, col_g2, col_g3 = st.columns([1,1,1])
    
    with col_g1: # 힌트 버튼은 왼쪽 열에
        if not st.session_state.hint_shown_for_current_q: # 힌트가 아직 안 보여졌을 때만 버튼 표시
            if st.button("힌트 보기 💡", key=f"hint_{st.session_state.current_movie_index}", use_container_width=True):
                with st.spinner('힌트 찾는 중...'):
                    time.sleep(0.5)
                    show_hint()
    with col_g3: # 정답 확인 버튼은 오른쪽 열에
        if st.button("정답 확인 ✅", key=f"check_answer_{st.session_state.current_movie_index}", use_container_width=True):
            if user_guess:
                with st.spinner('정답 확인 중...'):
                    time.sleep(0.8) # 로딩 효과
                    check_answer(user_guess)
            else:
                st.warning("영화 제목을 입력해주세요!")

    # 피드백 표시
    if st.session_state.feedback:
        if "정답입니다" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        elif "아쉽네요" in st.session_state.feedback:
            st.error(st.session_state.feedback)
        else: # 재시도 메시지
            st.info(st.session_state.feedback)
    
    st.markdown(f'<p class="score-board">현재 점수: {st.session_state.score} 점</p>', unsafe_allow_html=True)

    st.write("---") # 구분선

    # 다음 문제 버튼 (정답을 맞췄거나 모든 기회를 소진했을 때)
    if st.session_state.get('correctly_answered_this_turn', False):
        col_n1, col_n2, col_n3 = st.columns([1,2,1])
        with col_n2:
            if st.button("다음 문제 👉", key=f"next_question_{st.session_state.current_movie_index}"):
                st.session_state.correctly_answered_this_turn = False # 플래그 초기화
                get_next_movie() # 다음 문제로 이동
    
# 사이드바 정보
st.sidebar.header("🕹️ 게임 가이드")
st.sidebar.info(
    "1. 이모티콘을 보고 어떤 영화인지 맞춰보세요!\n"
    "2. 영화 제목을 입력하고 '정답 확인' 버튼을 누르세요.\n"
    "3. **'힌트 보기' 버튼으로 장르 힌트를 얻을 수 있어요!**\n"
    "4. 한 문제당 2번 틀리면 정답이 공개되고 다음 문제로 넘어갑니다.\n"
    "5. 모든 문제를 다 풀면 최종 점수를 확인할 수 있습니다!"
)
