import streamlit as st
from pathlib import Path

# 이미지 폴더 경로
img_path = Path("images")

# 멸종위기 동물 데이터 (로컬 이미지 사용)
animal_data = {
    "남생이": {
        "desc": "한국과 동아시아의 담수에서 서식하는 반수생 거북. 수질 오염과 경쟁종으로 인해 개체수가 줄고 있습니다.",
        "animal_img": img_path / "namsaengi.jpg",
        "habitat_img": img_path / "river.jpg"
    },
    "반달가슴곰": {
        "desc": "한국 지리산과 설악산 등에 서식. 가슴의 흰색 반달 무늬가 특징이며, 산림 훼손과 밀렵으로 개체수가 위협받고 있습니다.",
        "animal_img": img_path / "bandal_bear.jpg",
        "habitat_img": img_path / "mountain_forest.jpg"
    },
    "수달": {
        "desc": "한반도 강, 하천, 호수에 서식. 깨끗한 물을 필요로 하며, 어류와 갑각류를 먹습니다. 수질 오염이 큰 위협 요소입니다.",
        "animal_img": img_path / "otter.jpg",
        "habitat_img": img_path / "lake.jpg"
    },
    "저어새": {
        "desc": "한국 서해안 갯벌과 무인도에서 번식. 긴 부리 끝이 숟가락처럼 생긴 것이 특징입니다. 갯벌 파괴가 주요 위협입니다.",
        "animal_img": img_path / "spoonbill.jpg",
        "habitat_img": img_path / "mudflat.jpg"
    },
    "자이언트 판다": {
        "desc": "중국 쓰촨성의 대나무 숲에 서식. 대나무가 주식이며 낮은 번식률과 서식지 감소로 멸종위기종입니다.",
        "animal_img": img_path / "panda.jpg",
        "habitat_img": img_path / "bamboo_forest.jpg"
    },
    "바다거북": {
        "desc": "열대 및 아열대 해양에 서식. 산란을 위해 모래사장을 찾으며, 해양 쓰레기와 어업 활동으로 위협받습니다.",
        "animal_img": img_path / "sea_turtle.jpg",
        "habitat_img": img_path / "ocean.jpg"
    },
    "호랑이": {
        "desc": "인도, 러시아 연해주, 동남아시아 열대우림 등에 서식. 밀렵과 서식지 파괴로 위협받고 있습니다.",
        "animal_img": img_path / "tiger.jpg",
        "habitat_img": img_path / "jungle.jpg"
    },
    "아시아 코끼리": {
        "desc": "인도, 스리랑카, 동남아시아 열대우림과 초원에 서식. 서식지 파괴와 상아 밀렵으로 개체수가 감소하고 있습니다.",
        "animal_img": img_path / "elephant.jpg",
        "habitat_img": img_path / "savanna.jpg"
    },
    "고래상어": {
        "desc": "열대와 아열대 해역에 서식하는 세계에서 가장 큰 물고기. 플랑크톤을 먹으며, 남획과 해양 오염으로 위협받습니다.",
        "animal_img": img_path / "whale_shark.jpg",
        "habitat_img": img_path / "ocean.jpg"
    },
    "장수하늘소": {
        "desc": "한국의 활엽수림, 특히 오래된 참나무 숲에서 발견. 산림 파괴로 개체수가 급감하고 있습니다.",
        "animal_img": img_path / "longhorn_beetle.jpg",
        "habitat_img": img_path / "forest.jpg"
    }
}

# 웹앱 제목
st.title("🌍 멸종위기 동물 서식지 탐색기")

st.write("멸종위기 동물을 선택하면 해당 동물의 사진과 서식지를 확인할 수 있습니다.")

# 동물 선택
selected_animal = st.selectbox("동물을 선택하세요:", list(animal_data.keys()))

# 정보 출력
st.subheader(f"🐾 {selected_animal}")
st.write(animal_data[selected_animal]["desc"])

# 동물 사진
st.image(animal_data[selected_animal]["animal_img"], caption=f"{selected_animal} 사진", use_container_width=True)

# 서식지 사진
st.image(animal_data[selected_animal]["habitat_img"], caption=f"{selected_animal} 서식지", use_container_width=True)
