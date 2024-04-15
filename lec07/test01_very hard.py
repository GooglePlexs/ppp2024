def read_col(filename, col_name):
   dataset = []
   with open(filename) as f:
    lines = f.readlines()
    header = [x.strip() for x in lines[0].split(",")] ###
    print(header) ### 이 코드를 이용해서 순서가 아닌 영어로 호출
    col_idx = header.index(col_name) ###
    for line in lines[1:]:
      tokens = line.split(",")
      dataset.append(float(tokens[col_idx]))

    return dataset


#방법 1
#def count_rainday(rainfall):
#  rainfall_five = 0
#  for rain_data in rainfall:
#    if rain_data >= 5.0:
#      rainfall_five += 1
#  return rainfall_five


#방법 2
def count_rainday(rainfall):
  
  return sum([1 if x >= 5 else 0 for x in rainfall])


def longest_rainday(rainfall):
  
  rain_event = []

  # 각 객체에 숫자 부여 0,1,2,3(일차)

  prev_rain_count = 0
  for rain in rainfall:
    if rain ==0:
      if prev_rain_count > 0:  # 각 객체별 분화 1,2 / 0 / 1,2,3 /0 ...
        rain_event.append(prev_rain_count) # 각 객체별 분화 1,2 / 0 / 1,2,3 /0 ...
      prev_rain_count = 0
    else:
      prev_rain_count += 1
  
  return max(rain_event) 


def max_rainfall_event(rainfall):
  
  rain_event = []

  prev_rain = 0
  prev_rain_count = 0
  for rain in rainfall:
    if rain ==0:
      if prev_rain_count > 0:  
        rain_event.append(prev_rain) 
      prev_rain = 0
      prev_rain_count = 0
    else:
      prev_rain_count += 1
      prev_rain += rain
  
  return max(rain_event) 


def top_rank(values, limit):
  # return sorted(values)[-limit:] # 3,2,1 등
  # return sorted(values)[-limit:][::-1] # 1,2,3 등 
  return sorted(values, reverse = True)[:limit] # 1,2,3 등


def read_col_int(filename, col_name):
   dataset = []
   with open(filename) as f:
    lines = f.readlines()
    header = [x.strip() for x in lines[0].split(",")] ###
    print(header) ### 이 코드를 이용해서 순서가 아닌 영어로 호출
    col_idx = header.index(col_name) ###
    for line in lines[1:]:
      tokens = line.split(",")
      dataset.append(float(tokens[col_idx]))

    return dataset
   

def sumifs(rainfall, months, conditions):
  
  total = 0

#  for i in range(len(rainfall)):
#    rain = rainfall[i]
#    month = months[i]
#    if month in conditions:
#      total += rain

  for rain, month in zip(rainfall,months):
    if month in conditions:
      total += rain

  return total


def get_year_ifs(values, conditions, criteria):
#  dataset = []
#  for rain, year in zip(values,conditions):    
#    if year == criteria:
#      dataset.append(rain)
  
#  return dataset
   return [rain for rain, year in zip(values, conditions, criteria) if year == criteria]

def read_col_year(weather_filename, col_name, year):
   dataset = []
   with open(weather_filename) as f:
    lines = f.readlines()
    header = [x.strip() for x in lines[0].split(",")] ###
    print(header) ### 이 코드를 이용해서 순서가 아닌 영어로 호출
    col_idx = header.index(col_name) ###
    for line in lines[1:]:
      tokens = line.split(",")
      y = int(tokens[0])
      if y == year:
        dataset.append(float(tokens[col_idx]))
    return dataset



def main():

    weather_filename = "lec07/weather(146)_2022-2022.csv" # 파일이 변경되었을 때 수정을 최소화 할 수 있다
    tavg = read_col(weather_filename , "tavg")
    tmax = read_col(weather_filename , "tmax")
    rainfall = read_col(weather_filename , "rainfall")
    # months_float = read_col(weather_filename , "months")
    # months = read_col_int(weather_filename , "rainfall")
    months_float = read_col(weather_filename , "months")
    months = read_col_int(weather_filename , "rainfall")



    # 1번 연평균기온
    print(f"연 평균 기온은 {sum(tavg)/len(tavg):.1f}°C입니다.")
    # 2번 5mm 이상 강우일수 
    print(f"연 5mm 이상 강우일수는 {count_rainday(rainfall)}일 입니다.")
    # 3번 총 강우량
    print(f"총 강우량은 {sum(rainfall):.1f}mm 입니다.")
    # 4번 최장 연속 강우일수
    print(f"최장 연속 강우일수는 {longest_rainday(rainfall)}일 입니다.")
    # 5번 강우 이벤트 중 최대 강수량
    print(f"강우 이벤트 중 최대 강수량은 {max_rainfall_event(rainfall):.1f}mm 입니다.")
    # 6번 가장 더운날 top 3
    print(f"가장 더운날 top 3는 {top_rank(tmax, 3)}°C 입니다.")

    # 7번 6,7,8월 강수량
    print(f"6,7,8월 강수량은 {sumifs(rainfall, months, selected=[6,7,8])}mm 입니다.")
    # 8번 2021년 2022년 강수량

    weather_filename = "lec07/weather(146)_2001-2022.csv"

    # rainfall_2021 = read_col_year(weather_filename, "rainfall",2021)
    rainfall_all = read_col(weather_filename, "rainfall")
    year_all = read_col_int(weather_filename, "year")
    rainfall_2021 = get_year_ifs(rainfall_all, year_all, 2021)
    
    # rainfall_2021 = read_col_year(weather_filename, "rainfall", 2021)

    print(f"2021년, 2022년 강수량은 {sum(rainfall_2021):.1f}mm 입니다.")
    

if __name__ == "__main__":
  main()