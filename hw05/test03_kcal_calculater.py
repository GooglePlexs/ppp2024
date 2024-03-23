# 조건 : 반복문과 사전(딕셔너리)을 활용하여 칼로리 계산 프로그램(과제#04-03)(test03_fruit_kcal.py)을 수정하여, 총 칼로리를 계산하시오
# 난이도가 높아 3월20일 수업 때 과제에서 제외한다고 하셨음
# 나중에 할 수 있을거 같으면 풀어보기

foods = []
calorie = []

while True:
  food_name = input("음식 이름을 입력하세요 (종료: exit): ")
  if food_name == "exit":
    break
  
  calories = int(input("칼로리를 입력하세요: "))
  
  foods.append(food_name)
  calories.append(calorie)