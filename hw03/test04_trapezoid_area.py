high_line = int(input("윗변의 길이를 입력하십시오"))
low_line  = int(input("아랫변의 길이를 입력하십시오"))
height    = int(input("높이를 입력하십시오"))
trapezoid_area = ((high_line + low_line) / 2) * height 
print("윗변이 {}, 아랫변이 {}, 높이가 {}일 때 사다리꼴의 면적은 {}입니다.".format(high_line,low_line,height,trapezoid_area))