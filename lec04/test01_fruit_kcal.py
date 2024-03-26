eat_fruit = "딸기"
eat_gram = 20

cal = {"한라봉": 0.5,"딸기" : 0.34, "바나나" : 0.77, "사과" : 0.57}

total_cal = 0

for fruit in cal:
    if eat_gram == fruit:
        total_cal = cal[fruit] * eat_gram

print(f"총 칼로리는 {total_cal}입니다.")