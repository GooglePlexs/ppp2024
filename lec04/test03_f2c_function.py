temp_f = int(input("계산할 화씨온도를 입력하시오"))

def f2c(temp_f):
    return (temp_f - 32) * 5 / 9
print("{}F => {:.2f}C" .format(temp_f, f2c(temp_f)))


