# 🚇 부산 지하철 역별 이용객 수 지도 분석 앱 (Busan Subway Map Analysis)

Streamlit과 Folium을 활용하여 부산 지하철 역별 이용객 수를 지도에 시각화하고 분석할 수 있는 Interactive Web App입니다.

---

## 📌 주요 기능 (Features)

1. **CSV 데이터 업로드**: `busan_subway.csv` 파일 업로드 및 데이터 확인
2. **호선별 필터링**: `Multiselect` 필터를 통해 원하는 호선(1~4호선 등)만 지도에 표시
3. **이용객 수 시각화**: 
   - 이용객 수의 제곱근($\sqrt{N}$) 비율로 원의 면적(반지름)을 자동 조절하여 시각적 직관성 제공
   - **호선별 테마 색상 적용** (1호선: 주황, 2호선: 초록, 3호선: 갈색, 4호선: 파랑)
4. **인터랙티브 마커**:
   - **Hover (마우스 오버)**: 호선 및 역명 표시
   - **Click (클릭)**: 정확한 이용객 수 (천 단위 쉼표 표기) 팝업 출력
5. **상위 역 데이터 제공**: 선택된 호선 내 이용객 수 **Top 5 역** 표 제공

---

## 📁 데이터 형식 (Data Format)

앱을 실행하기 위해 필요한 CSV 파일(`busan_subway.csv`)의 열 구성은 다음과 같아야 합니다.

| 호선 | 역명 | 위도 | 경도 | 이용객수 |
| :--- | :--- | :--- | :--- | :--- |
| 1호선 | 서면 | 35.1577 | 129.0591 | 65000 |
| 2호선 | 해운대 | 35.1631 | 129.1586 | 42000 |

---

## 🛠️ 설치 및 실행 방법 (Setup & Run)

### 1. Repository 클론 (Clone)
```bash
git clone https://github.com/사용자이름/저장소이름.git
cd 저장소이름
```

### 2. 패키지 설치 (Requirements)
```bash
pip install -r requirements.txt
```

### 3. Streamlit 앱 실행 (Run App)
```bash
streamlit run app.py
```

---

## 💡 사용 기술 스택 (Tech Stack)

- **Python** 3.x
- **Streamlit** (웹 인터페이스 구축)
- **Pandas** (데이터 전처리 및 분석)
- **Folium & Streamlit-Folium** (지도 데이터 시각화)