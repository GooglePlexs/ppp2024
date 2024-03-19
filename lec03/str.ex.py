#text = input("영어 단어를 입력하세요")

text = "orange"

print('입력한 문자는 "{}"입니다.'.format(text)) 
# \"일 경우는 기존의"를 '로 바꿔 적으면 구분이 편하다
print(len(text))
#len의 경우에는 영단어 길이(개수)를 계산해준다
print(text.upper())
#upper 말 그대로 단어를 전부 대문자로 바꾸는 것임


print(5 * 20)
# 숫자 계산
print("5" * 20)
# 문자를 20번 출력해라
print("=" * 30)
# 문자를 30번 출력해라 (p.10)

#첫 세글자, 마지막 두글자
print(text[:3])
print(text[-2:])

print(text[4])
#orange에서 g를 추출 할 때 5번째지만 인덱스는 0부터 시작해서 4를 입력해야 추출범위로 묶을 수 있다 ([4:4]는 안 된다)
print(text[:])
# : -> 전체추출

#문자열 뒤집기
print(text[::-1])
# 처음부터 끝자리 뒤에서 부터