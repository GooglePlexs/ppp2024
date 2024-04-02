def total_calorie(fruits_eat,fruits_calorie_dic):

  # 방법 1
  #total = 0
  #for fruit_name in fruits_eat:
  #  # print(fruit_name)
  #  total += fruit_eat[fruits_name] * fruits_calorie_dic[fruits_name] / 100
  #return total

  # 방법 2
  #total = 0
  #for fruit_name, fruit_gram in fruits_eat.items():
  #  total += fruit_gram * fruits_calorie_dic[friut_name] / 100 
  #return total

  # 방법 3
  return [ gram * fruits_calorie_dic[name] / 100 for name, gram in fruits_eat.items() ]

def main():
  fruits_calorie_dic = {"한라봉": 50, "딸기": 34, "바나나": 77}
  fruits_mon = {"딸기": 300, "한라봉": 150}
  print(total_calorie(fruits_mon,fruits_calorie_dic))

  fruits_wed = {"딸기": 200, "바나나": 300}
  print(total_calorie(fruits_wed,fruits_calorie_dic))

if __name__ == "__main__":
  main()