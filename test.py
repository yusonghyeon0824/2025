import streamlit as st

st.set_page_config(page_title="멸종위기종 탐험", layout="wide")

st.title("🌍 멸종위기종을 만나러 가보자!!!")
st.write("서식지 사진을 클릭하면 그곳에 사는 멸종위기 동물들을 확인할 수 있어요!")

# 서식지와 동물 데이터
habitats = {
    "열대우림": {
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgtkurLA8MhD6LOTsvZqTYqUI2WA7OZe5iCg&s",
        "animals": [
            {"name": "오랑우탄", "img": "https://i.namu.wiki/i/KdaEX59KjJ0XLrGls34LeBPbHN-556HnwdLJLUS_jl1cm58UIRdwOM4pQ2yAkJardGAvmCX-Q2jaV8C8xZ4TMQ.webp",
             "desc": "열대우림에 서식하며, 서식지 파괴로 멸종 위기에 처해 있습니다."},
            {"name": "재규어", "img": "https://upload.wikimedia.org/wikipedia/commons/1/11/Jaguar_%28Panthera_onca_palustris%29_male_Three_Brothers_River_2_%28cropped%29.jpg",
             "desc": "남아메리카의 대표적 맹수로, 서식지 감소와 불법 사냥의 위협을 받고 있습니다."}
        ]
    },
    "사막": {
        "img": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Libya_5230_Wan_Caza_Dunes_Luca_Galuzzi_2007.jpg",
        "animals": [
            {"name": "아라비아 오릭스", "img": "https://i.namu.wiki/i/2Yl-D08YkWD_02K0yNPgJg0hOw9-CIoOa5_KTS4v8Qgo463hjg_ri_HVyrznMo4YZ3m0zZn0Vzgx1PRoYvwcqw.webp",
             "desc": "사막의 혹독한 환경에서 살아가는 영양으로, 과거 멸종 위기에서 복원되었습니다."},
            {"name": "페넥여우", "img": "https://pimg.mk.co.kr/meet/neds/2015/01/image_readtop_2015_71113_14218941471733860.jpg",
             "desc": "큰 귀가 특징인 사막 여우로, 불법 애완동물 거래로 위협받고 있습니다."}
        ]
    },
    "바다": {
        "img": "https://m.health.chosun.com/site/data/img_dir/2023/05/31/2023053102582_0.jpg",
        "animals": [
            {"name": "바다거북", "img": "https://waterstone.kr/data/file/challenge_list/832805294_0sBvzDnm_5e7248eca58031c67fa0ee7820a7a5dc8ef402b2.png",
             "desc": "산란지 파괴와 해양 오염으로 인해 개체 수가 급감하고 있습니다."},
            {"name": "범고래", "img": "https://upload.wikimedia.org/wikipedia/commons/3/37/Killerwhales_jumping.jpg",
             "desc": "최상위 포식자로 해양 생태계에서 중요한 역할을 하지만, 오염과 먹이 부족으로 위협받고 있습니다."}
        ]
    },
    "극지방": {
        "img": "https://img.freepik.com/free-photo/icebergs-glacier-lagoon-iceland_1232-4683.jpg?semt=ais_hybrid&w=740&q=80",
        "animals": [
            {"name": "북극곰", "img": "https://cdn.imweb.me/upload/S2022083177899bd6d2f9d/14a602c979130cc15cf463fe2d760c26e11ab6a2.jpeg",
             "desc": "빙하가 녹으면서 서식지가 줄어드는 대표적 기후 위기 피해 동물입니다."},
            {"name": "황제펭귄", "img": "https://cdn.eyesmag.com/content/uploads/posts/2023/08/25/3-bd95218b-703e-4fb0-a3f7-d5922b596363.jpg",
             "desc": "남극에 서식하며, 기후 변화로 인한 번식지 감소가 큰 위협이 되고 있습니다."}
        ]
    }
}

# 상태 저장 (어느 서식지를 클릭했는지 기억)
if "selected_habitat" not in st.session_state:
    st.session_state["selected_habitat"] = None

# 서식지 선택 화면
if st.session_state["selected_habitat"] is None:
    st.subheader("서식지를 선택하세요 🖼️")
    cols = st.columns(4)
    for i, (habitat, data) in enumerate(habitats.items()):
        with cols[i]:
            st.image(data["img"], use_container_width=True, caption=habitat)
            if st.button(f"{habitat} 보기", key=habitat):
                st.session_state["selected_habitat"] = habitat

# 동물 출력 화면
else:
    habitat = st.session_state["selected_habitat"]
    st.header(f"📍 {habitat}에 사는 멸종위기 동물들")
    st.markdown("⬅️ 왼쪽 사이드바에서 '처음으로' 버튼을 눌러 다른 서식지를 선택할 수 있습니다.")

    for animal in habitats[habitat]["animals"]:
        st.subheader(animal["name"])
        st.image(animal["img"], use_container_width=True)
        st.write(animal["desc"])
        st.markdown("---")

    # 사이드바에서 돌아가기 버튼
    if st.sidebar.button("처음으로"):
        st.session_state["selected_habitat"] = None
