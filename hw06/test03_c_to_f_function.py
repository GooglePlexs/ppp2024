def main():
  t_c = int(input("계산할 섭씨 온도를 입력하시오"))
  c2f(t_c)

def c2f(t_c):
  t_f=0
  t_f= t_c*(9/5) + 32
  print(f"섭씨 {t_c} 도는 화씨 {t_f:.0f} 도 입니다.")

if __name__ == "__main__":
  main()