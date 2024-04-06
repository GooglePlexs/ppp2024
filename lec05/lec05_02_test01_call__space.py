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

# *********************************************************************************************************************************************************** #

def read_file(filename):
  with open(filename) as f:
    text = f.readline().strip() # f안에 있는 함수이름(readline)
  #  text = "3 5 7\n".strip()   # 실제
    print(f"!{text}!")
    return text

# *********************************************************************************************************************************************************** #



def main():
  
  # input_text = "5 10 3 4 7"
  input_text = read_file("lec05/numbers1.txt")
  # 조건 값을 다른 파일에서 가져오는 방법 (간접적)

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

  print(f"리스트의 마지막 값은 {nums[-1]}")

if __name__ == "__main__":
  main()