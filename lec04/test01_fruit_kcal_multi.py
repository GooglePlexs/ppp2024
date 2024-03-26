eat_fruits = ["딸기","사과"]
eat_grams = [50,100]


cal = {"한라봉": 0.5,"딸기" : 0.34, "바나나" : 0.77, "사과" : 0.57}

total_cal = 0
index = 0

for eat_fruit in eat_fruits:
    for eat_fruit in cal:
        if eat_fruits == eat_fruit:
            total_cal = cal[eat_fruits] * eat_grams[index]
    index += 1

print(f"총 칼로리는 {total_cal}입니다.")
# 이거 왜 안됨?????



#eat_friuts_dic = {}
#total_cal = 0
#for eat_fruit,eat_gram in eat_fruits_dic.items():
#    for fruit in cal:
#        if eat_grams == fruit:
#            total_cal = cal[fruit] * eat_grams

#print(f"총 칼로리는 {total_cal}입니다.")