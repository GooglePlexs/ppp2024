# temp_C = 30
# temp_F= temp_C*(9/5) + 32
# print("섭씨 {}도는 화씨 {}도 입니다".format(temp_C,temp_F))

weight = int(input("몸무게를 입력하십시오 (kg기준)"))
height_m = int(input("신장을 입력하십시오 (cm기준)"))
height_cm = height_m / 100
bmi = weight / (height_cm ** 2)
print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {}입니다.".format(height_m,weight,bmi))

# weight = int(input("몸무게를 입력하십시오 (kg기준)"))
# height_m = int(input("신장을 입력하십시오 (cm기준)"))
# height_cm = height_m / 100
# bmi = weight // (height_cm ** 2)
# print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {}입니다.".format(height_m,weight,bmi))