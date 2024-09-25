#import pizza  #pizza.py 파일

#파일명.함수()
#pizza.make_pizza(16, 'pepperoni')
#pizza. make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from pizza import make_pizza #특정 함수만 호출, 
# #함수() > 파일명. 필요 없음
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza as mp #함수명이 길때 as로 별칭 설정 가능 > import 파일명 as : 파일명도 as로 가능
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

