def average(nums):

  total_number = sum(nums)
  count_number = len(nums)
  
  return total_number / count_number

def main():
   nums = []
   while True:
      input_number = input("숫자를 입력하세요 (exit: 종료): ")
      if input_number == "exit":
         break
      nums.append(int(input_number))
   average_value = average(nums)
   print(f"해당 숫자 리스트 {nums}의 평균은 {average_value:.1f}입니다.")

if __name__ == "__main__":
  main()