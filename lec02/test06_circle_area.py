import math

r = int(input("원의 반지름을 입력하시오."))
circle_area = r**2 * math.pi
print("반지름이 {}일 때, 원의 면적은 {}입니다".format(r,circle_area))