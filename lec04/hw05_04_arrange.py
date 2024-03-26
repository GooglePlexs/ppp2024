import math

for deg in range(0 ,91 ,15):
    #rad = math.radian(deg)
    rad = math.pi * deg / 180
    if deg != 90:
        print(f"{deg:4d} {math.sin(rad):6.4f} {math.cos(rad):6.4f} {math.tan(rad):6.4f}")
    else:
        print(f"{deg:4d} {math.sin(rad):.4f} {math.cos(rad):.4f} {"N/A":^6}") #가운데 정렬
# 이거 왜 안됨?????

#import math
#for deg in range(0 ,91 ,15):
    #rad = math.radian(deg)
    #rad = math.pi * deg / 180
    #print(f"{deg:4d} {math.sin(rad):.4f} {math.cos(rad):.4f} {'N/A':>6}") #오른쪽 정렬
    #print(f"{deg:4d} {math.sin(rad):.4f} {math.cos(rad):.4f} {'N/A':<6}") #왼쪽정렬
    #print(f"{deg:4d} {math.sin(rad):.4f} {math.cos(rad):.4f} {'N/A':^6}") #가운데 정렬