import math
def calculate_bmi_point(weight,height_m):
    return weight / math.pow (height_m , 2)

height_cm = float(input("신장을 입력하십시오 (cm기준)"))
weight = float(input("몸무게를 입력하십시오 (kg기준)"))

height_m = height_cm / 100
bmi = calculate_bmi_point(weight,height_m)

if bmi < 18.5:
    print(print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {:.1f}이며 저체중입니다.".format(height_cm,weight,bmi)))
elif bmi <23:
    print(print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {:.1f}이며 표준체형입니다.".format(height_cm,weight,bmi)))
elif bmi <25:
    print(print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {:.1f}이며 비만 전단계입니다.".format(height_cm,weight,bmi)))
elif bmi <30:
    print(print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {:.1f}이며 1단계 비만입니다.".format(height_cm,weight,bmi)))
elif bmi <35:
    print(print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {:.1f}이며 2단계 비만입니다.".format(height_cm,weight,bmi)))
else:
    print(print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {:.1f}이며 3단계 비만입니다.".format(height_cm,weight,bmi)))




#elif bmi >35:
#    print(print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {}이며 3단계 비만입니다.".format(height_cm,weight,bmi)))
