import math

x1 = float(input("첫번째 점의 x좌표를 입력하시오"))
y1 = float(input("첫번째 점의 y좌표를 입력하시오"))
x2 = float(input("두번째 점의 x좌표를 입력하시오"))
y2 = float(input("두번째 점의 y좌표를 입력하시오"))

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if dist >= 1:
    print("거리는 {:.1f}입니다".format(dist))
    #f는 실수이며, 자리수 nf로 소수점 n개까지 출력한다
else:
    print("거리가 너무 근접합니다")

#print("거리는 {:8.3f}입니다".format(dist))
    #f는 실수이며, 자리수 nf로 소수점 n개까지 출력한다(자리수를 8개까지 채워야 함으로 실수4자리에 모자란 4자리를 띄어쓰기로 채운다)

