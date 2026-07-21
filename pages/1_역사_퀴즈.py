import streamlit as st

st.set_page_config(page_title='역사 퀴즈', page_icon='📜')

st.title('📜 한국사 미니 퀴즈')
st.write('역사 교사가 내는 3문제! 몇 개나 맞힐 수 있을까요?')

score = 0

q1 = st.radio('1. 훈민정음을 창제한 왕은?', ['태종', '세종대왕', '정조', '광해군'])
if q1 == '세종대왕':
    score += 1
q2 = st.radio('2. 임진왜란 때 거북선으로 활약한 장군은?', ['강감찬', '을지문덕', '이순신', '김유신'])
if q2 == '이순신':
    score += 1
q3 = st.radio('3. 3·1 운동이 일어난 해는?', ['1897년', '1910년', '1919년', '1945년'])
if q3 == '1919년':
    score += 1
if st.button('채점하기 🚀', type='primary'):
    st.metric('내 점수', f'{score} / 3')
    if score == 3:
        st.balloons()
        st.success('만점! 정말 대단해요! 👑')
