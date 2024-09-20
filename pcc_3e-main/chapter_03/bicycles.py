bicycles = ['trek', 'cannondale', 'redline', 'specialized']


message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

print(len(bicycles)) #length

print(bicycles[-1].title())

bicycles[1] = "genesis" # 바꿔치기
print(bicycles[1].title())

#추가 -> insert,append
bicycles.append("canival") #마지막에 추가
print(bicycles)

bicycles.insert(1,"sonata") # 해당 index에 추가
print(bicycles)

#삭제
del bicycles[0] 
print(bicycles)