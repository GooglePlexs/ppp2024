w = 60
h = 170
bmi = w / ( h * h ) * 10000
print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {}입니다.".format(h,w,bmi))

w = 60
h_cm = 170
h_m = h_cm / 100
bmi = w / ( h_m * h_m ) 
print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {}입니다.".format(h,w,bmi))

w = 60
h_cm = 170
h_m = h_cm / 100
bmi = w / ( h_m ** 2 ) 
print("키가 {}cm, 몸무게가 {}kg이면 BMI는 {}입니다.".format(h,w,bmi))