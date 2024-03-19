x = float(input("해당 점의 x좌표를 입력하십시오"))
y = float(input("해당 점의 y좌표를 입력하십시오"))

if x>0 and y>0 :
    print("해당 점의 위치는 1사분면 입니다")
elif x<0 and y>0 :
    print("해당 점의 위치는 2사분면 입니다")
elif x<0 and y<0 :
    print("해당 점의 위치는 3사분면 입니다")
elif x>0 and y<0 :
    print("해당 점의 위치는 4사분면 입니다")
else:
    print("해당 점은 특정 사분면에 존재하지 않으므로 올바른 점을 입력해주시기 바랍니다.")



