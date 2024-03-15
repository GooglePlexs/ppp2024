import math
def calculate_circle_area(radius):
    return math.pow( radius, 2 ) * math.pi

radius = int(input("원의 반지름을 입력하십시오"))
circle_area = calculate_circle_area(radius)
print("반지름이 {}일 때,  원의 면적은 {}입니다".format(radius,circle_area))