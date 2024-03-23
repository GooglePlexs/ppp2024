import math

in_number = int(input("계산할 구구단의 단을 입력하세요"))

for i in range(9):
    print(f"{in_number} * {i+1} = {in_number * (i+1)}")