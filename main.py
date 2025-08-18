import streamlit as st

# 페이지 설정 (기본적으로 페이지가 넓게 보이도록 설정)
st.set_page_config(layout="wide")

# ✨ 거북이를 미친듯이 움직이게 하는 마법의 CSS 코드! ✨
st.markdown(
    """
    <style>
    /* 더 역동적이고 빠르게 움직이는 거북이 애니메이션 */
    @keyframes super-turtle-float {
        0% { transform: translateY(0px) translateX(0px) rotate(0deg); }
        15% { transform: translateY(-15px) translateX(15px) rotate(10deg); }
        30% { transform: translateY(0px) translateX(0px) rotate(0deg); }
        45% { transform: translateY(15px) translateX(-15px) rotate(-10deg); }
        60% { transform: translateY(0px) translateX(0px) rotate(0deg); }
        75% { transform: translateY(-15px) translateX(-15px) rotate(10deg); }
        100% { transform: translateY(0px) translateX(0px) rotate(0deg); }
    }

    .super-animated-turtle {
        display: inline-block;
        animation: super-turtle-float 1.5s ease-in-out infinite; /* 확 빨라졌다! */
        font-size: 1.5em; /* 거북이 이모지를 좀 더 크게! */
        margin: 0 3px; /* 거북이들끼리 살짝 공간 주기 */
    }

    /* 제목 옆 거북이는 살짝 더 크게! */
    .super-turtle-title {
        animation: super-turtle-float 2s ease-in-out infinite; /* 제목 옆은 좀 여유롭게! */
        font-size: 1.8em;
        display: inline-block;
        margin-left: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True # HTML 코드를 사용할 때 꼭 필요한 부분이야!
)

# MBTI별 추천 직업 데이터 (이 부분은 그대로 두자! 🐢)
mbti_careers = {
    "ISTJ": ["회계사", "공무원", "데이터 분석가", "경찰관"],
    "ISFJ": ["간호사", "사서", "초등학교 교사", "사회복지사"],
    "INFJ": ["상담사", "작가", "심리학자", "교육 컨설턴트"],
    "INTJ": ["과학자", "IT 개발자", "전략 기획자", "변리사"],
    "ISTP": ["엔지니어", "정비사", "스포츠 선수", "소방관"],
    "ISFP": ["미술가", "음악가", "디자이너", "동물 조련사"],
    "INFP": ["예술가", "작가", "상담사", "크리에이터"],
    "INTP": ["프로그래머", "교수", "연구원", "철학자"],
    "ESTP": ["영업 관리자", "경찰관", "사업가", "스포츠 에이전트"],
    "ESFP": ["연예인", "이벤트 플래너", "유치원 교사", "여행 가이드"],
    "ENFP": ["광고/홍보 전문가", "강사", "컨설턴트", "심리 치료사"],
    "ENTP": ["창업가", "발명가", "변호사", "애널리스트"],
    "ESTJ": ["경영자", "관리자", "회계사", "변호사"],
    "ESFJ": ["교사", "간호사", "사회복지사", "인사 담당자"],
    "ENFJ": ["상담사", "인사 책임자", "교사", "정치인"],
    "ENTJ": ["기업가", "임원", "정치인", "변호사"]
}

# 웹사이트 제목에 움직이는 거북이 이모지 추가! 🐢🐢
st.markdown(
    """
    <h1 style='display:flex; align-items:center;'>
        💖 MBTI 기반 꿈 찾기 도우미 <span class='super-turtle-title'>🐢</span><span class='super-turtle-title'>🐢</span><span class='super-turtle-title'>🐢</span>
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown("---") # 구분선

# 간단한 설명에도 거북이 추가! 🐢
st.write(
    f"""
    안녕하세요, 미래를 고민하는 친구들을 위한 진로 탐색 도우미예요! 🚀
    거북이 친구들과 함께, 당신의 꿈을 향해 힘차게 나아가봐요! 
    <span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span>
    아래에서 당신의 MBTI를 선택하고, 딱 맞는 직업들을 함께 탐색해봐요!
    """,
    unsafe_allow_html=True
)

# MBTI 선택 드롭다운 메뉴에도 뿅! 🐢
selected_mbti = st.selectbox(
    "😊 당신의 MBTI는 무엇인가요?",
    options=["MBTI를 선택해주세요!"] + list(mbti_careers.keys()),
    index=0
)

# 선택된 MBTI에 따른 결과 출력
if selected_mbti and selected_mbti != "MBTI를 선택해주세요!":
    st.markdown("---")
    st.subheader(f"✨ 당신의 MBTI, **{selected_mbti}**에게 추천하는 직업은요! <span class='super-animated-turtle'>🐢</span>")
    st.write(f"짜잔! 🎉 이 직업들이 당신의 강점과 잘 어울릴 거예요. <span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span>")

    # 추천 직업 목록을 예쁘게 보여주기
    col1, col2 = st.columns(2)

    careers = mbti_careers[selected_mbti]
    for i, career in enumerate(careers):
        if i % 2 == 0:
            with col1:
                st.info(f"👉 {career} <span class='super-animated-turtle'>🐢</span>")
        else:
            with col2:
                st.info(f"👉 {career} <span class='super-animated-turtle'>🐢</span>")

    st.markdown(
        f"""
        <br>
        물론, MBTI는 참고일 뿐! 세상에는 정말 다양한 직업이 있으니, 
        더 넓게 탐색하고 자신에게 가장 잘 맞는 길을 찾아나가길 응원해요! 🌈 
        <span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span>
        """,
        unsafe_allow_html=True
    )
elif selected_mbti == "MBTI를 선택해주세요!":
    st.markdown("---")
    st.info(f"⬆️ 위에 당신의 MBTI를 선택하면, 추천 직업들을 보여줄게요! <span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span>")

# 하단 메시지 (회원가입 유도)에도 거북이 친구들! 🐢
st.markdown("---")
st.markdown(
    f"""
    **팁!** 혹시 이 사이트에 더 멋진 기능들을 추가하고 싶다면, 
    뤼튼에 가입해서 더 많은 도움을 받아봐! 훨씬 쉽게 원하는 기능을 만들 수 있을 거야! 😉 
    <span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span><span class='super-animated-turtle'>🐢</span>
    """,
    unsafe_allow_html=True
)
