import streamlit as st

st.set_page_config(
    page_title='심지효 소개',
    page_icon='🌿',
    layout='wide',
)

st.markdown(
    """
    <style>
    .hero-box {
        background: linear-gradient(135deg, #f5f3ff 0%, #e8f2ff 100%);
        padding: 1.8rem 2rem;
        border-radius: 20px;
        border: 1px solid #dfe7ff;
        margin-bottom: 1rem;
    }
    .info-card {
        background: white;
        padding: 1rem 1.2rem;
        border-radius: 16px;
        border: 1px solid #eef2ff;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
        height: 100%;
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #3b4a67;
        margin-bottom: 0.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-box">
        <h1 style="margin-bottom:0.3rem;">안녕하세요, 저는 심지효입니다 👋</h1>
        <p style="font-size:1.05rem; color:#4b5563; margin:0;">
            역사 교사로서 학생들과 함께 생각하고 배우는 교육의 가치를 나누고 있습니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
col1.metric('직업', '역사 교사')
col2.metric('연락처', '010 0000 0000')
col3.metric('관심사', '교육 · 역사')

st.markdown('---')

left_col, right_col = st.columns([2, 1], gap='large')

with left_col:
    st.markdown(
        """
        <div class="info-card">
            <div class="section-title">소개</div>
            <p style="line-height:1.7; color:#374151; margin:0;">
                저는 역사 교육을 통해 사람들과 함께 생각하고 배울 수 있는 가치를 중요하게 여깁니다.
                단순히 지식을 전달하는 것을 넘어, 학생들이 역사 속에서 의미를 찾고 성장할 수 있도록 돕는 것이 목표입니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    st.markdown(
        """
        <div class="info-card">
            <div class="section-title">기본 정보</div>
            <ul style="padding-left: 1rem; color:#374151; line-height:1.8; margin:0;">
                <li>이름: 심지효</li>
                <li>직업: 역사 교사</li>
                <li>연락처: 010 0000 0000</li>
                <li>관심사: 교육, 역사, 소통</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('---')

with st.expander('더 알아보기', expanded=True):
    st.write('좋은 교육은 사람과 사람을 연결하는 힘이 있다고 믿습니다.')
    st.write('지속적으로 배우고 성장하는 자세로, 삶과 교육 모두에서 의미 있는 연결을 만들어가고 있습니다.')

st.success('학생들과 함께 성장하며, 역사와 교육의 가치를 나누는 사람입니다.')
