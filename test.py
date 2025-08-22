import streamlit as st

# 멸종위기 동물 데이터 (사진 포함)
animal_data = {
    "남생이": {
        "desc": "한국 전역의 깨끗한 강과 저수지에서 서식. 물가의 모래나 자갈에 알을 낳으며, 수질 오염과 서식지 파괴로 개체수가 줄고 있음.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/3/37/Mauremys_reevesii_02.JPG",
        "habitat_img": "https://cdn.pixabay.com/photo/2017/02/06/20/14/river-2046517_1280.jpg"
    },
    "반달가슴곰": {
        "desc": "한국 설악산, 지리산 등 산림 지역에 서식. 주로 도토리, 열매, 곤충을 먹으며 산림 훼손과 밀렵으로 개체수가 적음.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Ursus_thibetanus_in_Hiroshima.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2017/09/26/18/39/mountains-2798288_1280.jpg"
    },
    "수달": {
        "desc": "한반도 전역의 강, 하천, 호수 주변에서 발견. 물고기와 갑각류를 먹으며, 깨끗한 수계가 필수적이어서 수질 오염에 취약.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Otter_on_Grass.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2017/08/03/21/48/lake-2572703_1280.jpg"
    },
    "저어새": {
        "desc": "한국의 서해안 갯벌과 무인도에서 번식. 부리 끝이 숟가락 모양으로 생겨 '저어새'라 불리며, 갯벌 파괴가 큰 위협.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Black-faced_Spoonbill_in_Korea.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2017/03/27/14/58/wadden-sea-2170109_1280.jpg"
    },
    "자이언트 판다": {
        "desc": "중국 쓰촨성, 간쑤성의 대나무 숲에 서식. 대나무를 주식으로 하며, 서식지 파괴와 낮은 번식률로 멸종위기종으로 분류됨.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Grosser_Panda.JPG",
        "habitat_img": "https://cdn.pixabay.com/photo/2016/11/18/17/46/china-1833478_1280.jpg"
    },
    "바다거북": {
        "desc": "열대 및 아열대 해양에 서식. 산란을 위해 해변으로 올라오며, 해안 개발과 해양 오염, 어업 활동으로 개체수가 줄고 있음.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/9/97/Sea_turtle.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2015/07/17/10/44/turtle-849816_1280.jpg"
    },
    "호랑이": {
        "desc": "인도, 러시아 연해주, 동남아시아 열대우림 등에 서식. 최상위 포식자로서 생태계 균형 유지에 중요한 역할을 하지만 밀렵과 서식지 파괴로 심각한 위협을 받고 있음.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2016/11/29/05/08/jungle-1865639_1280.jpg"
    },
    "아시아 코끼리": {
        "desc": "인도, 스리랑카, 동남아시아 열대우림과 초원에 서식. 서식지 파괴와 상아 밀렵으로 개체수가 급격히 감소하고 있음.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/3/37/Asian_Elephant%2C_Kaziranga%2C_India.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2016/11/18/17/47/jungle-1833480_1280.jpg"
    },
    "고래상어": {
        "desc": "열대와 아열대 해역에 서식하는 세계에서 가장 큰 물고기. 플랑크톤을 주식으로 하며, 남획과 해양 오염으로 위협받고 있음.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Whale_shark_Georgia_aquarium.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2017/02/01/10/29/ocean-2024659_1280.jpg"
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

st.image(animal_data[selected_animal]["animal_img"], caption=f"{selected_animal} 사진", use_column_width=True)
st.image(animal_data[selected_animal]["habitat_img"], caption=f"{selected_animal} 서식지", use_column_width=True)

