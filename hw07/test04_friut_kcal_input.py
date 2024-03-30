def total_calorie(fruits, fruits_calorie_dic):

  total_calories = 0

  for fruit, weight in fruits.items():
    if fruit in fruits_calorie_dic:
      total_calories += fruits_calorie_dic[fruit] * weight / 100
    else:
      print(f"해당 과일이 정보에 없습니다.")

  return total_calories

def main():
  fruits = {"딸기": 300, "한라봉": 150}
  fruits_calorie_dic = {"한라봉": 50, "딸기": 34, "바나나": 77}
  
  total_calories = total_calorie(fruits, fruits_calorie_dic)
  
  print(f"총 칼로리는 {total_calories:.0f} kcal입니다")

if __name__ == "__main__":
  main()