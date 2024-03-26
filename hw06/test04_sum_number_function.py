def main():
  n = 0
  n = int(input("1부터 합산하기를 원하는 마지막 숫자를 기입하시오"))
  sum_n(n)


def sum_n(n):
  sum_n = 0
  for i in range(1, n + 1):
    sum_n += i
  print(f"1부터 {n}까지의 합산 값은 {sum_n}입니다")

if __name__ == "__main__":
  main()