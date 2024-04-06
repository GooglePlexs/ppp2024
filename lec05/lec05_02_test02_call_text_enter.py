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

#def read_file_1(filename):
#  with open(filename) as f:
#     for line in f:
#        text = line.strip()
#        print(f"!{text}!")
#        nums = text2list(text)


#def read_file_2(filename):
#  with open(filename) as f:
#     lines = f.readlines()
#     for line in lines:               
#        text = line.strip()
#        print(f"!{line}!")
#        nums = text2list(text)


# 복잡하게 설계했을 경우
#def read_file_multi_line(filename):
#  data = []
#  with open(filename) as f:
#     lines = f.readlines()
#     for line in lines:               
#        text = line.strip()
#        print(f"!{line}!")
#        value = int(text)
#        data.append(value)
#        return " ".join(data)
     

def read_file_from_line(filename):
  data = []
  with open(filename) as f:
    lines = f.readlines()
    for line in lines:               
       text = line.strip()
       value = int(text)
       data.append(value)
    return data

#파일 크기가 1GB 일때
#첫 번째 : 1줄 읽고, 1줄 처리 ... 1줄 읽고, 1줄 처리 ... (메모리 사용량: 적음)
#두 번째 : 전체 읽고, 전체 처리 (메모리 사용량: 1GB)
#lines은 list 형식이다(많은 숫자 담는다)

# *********************************************************************************************************************************************************** #



def main():
  
  # input_text = "5 10 3 4 7"


  # 복잡하게 설계한 경우
  #input_text = read_file_multi_line("lec05/numbers2.txt")  # 사용자 단계 (01 -> 02로 변화)
  
  
  # 조건 값을 다른 파일에서 가져오는 방법 (간접적)

  nums = read_file_from_line("lec05/numbers2.txt")

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