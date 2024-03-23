import math

start_degree = 0
end_degree = 360


print("각도 radian    sin      cos      tan")


for x in range(start_degree, end_degree + 1):
  radian_result = math.radians(x)
  sin_result = math.sin(math.radians(x))
  cos_result = math.cos(math.radians(x))
  tan_result = math.tan(math.radians(x))
  

  
  print(f"{x}   {radian_result:.4f}   {sin_result:.4f}   {cos_result:.4f}   {tan_result:.4f}")