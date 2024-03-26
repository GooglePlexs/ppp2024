n = 5

for i in range(n):
    star = i + 1
    print("*" * star)


#for i in range(n):
#    for j in range(i+1):
#        print("*" , end="") # "*" => 별을 한개만 출력 , end="" => ""가 나올때마다 줄바꿈 하지 말것(C언어 등)
#    print()

for i in range(n):
    num_star = i+1
    num_space = n - num_star
    print(" " * num_space + "*" * num_star)

#for i in range(n):
#    print(' '*(n-i-1) + "*" * (i+1)*2)
    
#for i in range(n):
#    print(' '*(n-i-1) + "*" * ((i+1)*2-1))