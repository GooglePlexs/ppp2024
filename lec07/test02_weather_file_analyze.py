from test01_backup import read_col,read_col_int #__init__.py를 만들면 호출이 쉬워진다

def read_col_int(weather_filename, col_name):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        for line in lines[1:]:
            tokens = line.split(",")
            years = int(tokens[0])
            months = int(tokens[1])
            days = int(tokens[2])
            dataset.append([years,months,days])
    return dataset

def read_data(filename):
    pass







def main():
    weather_filename = "lec07/weather(146)_2022-2022.csv"
    tmax = read_col(weather_filename , "tmax")
    tmin = read_col(weather_filename , "tmin")

    #years = read_col_int(weather_filename , "years")
    #months = read_col_int(weather_filename , "months")
    #days = read_col_int(weather_filename , "days")

    dates = read_data(filename)

    #방법1
    temp_diff = []
    for tx, tn in zip(tmax,tmin):
        temp_diff.append(tx - tn)
    #방법2 - 다른 코드에서도 일반적
    temp_diff = []
    for i in range(len(tmax)):
        temp_diff.append(tmax[i] - tmin[i])
    #방법3 - 지능형 리스트(방법1을 한 줄로 고칠 수 있다)
    # temp_diff = [ for in] 해당 코드를 고쳐보시오
    temp_diff = [tx-tn for tx, tn in zip(tmax,tmin)]

    #방법1
    max_idx = 0
    max_diff_temp = 0
    i = 0
    for td in temp_diff:
        if max_diff_temp < td:
            max_diff_temp =td
            max_idx = i
        i += 1

    # print(f"일교차가 가장 큰 날짜는 0000/00/00 , 최대 일교차는 {max(temp_diff):.1f}C입니다.")
    # print(f"일교차가 가장 큰 날짜는 {years[max_idx]}/{months[max_idx]:02d}/{days[max_idx]} , 최대 일교차는 {max(temp_diff):.1f}C입니다.")
    print(f"일교차가 가장 큰 날짜는 {dates[max_idx]:02d} , 최대 일교차는 {max(temp_diff):.1f}C입니다.")


    #방법2
    max_idx = temp_diff.index(max(temp_diff))
    print(f"일교차가 가장 큰 날짜는 {dates[max_idx]:02d} , 최대 일교차는 {max(temp_diff):.1f}C입니다.")


    #방법3
    max_diff_temp = 0
    max_diff_date = None
    for td, date in zip(temp_diff,dates):
        if td > max_diff_temp:
            max_diff_temp = td
            max_diff_date = date
    print(f"일교차가 가장 큰 날짜는 {max_diff_date} , 최대 일교차는 {max_diff_temp:.1f}C입니다.")

    #방법4 (방법1의 간단화 버전)
    max_idx = 0
    max_diff_temp = 0
    for td in enumerate(temp_diff):
        if max_diff_temp < td:
            max_diff_temp =td
            max_idx = i
    print(f"일교차가 가장 큰 날짜는 {dates[max_idx]:02d} , 최대 일교차는 {max(temp_diff):.1f}C입니다.")



if __name__ == "__main__":
    main()