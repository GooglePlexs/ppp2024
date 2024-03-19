import math

def menu():
    print("계산할 식을 선택하시오")
    print("1. 원의 길이")
    print("2. 원의 면적")

    choice = int(input("선택: "))
    return choice

def length(radius):
    return 2 * math.pi * radius

def area(radius):
    return math.pi * math.pow(radius,2) 

choice_fianl = menu()

if choice_fianl == 1:
    radius = float(input("원의 반지름을 입력하세요: "))
    print("원의 길이:{:.1f}".format(length(radius)))
elif choice_fianl == 2:
    radius = float(input("원의 반지름을 입력하세요: "))
    print("원의 면적:{:.2f}".format(area(radius)))
else:
    print("업데이트 예정입니다.")