def largest(a, b, c):
    if a>b>=c and a>c>=b:
        print(f"가장 큰 수는 {a}입니다.")
    if b>a>=c and b>c>=a:
        print(f"가장 큰 수는 {b}입니다.")
    if c>a>=b and c>b>=a:
        print(f"가장 큰 수는 {c}입니다.")
    if a==b>c:
        print(f"가장 큰 수는 {a,b}입니다.")
    if a==c>b:
        print(f"가장 큰 수는 {a,c}입니다.")
    if b==c>a:
        print(f"가장 큰 수는 {b,c}입니다.")
    else:
        print("가장 큰 수는 존재하지 않습니다.")

def main():
    x1 = 5 
    x2 = 7 
    x3 = 2
    largest_num = largest(x1, x2, x3)
    print(f"가장 큰 수는 {largest_num}입니다.")

if __name__ == "__main__":
    main()