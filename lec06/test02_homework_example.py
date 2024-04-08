##
def read_tmax(filename):
    
    results = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tmax = float(tokens[5])
            results.append(tmax)
    
    return results

def read_tmin(filename):
    
    results_2 = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tmin = float(tokens[5])
            results_2.append(tmin)
    
    return results_2


###
def read_weather(filename, col_idx):

    results = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tmax = float(tokens[col_idx])
            results.append(tmax)
    
    return results



def main():
    ##
    tmax = read_tmax("lec06/weather(146)_2022-2022.csv")
    tmin = read_tmin("lec06/weather(146)_2022-2022.csv")

    ### 같은 코드지만 인덱스만 다르기에 가능함 (다르게 기능함)
    tmax = read_col("lec06/weather(146)_2022-2022.csv" , 3)
    tmin = read_col("lec06/weather(146)_2022-2022.csv" , 5)


    print(f"연 최고 온도 (max(tmax))는 {max(tmax):.1f}입니다.")
    print(f"연 최저 온도 (min(tmin))는 {min(tmin):.1f}입니다.")


if __name__ == "__main__":
    main()