import math
def calculate_bmi_point(weight,height_cm):
    return weight / math.pow (height_cm , 2)

height_m = int(input("신장을 입력하십시오 (cm기준)"))
weight = int(input("몸무게를 입력하십시오 (kg기준)"))

height_cm = height_m / 100
bmi = calculate_bmi_point(weight,height_cm)
print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {}입니다.".format(height_m,weight,bmi))