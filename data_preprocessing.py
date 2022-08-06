import pandas as pd
# 변수명은 일단 알아보기 쉽게 최대한 풀어서 작성함!
# 본인의 취향 것 수정하여 사용할 것

# 해당 전처리는 train.csv의 결측치를 모두 제거한 데이터로 test.csv에는 이와 같은 방법으로 학습하면 곤란하다.

# train set ver
# 데이터 가져오기
train_data = pd.read_csv("train.csv")  # 해당 상대경로는 본인의 작업환경에 따라 유동적으로 변경해 주세요
train_data_drop = train_data.dropna()

# 데이터 쪼개기 => 결측치 제거한 값으로

# feature data
idx1to26_drop = train_data_drop.iloc[:, 1:27]
idx28to40_drop = train_data_drop.iloc[:, 28:41]
idx41to56_drop = train_data_drop.iloc[:, 41:57]
idx57to68_drop = train_data_drop.iloc[:, 57:69]

# target data
target_drop = train_data_drop.iloc[:, 69]

# test.csv에 대한 전처리는 일단 평균값으로 대체하여 결측치를 보완하였다.
# 다른 방식으로 결측치를 보완하고 싶다면 pd 의 다른 함수를 이용하면 된다.

# test set ver
# 데이터 가져오기
test_data = pd.read_csv("test.csv")
test_data_rpm = test_data.fillna(test_data.mean())


# 데이터 쪼개기 => 결측치를 평균으로 대체한 값으로

# feature data
idx1to26_rpm = test_data_rpm.iloc[:, 1:27]
idx28to40_rpm = test_data_rpm.iloc[:, 28:41]
idx41to56_rpm = test_data_rpm.iloc[:, 41:57]
idx57to68_rpm = test_data_rpm.iloc[:, 57:69]

# test_data 에는 target data가 없다.

# 제출 파일 생성
submission = pd.read_csv('sample_submission.csv')
# submission["nerdiness"] = 모델이 예측한 값 변수

# 생성된 CSV 파일 저장하는 코드
# 코랩에서 작업시 작업 디렉터리에 생성되며 이를 로컬로 다운 받아 제출을 해 주어야 한다.
# submission.to_csv("baseline.csv", index = False)