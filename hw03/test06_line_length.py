import math
def calculate_line_lenght(first_point_x,first_point_y,second_point_x,second_point_y):
    x = (first_point_x - second_point_x)
    y = (first_point_y - second_point_y)
    point_square = math.pow(x,2) +  math.pow(y,2)
    return math.sqrt(point_square)
    
first_point_x = int(input("첫번째 점의 x좌표를 입력하시오"))
first_point_y = int(input("첫번째 점의 y좌표를 입력하시오"))
second_point_x = int(input("두번째 점의 x좌표를 입력하시오"))
second_point_y = int(input("두번째 점의 y좌표를 입력하시오"))

line_length = calculate_line_lenght(first_point_x,first_point_y,second_point_x,second_point_y)
print("첫번째 점 좌표가({},{}), 두번째 점 좌표가({},{}) 일 때, 두 지점 사이의 길이는 {}입니다.".format(first_point_x,first_point_y,second_point_x,second_point_y,line_length))