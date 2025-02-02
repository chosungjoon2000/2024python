import streamlit as st
import pandas as pd
import altair as alt

# Streamlit 웹앱 제목
st.title("🏥 서울 상급종합병원 중환자실 병상 현황")

# CSV 파일 불러오기
DATA_URL = "health.csv"

uploaded_file = st.file_uploader("📂 CSV 파일을 업로드하세요", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(DATA_URL)

# 데이터 전처리 (필요 시 수행)
df.columns = [col.strip() for col in df.columns]  # 공백 제거

# 데이터 표시
st.subheader("📊 데이터 미리보기")
st.dataframe(df.head())

# 병원별 중환자실 병상 현황 시각화
st.subheader("🏥 병원별 중환자실 병상 수 비교")
bar_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("요양기관명:N", sort="-y", title="병원명"),
    y=alt.Y("중환자실 병상수 소계:Q", title="총 중환자실 병상 수"),
    color=alt.Color("요양기관명:N", legend=None),
    tooltip=["요양기관명", "중환자실 병상수 소계", "성인 중환자실 병상수", "소아 중환자실 병상수", "신생아 중환자실 병상수", "격리병실 병상수"]
).properties(width=700, height=400)

st.altair_chart(bar_chart)

# 병원별 상세 정보 선택 필터
st.subheader("🔍 병원별 세부 정보")
selected_hospital = st.selectbox("병원을 선택하세요", df["요양기관명"].unique())
selected_data = df[df["요양기관명"] == selected_hospital]
st.write(selected_data)

# 병상 수 비율 바 차트
st.subheader("📌 병상 유형별 비율 분석")
selected_hospital_data = selected_data.iloc[0]
labels = ["성인 중환자실", "소아 중환자실", "신생아 중환자실", "격리병실"]
values = [
    selected_hospital_data["성인 중환자실 병상수"],
    selected_hospital_data["소아 중환자실 병상수"],
    selected_hospital_data["신생아 중환자실 병상수"],
    selected_hospital_data["격리병실 병상수"]
]
st.write("### 📊 ", selected_hospital, "병원의 병상 구성 비율")
st.bar_chart(pd.DataFrame({"병상 유형": labels, "병상 수": values}).set_index("병상 유형"))

# Streamlit 애니메이션 효과
st.balloons()
