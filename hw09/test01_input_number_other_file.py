def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        data = []
        for line in lines:
            text = line.strip()
            nums = text2list(text)
            data.extend(nums)
        return data


def text2list(text):
    return [int(x) for x in text.split()]

def num_number(nums):
    
    return len(nums)

def average(nums):

  return sum(nums) / len(nums)

def max_number(nums):
    max_num = max(nums)
    return max_num

def min_number(nums):
    min_num = min(nums)
    return min_num

def median(nums):

  sorted_nums = sorted(nums)
  length = len(sorted_nums)
  mid_index = length // 2
  
  return sorted_nums[mid_index]


def main():
    nums = read_file("hw09/numbers1.txt")
    
    num_value = num_number(nums)
    print(f"총 숫자 개수: {num_value}")

    average_value = average(nums)
    print(f"평균: {average_value:.1f}")

    max_value = max_number(nums)
    print(f"최댓값: {max_value}")

    min_value = min_number(nums)
    print(f"최솟값: {min_value}")

    median_value = median(nums)
    print(f"중앙값: {median_value}")


if __name__ == "__main__":
    main()