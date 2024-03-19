Hallabong_g = int(input("섭취한 한라봉의 중량를 입력하십시오(g단위)"))
strawberry_Seolhyang_g = int(input("섭취한 설향 품종 딸기의 중량를 입력하십시오(g단위)"))
banana_g = int(input("섭취한 바나나의 중량를 입력하십시오(g단위)"))

Hallabong = 0.5 * Hallabong_g
strawberry_Seolhyang = 0.34 * strawberry_Seolhyang_g
banana = 0.77 * banana_g

kcal = Hallabong + strawberry_Seolhyang + banana
print("섭취한 한라봉의 중량이 {}g, 설향 품종 딸기의 중량이 {}g , 바나나의 중량이 {}g 일 때 총 칼로리는 {}kcal입니다".format(Hallabong_g,strawberry_Seolhyang_g,banana_g,kcal))