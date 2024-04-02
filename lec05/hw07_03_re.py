def is_leap_year(year): #is함수는 True / False로 같이출력되기를 바람

  if year % 4 == 0:
    if year % 100 == 0:
      return False
    else:
      return True
  else:
    return False

def main():
  input_year = int(input("계산하기를 원하는 년도를 입력하시오"))

  if is_leap_year(input_year):
    print(f"True")
  else:
    print(f"False")


if __name__ == "__main__":
  main()