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


def read_col_int(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        print(header) #???
        for line in lines[1:]:
            tokens = line.split(",")
            years = int(tokens[0])
            months = int(tokens[1])
            days = int(tokens[2])
            dataset.append([years, months, days])
    return dataset



def main():

    weather_filename = "hw11/weather(146)_2022-2022.csv" # 파일이 변경되었을 때 수정을 최소화 할 수 있다
    tavg = read_col(weather_filename , "tavg")
    tmax = read_col(weather_filename , "tmax")
    rainfall = read_col(weather_filename , "rainfall")

    months = read_col(weather_filename, "month")  # 수정된 부분
    months = [int(x) for x in months]
    summer_rainfall = sumifs(rainfall, months, selected=[6, 7, 8])




    # 1번 연평균기온
    print(f"연 평균 기온은 {sum(tavg)/len(tavg):.1f}°C입니다.")
    # 2번 5mm 이상 강우일수 
    print(f"연 5mm 이상 강우일수는 {count_rainday(rainfall)}일 입니다.")
    # 3번 총 강우량
    print(f"총 강우량은 {sum(rainfall):.1f}mm 입니다.")
    # 4페이지 4번 최장 연속 강우일수
    print(f"최장 연속 강우일수는 {longest_rainday(rainfall)}일 입니다.")
    # 4페이지 5번 강우 이벤트 중 최대 강수량
    print(f"강우 이벤트 중 최대 강수량은 {max_rainfall_event(rainfall):.1f}mm 입니다.")
    # 4페이지 6번 가장 더운날 top 3
    print(f"가장 더운날 top 3는 {top_rank(tmax, 3)}°C 입니다.")
    # 5페이지 1번 여름철(6,7,8) 총 강수량

    print(f"6, 7, 8월 강수량은 {summer_rainfall:.1f}mm 입니다.")


    weather_filename_wide = "hw11/weather(146)_2001-2022.csv"
    rainfall_all = read_col_int(weather_filename_wide, "rainfall", 2021)
    rainfall_all += read_col_int(weather_filename_wide, "rainfall", 2022)  # 2021년과 2022년 강수량 합산
    # 5페이지 2번 2021년과 2022년의 총 강수량
    print(f"2021년과 2022년 총 강수량은 {sum(rainfall_all):.1f}mm 입니다.")
    


if __name__ == "__main__":
  main()