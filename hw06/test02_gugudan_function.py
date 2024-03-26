def main():
  dan = int(input("출력하고 싶은 단을 입력하세요: "))
  gugudan(dan)

def gugudan(dan):
  for i in range(9):
    print(f"{dan} * {i+1} = {dan * (i+1)}")

if __name__ == "__main__":
  main()