def read_col(filename, col_idx):

  results = []
  with open(filename) as f:
    lines = f.readlines()
    for line in lines[1:]:
      tokens = line.split(",")
      results.append(float(tokens[col_idx]))
  return results


def main():

  tavg_year = read_col("hw10/weather(146)_2022-2022.csv", 4)
  rainfall = read_col("hw10/weather(146)_2022-2022.csv", 9)

  tavg_year_avg = sum(tavg_year) / len(tavg_year)

  rainfall_five = 0
  for rain_data in rainfall:
    if rain_data >= 5.0:
      rainfall_five += 1

  total_rainfall = sum(rainfall)

  # 결과 출력
  print(f"연 평균 기온은 {tavg_year_avg:.1f}°C입니다.")
  print(f"연 5mm 이상 강우 일수는 {rainfall_five:.1f}일입니다.")
  print(f"총 강우량은 {total_rainfall:.1f}mm입니다.")


if __name__ == "__main__":
  main()