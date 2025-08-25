import streamlit as st

st.title("🌍 멸종위기종 탐험 앱")
st.write("서식지를 선택하면 그곳에 사는 멸종위기 동물들을 확인할 수 있어요.")

# 서식지와 동물 데이터
habitats = {
    "🌴 열대우림": [
        {"name": "오랑우탄", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Orangutan.jpg"},
        {"name": "재규어", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Standing_jaguar.jpg"},
    ],
    "🏜 사막": [
        {"name": "아라비아 오릭스", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Arabian_Oryx_Oman.jpg"},
        {"name": "펜넥여우", "img": "https://upload.wikimedia.org/wikipedia/commons/7/79/Fennec_Fox.jpg"},
    ],
    "🌊 바다": [
        {"name": "바다거북", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Green_turtle_swimming_over_coral_reefs_in_Kona.jpg"},
        {"name": "범고래", "img": "https://upload.wikimedia.org/wikipedia/commons/3/37/Killerwhales_jumping.jpg"},
    ],
    "❄️ 극지방": [
        {"name": "북극곰", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Polar_Bear_-_Alaska.jpg"},
        {"name": "황제펭귄", "img": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Emperor_Penguin_Manchot_empereur.jpg"},
    ]
}

# 선택박스
choice = st.selectbox("서식지를 선택하세요:", list(habitats.keys()))

# 선택한 서식지 동물 출력
st.subheader(f"{choice}에 사는 멸종위기 동물들")
animals = habitats[choice]

for animal in animals:
    st.write(f"**{animal['name']}**")
    st.image(animal["img"], use_container_width=True)
    st.markdown("---")
