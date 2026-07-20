import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    import streamlit as st
    import pandas as pd
    import numpy as np
    from datetime import date
    from PIL import Image
    import io

    # 페이지 설정
    st.set_page_config(
        page_title='Streamlit 요소 예시',
        page_icon=':sparkles:',
        layout='wide',
    )

    st.title('Streamlit 요소 예시 페이지')
    st.subheader('하나의 단일 페이지에서 다양한 Streamlit 컴포넌트를 시연합니다')

    # 사이드바
    with st.sidebar:
        st.header('사이드바')
        user_name = st.text_input('이름', '사용자')
        show_map = st.checkbox('지도 표시', value=True)
        dataset_type = st.selectbox('샘플 데이터', ['시계열', '카테고리'])
        n = st.slider('샘플 행 수', 10, 1000, 200)
        st.markdown('---')
        st.write('예시 페이지')

    # 요약 메트릭
    col1, col2, col3 = st.columns(3)
    col1.metric('매출', '₩ 1,234,000', '+4.5%')
    col2.metric('활성 사용자', '3,210', '-1.2%')
    col3.metric('평균 세션 길이', '5m 12s', '+0.8%')

    # 차트 섹션
    st.header('차트')
    if dataset_type == '시계열':
        df = pd.DataFrame({
            'date': pd.date_range('2024-01-01', periods=n, freq='D'),
            'value': np.random.randn(n).cumsum() + 50,
        }).set_index('date')
        st.line_chart(df)
    else:
        cats = list('ABCDE')
        df = pd.DataFrame({
            'category': np.random.choice(cats, size=n),
            'value': np.random.randint(1, 100, size=n),
        })
        st.bar_chart(df.groupby('category').sum())

    # 데이터 미리보기
    st.header('데이터 미리보기')
    st.dataframe(df.head(10))
    st.table(df.head(5))

    # 지도 (무작위 좌표)
    if show_map:
        st.header('지도 (샘플 좌표)')
        map_df = pd.DataFrame(
            np.random.randn(100, 2) / [50, 50] + [37.55, 126.98],
            columns=['lat', 'lon'],
        )
        st.map(map_df)

    # 미디어
    st.header('미디어')
    img = Image.new('RGB', (320, 120), color=(73, 109, 137))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    st.image(buf, caption='생성된 예시 이미지', use_column_width=False)

    # 폼
    st.header('폼 및 입력')
    with st.form('sample_form'):
        age = st.number_input('나이', min_value=0, max_value=120, value=30)
        dob = st.date_input('생년월일', value=date(1990, 1, 1))
        fav_color = st.color_picker('좋아하는 색', '#00f900')
        agree = st.checkbox('약관 동의')
        submitted = st.form_submit_button('제출')
        if submitted:
            st.success(f'{user_name}님, 제출되었습니다.')
            st.write({'나이': age, '생년월일': str(dob), '색상': fav_color, '동의': agree})

    # 파일 업로더
    st.header('파일 업로드 (CSV)')
    uploaded = st.file_uploader('CSV 파일 업로드', type=['csv'])
    if uploaded is not None:
        uploaded_df = pd.read_csv(uploaded)
        st.write('업로드된 데이터 미리보기')
        st.dataframe(uploaded_df.head())

    # 탭과 확장 패널
    tab1, tab2 = st.tabs(['요약', '원본'])
    with tab1:
        st.write('이 탭은 요약 정보를 보여줍니다.')
    with tab2:
        st.code("""# 간단한 예시 코드
    print('Hello Streamlit')""")

    with st.expander('추가 정보'):
        st.write('여기에 상세 설명이나 참고 사항을 넣을 수 있습니다.')

    # 진행 표시
    st.header('진행 표시')
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    st.write('---')
    st.write('예시 페이지가 로드되었습니다. 필요하면 구성요소를 추가하겠습니다.')
            label=f'{country} GDP',
