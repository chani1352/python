# n은 참조 변수,데이터타입 지정 불필요
n = 10
print(n)

n="   good nice today   "
print("\n심볼 = " + n.title()) # title 첫글자 대문자
# f-format f" ~ {변수}"
print(f"\t심볼 = {n.strip()}")  # strip 앞뒤 공백 제거

# int a = 10, b = 20, c = 30; 자바 버전
a,b,c = 10,20,30