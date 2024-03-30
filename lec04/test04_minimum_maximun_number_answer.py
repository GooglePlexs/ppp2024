def minmax(nums):
    max_num = max(nums)
    min_num = min(nums)
    return max_num, min_num

def main():

    x = [3, 7, 25, 10, 2, 13] 
    mn = minmax(x)[0] 
    mx = minmax(x)[1]
    # mn, mx = minmax(x) 로 쓸 수 있다. 언패킹이라고 한다. print(f“가장 작은 수는 {mn}이고, 가장 큰 수는 {mx}입니다.”)

    print(f"최솟값은 {mn}, 최대값은 {mx} 입니다.")

if __name__ == "__main__":
    main()