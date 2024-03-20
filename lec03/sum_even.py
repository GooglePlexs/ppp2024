# 1-250까지의 짝수합

n=250

total = 0

for i in range(n):
    if (i+1) % 2 == 0:
        total = total + (i+1)
    if (i+1) % 2 == 1:
        total = total 

print(f"1부터 {n}까지의 합계는 {total:,}입니다.")
# :,을 통해 100단위로 표시해줌
