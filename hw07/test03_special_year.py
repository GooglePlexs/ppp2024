def is_leap_year(year):

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
    print(f"{input_year}년은 윤년입니다.")
  else:
    print(f"{input_year}년은 윤년이 아닙니다.")

if __name__ == "__main__":
  main()