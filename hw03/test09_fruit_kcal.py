def calculate_calories(calories, eat_hallabong, eat_strawberry, eat_banana):

  for fruit, fruit_calories in calories.items():
    if fruit == "한라봉":
      total_calories_hallabong = fruit_calories * eat_hallabong
    elif fruit == "딸기":
      total_calories_strawberry = fruit_calories * eat_strawberry 
    elif fruit == "바나나":
      total_calories_banana = fruit_calories * eat_banana 

  total_calories = total_calories_hallabong + total_calories_strawberry + total_calories_banana

  return total_calories

calories = {"한라봉": 50,"딸기": 34,"바나나": 77}

eat_hallabong = int(input("섭취한 한라봉의 양을 기입하시오(100g 단위)"))
eat_strawberry = int(input("섭취한 딸기의 양을 기입하시오(100g 단위)"))
eat_banana = int(input("섭취한 바나나의 양을 기입하시오(100g 단위)"))

total_calories = calculate_calories(calories, eat_hallabong, eat_strawberry, eat_banana)

print("총 섭취 칼로리: {}kcal".format(total_calories))