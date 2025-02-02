import streamlit as st

# 🎨 웹앱 제목
st.title('💡 나의 첫 스트림릿 MBTI 웹앱')
st.subheader('📌 당신의 MBTI 유형을 입력하고 맞춤 해석을 받아보세요!')

# 📝 사용자 입력 받기
name = st.text_input('✍️ 이름을 입력해주세요:')
mbti_types = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP'
]
mbti = st.selectbox('🔍 MBTI를 선택해주세요', mbti_types)

# MBTI 설명 데이터
mbti_descriptions = {
    "INTJ": "전략적인 사고를 가진 개척자 🚀
    - 독립적이고 분석적이며 높은 목표를 지향합니다.
    - 깊이 있는 사고를 통해 장기적인 계획을 세우는 능력이 뛰어납니다.",
    
    "INTP": "논리적이고 창의적인 철학자 🧠
    - 복잡한 문제 해결을 즐기며 지적 탐구를 좋아합니다.
    - 규칙에 얽매이기보다는 새로운 개념을 탐색하는 것을 선호합니다.",
    
    "ENTJ": "대담한 리더 💼
    - 강한 카리스마와 리더십을 갖춘 전략적 사고가 뛰어난 유형입니다.
    - 목표를 달성하기 위해 적극적으로 계획을 수립하고 실행합니다.",
    
    "ENTP": "도전적이고 재치 있는 발명가 ⚡
    - 끊임없이 새로운 아이디어를 창출하고 토론을 즐깁니다.
    - 전통적인 틀을 깨고 혁신을 이끄는 성향이 강합니다.",
    
    "INFJ": "통찰력 있는 이상주의자 ✨
    - 깊은 공감 능력을 바탕으로 세상을 더 나은 곳으로 만들고자 합니다.
    - 타인의 감정을 세심하게 이해하며, 조용한 카리스마가 돋보입니다.",
    
    "INFP": "감성적인 몽상가 🌿
    - 내면의 가치와 감정을 중시하며 창의적인 표현을 좋아합니다.
    - 의미 있는 삶을 추구하고, 사람들에게 영감을 주는 존재입니다.",
    
    "ENFJ": "타인을 이끄는 따뜻한 리더 💖
    - 사람들과의 관계를 중요하게 여기며, 자연스럽게 이끌어 가는 역할을 합니다.
    - 협력과 조화를 중시하며, 사회적 영향력을 발휘하는 것을 즐깁니다.",
    
    "ENFP": "자유로운 영혼의 활동가 🌈
    - 열정적이고 창의적이며, 항상 새로운 가능성을 탐색하는 유형입니다.
    - 즉흥적이면서도 깊은 감성을 지닌 낙천적인 성향이 있습니다.",
    
    "ISTJ": "책임감 강한 실용주의자 📚
    - 체계적이고 논리적인 사고를 바탕으로 신뢰받는 존재입니다.
    - 원칙과 규칙을 준수하며, 계획적인 삶을 선호합니다.",
    
    "ISFJ": "헌신적인 수호자 🛡️
    - 따뜻한 마음과 세심한 배려로 주변 사람을 챙깁니다.
    - 충성심이 강하고 조용하지만 강한 의지를 가지고 있습니다.",
    
    "ESTJ": "냉철한 관리자 🏛️
    - 현실적이며 조직적이고 효율성을 중시하는 리더입니다.
    - 강한 책임감을 바탕으로 목표를 달성하는 데 집중합니다.",
    
    "ESFJ": "사교적인 조정자 🎭
    - 친절하고 사려 깊으며, 사람들과 조화를 이루는 것을 중요하게 여깁니다.
    - 공동체 안에서 사람들을 이끄는 데 뛰어난 재능이 있습니다.",
    
    "ISTP": "유연한 문제 해결사 🛠️
    - 현실적이고 분석적인 사고를 갖춘 실용적인 성향입니다.
    - 직접 경험하면서 배우는 것을 좋아하고 즉흥적인 성향이 있습니다.",
    
    "ISFP": "예술적인 탐험가 🎨
    - 감성적이면서도 실용적이며, 예술적 표현을 즐깁니다.
    - 주변 환경과 조화를 이루며 자유롭게 살아가는 것을 선호합니다.",
    
    "ESTP": "모험을 즐기는 사업가 🚴
    - 대담하고 즉흥적이며, 빠른 판단력으로 상황을 해결하는 유형입니다.
    - 경쟁을 즐기며, 현실적인 방식으로 목표를 달성하는 능력이 뛰어납니다.",
    
    "ESFP": "에너지가 넘치는 연예인 🎤
    - 사교적이고 활발하며, 주변을 밝게 만드는 존재입니다.
    - 새로운 경험을 즐기고 즉흥적인 삶을 살아갑니다."
}

# 💡 버튼 클릭 시 결과 출력
if st.button('🔍 MBTI 해석 보기'):
    if name and mbti:
        st.success(f'✨ {name}님, 당신은 {mbti} 유형입니다!')
        st.markdown(mbti_descriptions[mbti])
        st.balloons()  # 풍선 애니메이션 효과 추가 🎈
    else:
        st.warning('⚠️ 이름과 MBTI를 모두 입력해주세요!')
