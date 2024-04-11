def read_food_eat(filename):

  food_result = {}
  with open(filename) as f:
    lines = f.readlines()
    for line in lines[1:]:
      tokens = line.split(",")
      food_name = tokens[0]
      food_kcal = float(tokens[1])
      food_result[food_name] = food_kcal
    return food_result

def calculate_calories(food_result, food_name, eat_amount):

  food_kcal = food_result[food_name]
  return food_kcal * eat_amount / 100

def main():

  food_result = read_food_eat("hw10/calorie_db.csv")

  total_calories = 0

  while True:
    food_name = input("과일 이름 입력 (종료: q): ")
    if food_name == "q":
      break

    eat_amount = float(input("섭취량 (g) 입력: "))

    calories = calculate_calories(food_result, food_name, eat_amount)

    if calories > 0 :
      total_calories += calories


  print(f"총 칼로리: {total_calories:.1f}kcal")

if __name__ == "__main__":
  main()