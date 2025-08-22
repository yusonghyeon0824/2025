import streamlit as st

# 멸종위기 동물 데이터 (이미지 URL 포함)
animal_data = {
    "남생이": {
        "desc": "한국과 동아시아의 담수에서 서식하는 반수생 거북. 수질 오염과 경쟁종으로 인해 개체수가 줄어들고 있습니다.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Chinese_Pond_Turtle_%28Mauremys_reevesii%29.jpg",
        "habitat_img": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Restored_Cheonggyecheon_in_Seoul.jpg"
    },
    "반달가슴곰": {
        "desc": "한국 지리산과 설악산 등에 서식. 가슴의 흰색 반달 무늬가 특징이며, 산림 훼손과 밀렵으로 개체수가 위협받고 있습니다.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Ursus_thibetanus_in_Hiroshima.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2017/09/26/18/39/mountains-2798288_1280.jpg"
    },
    "수달": {
        "desc": "한반도 강, 하천, 호수에 서식. 깨끗한 물을 필요로 하며, 어류와 갑각류를 먹습니다. 수질 오염이 큰 위협 요소입니다.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Otter_on_Grass.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2017/08/03/21/48/lake-2572703_1280.jpg"
    },
    "저어새": {
        "desc": "한국 서해안 갯벌과 무인도에서 번식. 긴 부리 끝이 숟가락처럼 생긴 것이 특징입니다. 갯벌 파괴가 주요 위협입니다.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Black-faced_Spoonbill_in_Korea.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2017/03/27/14/58/wadden-sea-2170109_1280.jpg"
    },
    "자이언트 판다": {
        "desc": "중국 쓰촨성의 대나무 숲에 서식. 대나무가 주식이며 낮은 번식률과 서식지 감소로 멸종위기종입니다.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Grosser_Panda.JPG",
        "habitat_img": "https://cdn.pixabay.com/photo/2016/11/18/17/46/china-1833478_1280.jpg"
    },
    "바다거북": {
        "desc": "열대 및 아열대 해양에 서식. 산란을 위해 모래사장을 찾으며, 해양 쓰레기와 어업 활동으로 위협받습니다.",
        "animal_img": "https://upload.wikimedia.org/wikipedia/commons/9/97/Sea_turtle.jpg",
        "habitat_img": "https://cdn.pixabay.com/photo/2015/07/17/10/44/turtle-849816_1280.jpg"
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
st.image(animal_data[selected_animal]["animal_img"], caption=f"{selected_animal} 사진", use_column_width=True)

# 서식지 사진
st.image(animal_data[selected_animal]["habitat_img"], caption=f"{selected_animal} 서식지", use_column_width=True)

