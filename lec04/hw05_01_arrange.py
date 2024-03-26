import math

in_number = int(input("계산할 구구단의 단을 입력하세요"))



for i in range(1, 9 + 1 ):
    print(f"{in_number} * {i} = {in_number * i:2d}")
#print 문에서는 m과 n을 곱한 결과의 자리수를 맞추려고


#for i in range(9):
#n = i+1
#print(f"{in_number} * {n} = {in_number * n}")


#for i in range(9):
#    print(f"{in_number} * {i+1} = {in_number * (i+1):2d}")