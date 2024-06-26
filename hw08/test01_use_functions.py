def text2list(text):
  
  return [int(x) for x in text.split()]


def average(nums):

  return sum(nums) / len(nums)


def median(nums):

  sorted_nums = sorted(nums)
  length = len(sorted_nums)
  mid_index = length // 2
  
  return sorted_nums[mid_index]

def min_number(nums):
    min_num = min(nums)
    return min_num

def max_number(nums):
    max_num = max(nums)
    return max_num


def main():
  
  input_text = "5 10 3 4 7"

  nums = text2list(input_text)

  print(f"주어진 리스트는 {nums}")

  average_value = average(nums)
  print("평균값은 {:.1f}".format(average_value))

  median_value = median(nums)
  print("중앙값은 {}".format(median_value))

  min_value = min_number(nums)
  print(f"최솟값은 {min_value}")

  max_value = max_number(nums)
  print(f"최댓값은 {max_value}")

if __name__ == "__main__":
  main()