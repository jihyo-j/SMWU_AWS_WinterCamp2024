elif choose == "Fruit Recommendation":
        
            
        def strawberry_recommendation_test():
            
            recommendation = None
            NO_recommendation = None
            recommendations = []
            
            st.title("🍓 딸기추천🍓")

            messages = [
                "딸기 종류는 많은데...",
                "내가 찾는 딸기는 뭔지 모르겠다면?",
                "나에게 딱! 맞는 딸기를 추천해드립니다!"
            ]
            
            st.write("")
            st.write("")
            
            # 세 가지 문구를 1초 간격으로 표시
            for msg in messages:
                st.write(msg)
                time.sleep(1)
            st.write("--------")
            
            # 단맛에 대한 선택
            sweet_preference = None  # 변수를 미리 정의합니다.
            sour_preference = None
            intensity_preference = None
            
            col1, col2, col3 = st.columns(3)
            
            # 맞춤 취향 별 선택지

            # 단맛에 대한 선택
            with col1:
                st.subheader("당도")
                sweet_preference = st.radio("", (None, '보통', '상', '최상'), key='sweet_preference')
            
            # 신맛에 대한 선택
            with col2:
                st.subheader("산미")
                sour_preference = st.radio("", (None, '약함', '보통', '강함'), key='sour_preference')
            
            # 경도에 대한 선택
            with col3:
                st.subheader("경도")
                intensity_preference = st.radio("", (None, '부드러움','단단함'), key='intensity_preference')
                
            recommendation = None
            NO_recommendation = None
            recommendations = []

            # 하나라도 선택되지 않은 경우 알림 표시
            if sweet_preference is None or sour_preference is None or intensity_preference is None:
                st.warning("각 문항마다 하나의 선택지를 선택해주세요.")
                return
            
            
            st.write("--------")

            # 모든 가능한 딸기 종류 결정
            if sweet_preference == '상'  and sour_preference == '약함' and intensity_preference =='단단함':
                recommendations.extend(['금실', '메리퀸'])
            elif sweet_preference == '최상'  and sour_preference == '보통' and intensity_preference =='단단함':
                recommendations.append('죽향')
            elif sweet_preference == '상'  and sour_preference == '약함' and intensity_preference =='부드러움':
                recommendations.append('장희')
            elif sweet_preference == '상'  and sour_preference == '보통' and intensity_preference =='부드러움':
                recommendations.extend(['만년설', '옐로우글램'])
    
            elif sweet_preference == '보통'  and sour_preference == '보통' and intensity_preference =='단단함':
                recommendations.extend(['아리향', '비타베리'])
            elif sweet_preference == '보통'  and sour_preference == '보통' and intensity_preference =='부드러움':
                recommendations.extend(['설향', '킹스베리'])
            elif sweet_preference == '보통' and sour_preference == '강함' and intensity_preference =='부드러움':
                recommendations.append('골든벨')
            elif sweet_preference == '보통' and sour_preference == '강함' and intensity_preference =='단단함':
                recommendations.append('육보')
            elif sweet_preference == '상' and sour_preference == '보통' and intensity_preference =='단단함':
                recommendations.append('샤이투')
        
            else:
                st.write("")
                st.write("")
                NO_recommendation = st.subheader("새로운 취향의 탄생! \n 아쉽게도 아직 조건에 맞는 딸기가 나오지 않았어요💫")
    
            # 모든 추천 딸기에 대한 이미지와 설명 추가
            if recommendations:
                for recommendation in recommendations:
                    st.subheader(f"추천하는 딸기 종류는 '{recommendation}'입니다.")
            
                    ## 딸기 종류

                    else:
                        st.write("")
                        st.write("")
                        NO_recommendation = st.subheader("새로운 취향의 탄생! \n 아쉽게도 아직 조건에 맞는 딸기가 나오지 않았어요💫")
                
        def grape_recommendation_test():
            st.title("🍇 포도추천🍇")

            messages = [
                "포도 종류는 많은데...",
                "내가 찾는 포도는 뭔지 모르겠다면?",
                "나에게 딱! 맞는 포도를 추천해드립니다!"
            ]
            
            st.write("")
            st.write("")
            
            for msg in messages:
                st.write(msg)
                time.sleep(1)
            st.write("--------")
            
            # 가로로 선택지를 나열하기 위해 columns 레이아웃 사용
            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("당도")
                sweet_preference = st.radio("", (None, '보통', '상', '최상'), key='sweet_preference')

            with col2:
                st.subheader("산미")
                sour_preference = st.radio("", (None, '약함', '보통', '강함'), key='sour_preference')

            with col3:
                st.subheader("껍질")
                peel_preference = st.radio("", (None, '껍질째 먹을래요','껍질은 빼고 먹을래요'), key='peel_preference')



            recommendation = None
            NO_recommendation = None
            recommendations = []

            # 하나라도 선택되지 않은 경우 알림 표시
            if sweet_preference is None or sour_preference is None or peel_preference is None:
                st.warning("각 문항마다 하나의 선택지를 선택해주세요.")
                return
            
            st.write("--------")
            
            if sweet_preference == '상'  and sour_preference == '보통' and peel_preference =='껍질은 빼고 먹을래요':
                recommendations.extend(['거봉', '흑보석'])
            elif sweet_preference == '보통'  and sour_preference == '보통' and peel_preference =='껍질은 빼고 먹을래요':
                recommendations.append('캠벨포도')
                
            elif sweet_preference == '상'  and sour_preference == '약함' and peel_preference =='껍질은 빼고 먹을래요':
                recommendations.append('충랑포도')
            elif sweet_preference == '보통'  and sour_preference == '약함' and peel_preference =='껍질은 빼고 먹을래요':
                recommendations.append('진옥')
     
            elif sweet_preference == '상'  and sour_preference == '강함' and peel_preference =='껍질째 먹을래요':
                recommendations.append('스텔라')    
            elif sweet_preference == '최상'  and sour_preference == '약함' and peel_preference =='껍질째 먹을래요':
                recommendations.extend(['마이하트포도', '블랙사파이어'])
            elif sweet_preference == '최상'  and sour_preference == '강함' and peel_preference =='껍질째 먹을래요':
                recommendations.append('홍주씨들리스')
            elif sweet_preference == '상' and sour_preference == '보통' and peel_preference =='껍질째 먹을래요':
                recommendations.append('슈팅스타')
            elif sweet_preference == '최상' and sour_preference == '보통' and peel_preference =='껍질째 먹을래요':
                recommendations.append('골드스위트')
            elif sweet_preference == '상' and sour_preference == '약함' and peel_preference =='껍질째 먹을래요':
                recommendations.append('루비스위트')
            elif sweet_preference == '보통' and sour_preference == '강함' and peel_preference =='껍질째 먹을래요':
                recommendations.append('레드클라렛')
        
            # 나머지 조건들 추가

            if recommendations:
                for recommendation in recommendations:
                    st.subheader(f"추천하는 포도 종류는 '{recommendation}'입니다.")
                    # 각 포도에 대한 설명 추가
                    
                    ##포도 종류

            else:
                st.write("")
                st.write("")
                NO_recommendation = st.subheader("새로운 취향의 탄생! \n 아쉽게도 아직 조건에 맞는 포도가 나오지 않았어요💫")
                
        def peach_recommendation_test():
            st.title("🍑 복숭아 추천 🍑")

            messages = [
                "복숭아 종류는 많은데...",
                "내가 찾는 복숭아는 뭔지 모르겠다면?",
                "나에게 딱! 맞는 복숭아를 추천해드립니다!"
            ]
            

            # 세 가지 문구를 1초 간격으로 표시
            for msg in messages:
                st.write(msg)
                time.sleep(1)
            st.write("--------")
                
            # 맞춤 취향 별 선택지
            # 가로로 선택지를 나열하기 위해 columns 레이아웃 사용
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.subheader("당도")
                sweet_preference = st.radio("", (None, '보통', '상', '최상'), key='sweet_preference')

            with col2:
                st.subheader("산미")
                sour_preference = st.radio("", (None, '약함', '보통', '강함'), key='sour_preference')

            with col3:
                st.subheader("경도")
                intensity_preference = st.radio("", (None, '말랑', '중간','단단'), key='intensity_preference')

            recommendation = None
            NO_recommendation = None
            recommendations = []

            # 하나라도 선택되지 않은 경우 알림 표시
            if sweet_preference is None or sour_preference is None or intensity_preference is None:
                st.warning("각 문항마다 하나의 선택지를 선택해주세요.")
                return
            
            st.write("--------")
            
            # 모든 가능한 복숭아 종류 결정
            if sweet_preference == '보통'  and sour_preference == '강함' and intensity_preference =='말랑':
                recommendations.extend(['신황도', '썬프레'])
            elif sweet_preference == '최상'  and sour_preference == '약함' and intensity_preference =='말랑':
                recommendations.append('레드골드')
            elif sweet_preference == '최상'  and sour_preference == '보통' and intensity_preference =='말랑':
                recommendations.append('용궁백도')
            elif sweet_preference == '상'  and sour_preference == '보통' and intensity_preference =='말랑':
                recommendations.append('미백도')
            elif sweet_preference == '보통'  and sour_preference == '하' and intensity_preference =='말랑':
                recommendations.append('용성황도')
        
            elif sweet_preference == '상'  and sour_preference == '보통' and intensity_preference =='중간':
                recommendations.append('그레이트')
            elif sweet_preference == '최상'  and sour_preference == '강함' and intensity_preference =='중간':
                recommendations.append('아까즈끼 ER') 
            elif sweet_preference == '보통'  and sour_preference == '약함' and intensity_preference =='중간':
                recommendations.append('용성황도') 
            elif sweet_preference == '상'  and sour_preference == '약함' and intensity_preference =='중간':
                recommendations.append('납작복숭아') 
            elif sweet_preference == '상'  and sour_preference == '강함' and intensity_preference =='중간':
                recommendations.append('엘바트') 
        
            elif sweet_preference == '상'  and sour_preference == '보통' and intensity_preference =='단단':
                recommendations.extend(['황귀비','천도'])
            elif sweet_preference == '보통'  and sour_preference == '강함' and intensity_preference =='단단':
                recommendations.append('대명')
            elif sweet_preference == '최상'  and sour_preference == '약함' and intensity_preference =='단단':
                recommendations.append('만천하')     
        
            
            # 모든 추천 복숭아에 대한 이미지와 설명 추가
            if recommendations:
                for recommendation in recommendations:
                    st.subheader(f"추천하는 복숭아 종류는 '{recommendation}'입니다.")
            
                    ##복숭아 종류
                
            else:
                st.write("")
                st.write("")
                NO_recommendation = st.subheader("새로운 취향의 탄생! \n 아쉽게도 아직 조건에 맞는 복숭아가 나오지 않았어요💫")
        

        if __name__ == '__main__':
            st.header('과일을 선택하세요')
            fruit_choice = st.selectbox(' ', ("선택하세요!","🍓 딸기", "🍇 포도", "🍑 복숭아"))
            st.write("--------")
            
            if fruit_choice == "🍓 딸기":
                strawberry_recommendation_test()
            elif fruit_choice == "🍇 포도":
                grape_recommendation_test()
            elif fruit_choice == "🍑 복숭아":
                peach_recommendation_test()