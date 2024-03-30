#정답
def largest(nums):
    largest_num=nums[0]
    for num in nums:
        if largest_num < num:
            largest_num = num
    return largest_num

#다른 정답
def largest(nums):
    return max(nums)


def main():
    x = [3, 7, 5, 6, 3]
    print(f"가장 큰 수는 {largest(x)}입니다.")

if __name__ == "__main__":
    main()