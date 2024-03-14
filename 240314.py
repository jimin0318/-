a=int(input())
b=int(input())
c=a+b
print('a와 b의 합은', c)
print('a와 b의 평균값은', c/2)

a=float(3)
b=float(2.5)
c=a+b
print('a와 b의 합은', c)
print('a와 b의 평균값은', c/2)

a=float(input())
b=float(input())
c=a+b
print("a와 b의 합은", c)
print("a와 b의 평균값은", c/2)

a=int(input())
b=int(input())

print('a와 b의 합은', c)
print('a와 b의 평균값은', (a+b)/2)


makit='Sieun Woojin!'
result = makit[0]

print(result)
result = makit[6]

print(result)
result = makit[-1]
print(result)

makit = 'Sieun Woojin!'
result=makit[2:9]
print(result)
result=makit[0:5]
print(result)
result=makit[6:]
print(result)

makit = '동서남북동서남북동서남북'
print(makit[::4])

makit = '동서남북'
print(makit[::-1])

phone = '010-1234-5678'
new_phone = phone.replace('-','.')
print(new_phone)

n=int(input("초를 입력하세요:"))
print(n,'초(sec)는',n//60,'분(min)',n%60,'초(sec)입니다.')

n=int(input("분을 입력하세요:"))
print(n,'분은',n//1440,'일',n%1440//60,'시간',n%60,'분입니다.')

a = ['메이킷','우진','시은']
print(a[0:3])
print(a[0])
print(a[1])
print(a[2])

a = ['메이킷','우진','제임스','시은']
print(a[0:2])
print(a[1:])
print(a[2:])
print(a[:])


a = ['우진','시은']
a.append('메이킷') 
print(a)
del a[2] 
print(a)

a = ['우진','시은','메이킷']
a.insert(1,'하워드')
print(a)

a = ['우진', '시은']
b = ['메이킷', '소피아', '하워드']
a.extend(b)
print(a)
print(b)


a = ['우진','시은']
b = ['메이킷','소피아','하워드']
c = []
c.extend(a)
print(c) # ['우진','시은'] 출력
c.extend(b)
print(c) # ['우진','시은','메이킷','소피아','하워드'] 출력


a = [3, 7, 4, 5, 6, 8]
print('리스트 a의 개수 즉 길이는',len(a))
print('리스트 a의 숫자들의 평균은',sum(a)/len(a))
