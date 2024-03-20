# 1-100까지의 합

total = 0

for i in range(100):
    total = total + (i+1)

print(f"1부터 100까지의 합계는 {total}입니다.")


# 1-n까지의 합

n=250

total = 0

for i in range(n):
    total = total + (i+1)

print(f"1부터 {n}까지의 합계는 {total:,}입니다.")
# :,을 통해 100단위로 표시해줌



