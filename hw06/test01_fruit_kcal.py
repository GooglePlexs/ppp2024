def calculate_calories(calories, fruits):

  total_calories = 0

  for fruit, kcal in calories.items():
    if fruit in fruits:
      total_calories += kcal * fruits[fruit]

  return total_calories


calories = {"한라봉": 50,"딸기": 34,"바나나": 77,"사과": 57,"포도": 60,}


hallabong_eat = int(input("섭취한 한라봉의 양을 기입하시오(100g 단위): "))
strawberry_eat = int(input("섭취한 딸기의 양을 기입하시오(100g 단위): "))
banana_eat = int(input("섭취한 바나나의 양을 기입하시오(100g 단위): "))
apple_eat = int(input("섭취한 사과의 양을 기입하시오(100g 단위): "))
grape_eat = int(input("섭취한 포도의 양을 기입하시오(100g 단위): "))

fruits = {
  "한라봉": hallabong_eat,
  "딸기": strawberry_eat,
  "바나나": banana_eat,
  "사과": apple_eat,
  "포도": grape_eat,
}

def main():
  total_calories = calculate_calories(calories, fruits)
  print(f"총 섭취 칼로리: {total_calories}kcal")

if __name__ == "__main__":
  main()