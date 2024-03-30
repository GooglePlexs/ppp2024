def get_range_list(n):

  if n>=1 :
    return list(range(1, n + 1))
  if n<1 :
    return list(range(n , 1 + 1))
  

def main():
  n = int(input("1부터 리스트가 종료되기 원하는 범위를 입력하시오"))
  range_list = get_range_list(n)
  print(f"1부터 {n}까지의 리스트: {range_list}")

if __name__ == "__main__":
  main()