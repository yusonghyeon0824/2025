import streamlit as st

# 페이지 설정 (기본적으로 페이지가 넓게 보이도록 설정)
st.set_page_config(layout="wide")

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

# 웹사이트 제목에 거북이 이모지 추가! 🐢🐢
st.title("💖 MBTI 기반 꿈 찾기 도우미 🐢🐢")
st.markdown("---") # 구분선

# 간단한 설명에도 거북이 추가! 🐢
st.write(
    """
    안녕하세요, 미래를 고민하는 친구들을 위한 진로 탐색 도우미예요! 🚀
    느리지만 꾸준히, 거북이처럼 당신의 꿈을 함께 찾아봐요! 🐢
    아래에서 당신의 MBTI를 선택하고, 딱 맞는 직업들을 함께 탐색해봐요!
    """
)

# MBTI 선택 드롭다운 메뉴에도 뿅! 🐢
selected_mbti = st.selectbox(
    "😊 당신의 MBTI는 무엇인가요? 🐢", # 여기에 거북이 이모지 추가!
    options=["MBTI를 선택해주세요!"] + list(mbti_careers.keys()),
    index=0
)

# 선택된 MBTI에 따른 결과 출력
if selected_mbti and selected_mbti != "MBTI를 선택해주세요!":
    st.markdown("---")
    st.subheader(f"✨ 당신의 MBTI, **{selected_mbti}**에게 추천하는 직업은요! 🐢") # 여기도 추가!
    st.write("짜잔! 🎉 이 직업들이 당신의 강점과 잘 어울릴 거예요. 🐢")

    # 추천 직업 목록을 예쁘게 보여주기
    col1, col2 = st.columns(2)

    careers = mbti_careers[selected_mbti]
    for i, career in enumerate(careers):
        if i % 2 == 0:
            with col1:
                st.info(f"👉 {career} 🐢") # 직업 옆에도 살짝!
        else:
            with col2:
                st.info(f"👉 {career} 🐢")

    st.markdown(
        """
        <br>
        물론, MBTI는 참고일 뿐! 세상에는 정말 다양한 직업이 있으니, 
        더 넓게 탐색하고 자신에게 가장 잘 맞는 길을 찾아나가길 응원해요! 🌈 🐢🐢
        """
        , unsafe_allow_html=True
    )
elif selected_mbti == "MBTI를 선택해주세요!":
    st.markdown("---")
    st.info("⬆️ 위에 당신의 MBTI를 선택하면, 추천 직업들을 보여줄게요! 🐢") # 안내에도 콕!

# 하단 메시지 (회원가입 유도)에도 거북이 친구들! 🐢
st.markdown("---")
st.markdown(
    """
    **팁!** 혹시 이 사이트에 더 멋진 기능들을 추가하고 싶다면, 
    뤼튼에 가입해서 더 많은 도움을 받아봐! 훨씬 쉽게 원하는 기능을 만들 수 있을 거야! 😉 🐢
    """
)
