"""
1.3.1 지도 학습과 비지도 학습
머신러닝 시스템을 ‘학습하는 동안의 감독 형태나 정보량’에 따라 분류할 수 있습니다.
지도 학습, 비지도 학습, 준지도 학습, 강화 학습 등 네 가지 주요 범주가 있습니다.

지도 학습
지도 학습supervised learning에는 알고리즘에 주입하는 훈련 데이터에
레이블label 3이라는 원하는 답이 포함됩니다(그림 1-5).


분류classification가 전형적인 지도 학습 작업이며, 스팸 필터가 좋은 예입니다.
스팸 필터는 많은 메일 샘플과 소속 정보(스팸인지 아닌지)로 훈련되어야 하며
어떻게 새 메일을 분류할지 학습해야 합니다.

또 다른 전형적인 작업은 예측 변수predictor variable라 부르는
특성feature (주행거리, 연식, 브랜드 등)을
사용해 중고차 가격 같은 타깃 수치를 예측하는 것입니다.
이런 종류의 작업을 회귀regression 4라고 부릅니다(그림 1-6).
시스템을 훈련시키려면 예측 변수와 레이블(중고차 가격)이 포함된
중고차 데이터가 많이 필요합니다.

일부 회귀 알고리즘은 분류에 사용할 수도 있고 또 반대의 경우도 있습니다.
예를 들어 분류에 널리 쓰이는 로지스틱 회귀는 클래스에
속할 확률을 출력합니다(예를 들면 스팸일 가능성 20 %).

지도 학습 알고리즘

k-최근접 이웃k-Nearest Neighbors
선형 회귀Linear Regression
로지스틱 회귀Logistic Regression
서포트 벡터 머신Support Vector Machines (SVM)
결정 트리Decision Tree와 랜덤 포레스트Random Forests
신경망Neural networks 6
"""