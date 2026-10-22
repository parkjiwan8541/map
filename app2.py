import math
import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

# 1. 앱 제목 설정
st.title("🚇 부산 지하철 역별 이용객 수 지도 분석")
st.write("CSV 파일을 업로드하여 호선별 필터 및 상위 역 정보를 확인해보세요.")

# 2. CSV 파일 업로드
uploaded_file = st.file_uploader(
    "busan_subway.csv 파일을 업로드하세요", type=["csv"]
)

if uploaded_file is not None:
  # 데이터 읽기
  df = pd.read_csv(uploaded_file)

  # [색상] 호선별 색상 지정 (딕셔너리 활용)
  line_colors = {
      "1호선": "orange",  # 주황
      "2호선": "green",  # 초록
      "3호선": "brown",  # 갈색
      "4호선": "blue",  # 파랑
  }

  # [호선필터] Multiselect로 호선 선택 (기본값: 전체 호선 선택)
  all_lines = sorted(df["호선"].unique().tolist())
  selected_lines = st.multiselect(
      "조회할 호선을 선택하세요", options=all_lines, default=all_lines
  )

  # 선택된 호선 데이터만 필터링
  filtered_df = df[df["호선"].isin(selected_lines)]

  # 3. 지도 기본 위치 설정 (부산 중심 좌표)
  m = folium.Map(location=[35.17955, 129.07564], zoom_start=11)

  # 4. 지도에 선택된 호선의 역만 원형 마커(CircleMarker)로 표시
  for index, row in filtered_df.iterrows():
    # 원의 면적이 이용객수에 비례하도록 반지름을 제곱근으로 계산
    radius_size = math.sqrt(row["이용객수"]) * 0.1

    # 호선에 맞는 색상 가져오기 (지정되지 않은 호선은 기본 검은색)
    line_color = line_colors.get(row["호선"], "black")

    # 마커 추가
    folium.CircleMarker(
        location=[row["위도"], row["경도"]],
        radius=radius_size,
        tooltip=f"[{row['호선']}] {row['역명']}",  # 마우스 올릴 때: 호선 + 역명
        popup=f"이용객 수: {row['이용객수']:,}명",  # 클릭할 때: 이용객 수
        color=line_color,  # 테두리 색상
        fill=True,
        fill_color=line_color,  # 채우기 색상
        fill_opacity=0.6,
    ).add_to(m)

  # 5. 지도 출력
  st.subheader("🗺️ 역별 이용객 수 지도")
  st_folium(m, width=700, height=500)

  # 6. [표] 이용객 수 상위 5개 역 표시 (선택된 호선 기준)
  st.subheader("🏆 이용객 수 상위 5개 역")
  top5_df = filtered_df.sort_values(by="이용객수", ascending=False).head(5)

  # 순위 및 주요 컬럼만 정리해서 보여주기
