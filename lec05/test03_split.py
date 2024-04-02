def main():
  
    #input_text = "5, 10, 3, 4, 7" # 방법 1
    #tokens = input_text.split(",")          # ['5', ' 10', ' 3', ' 4', ' 7’] numbers = []
    #results = []
    #for token in tokens:
    #    results.append(int(token))          # 숫자로 변환해서 추가        
    #print(sum(results))
    ##print(max(results))
    ##print(min(results))
  
  results = [int(x) for x in input_text.split(",")]
  print(results)


if __name__ == "__main__":
  main()