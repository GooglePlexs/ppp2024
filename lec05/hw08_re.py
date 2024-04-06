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

  # nums.sort()  - 1)

  print(f"주어진 리스트는 {nums}")

  average_value = average(nums)
  print("평균값은 {:.1f}".format(average_value))

  median_value = median(nums)
  print("중앙값은 {}".format(median_value))

  min_value = min_number(nums)
  print(f"최솟값은 {min_value}")

  max_value = max_number(nums)
  print(f"최댓값은 {max_value}")

  print(f"리스트의 마지막 값은 {nums[-1]}")

  # 뒤에서 세니까 7임
  # nums.sort()가 들어가 있으면 10이 나옴  - 1)
  # nums.sort() (우리가 가진 nums 자체의 순서가 바뀜) =/= sorted(nums) (nums 자체의 순서가 변하지는 않고, 정렬 한 것을 return 값에 부여 할 뿐임)
  # nums.sort() = 책 자체에 필기 (리턴값이 없음) / sorted(nums) = 필사한 연습장에 필기 (리턴값이 있음)

if __name__ == "__main__":
  main()