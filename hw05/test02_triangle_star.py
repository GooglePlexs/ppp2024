#직각삼각형
def print_triangle(n):
  for i in range(1,n+1):
    print("*" * i)
    
n = int(input("삼각형의 높이를 입력하시오"))
print_triangle(n)


# 마지막에 none이 출력
# def print_triangle(n):
#   for i in range(1,n+1):
#     print("*" * i)
    
# n = int(input("삼각형의 높이를 입력하시오"))
# star = print_triangle(n)
# print(f"{star}")