# Задача №1
s = [ int(i) for i in input().split()]
t = []
l = len(s)-1
k = 0
i = 0
if len(s)==0:
    print(str(0))
else:
    for st in s:
        if len(s)>1:
            if i==0:
                k = s[i+1] + s[-1]
                t.append(k)
            elif i>0 and i<l:
                k=s[i-1]+s[i+1]
                t.append(k)
            elif i==l:
                k = s[i-1]+s[0]
                t.append(k)
        elif len(s)==1:
            k = s[i]
            t.append(k)       
        i +=1
    j = 0
    for st2 in t:
        print(str(t[j])+' ',end='')
        j +=1
        
# Задача №2
s = [ int(i) for i in input().split()]
t = []
s.sort()
l = len(s)-1
k = 100000
if len(s)!=1:
    for i in range(0,l):
        if s[i]==s[i+1] and s[i]!=k:
            t.append(s[i])
            k=s[i]
    for j in range(l,l+1):
        if s[-1]==s[-2] and s[j]!=k:
            t.append(s[j])
n = len(t)
for g in range(0,n):
    print(t[g],end=' ')
    
#Задача №3 
a=float(input()) 
b=float(input()) 
c=input()

if c==('+'): 
    print (float(a+b))
elif c==('-'): 
    print (float(a-b))
elif c==('*'): 
    print (float(a*b))
elif c==('pow'):
     print (float(a**b))   
elif c==('/') and b!=0.0: 
    print (float(a/b))

elif c==('mod') and b!=0.0:
     print (float(a%b))

elif c==('div') and b!=0.0:
     print (float(a//b))
elif b==0:
    print ('Деление на 0!')
    
#Задача №4 
room=input()
if room == 'треугольник':
    a=float(input())
    b=float(input())
    c=float(input())
    p=((a+b+c)/2)
    s_room=(p*(p-a)*(p-b)*(p-c))**5
elif room == 'прямоугольник':
    a=float(input())
    b=float(input())
    s_room=a*b
elif room =='круг':
    r=float(input())
    s_room=3.14*(r**2)
print (s_room)

# Задача на 3 числа и выдачу максимального, минимального и оставшегося 
a=int(input())
b=int(input())
c=int(input())

s = a + b + c;
print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))

# К предыдущему решению, но через массивы
a=sorted([int(input()), int(input()), int(input())])
print(a[2], '\n', a[0], '\n', a[1])

# Также к предыдущему решению, но без доп знаний
a=int(input())
b=int(input())
c=int(input())

if a < b:    a, b = b, a
if b < c:    c, b = b, c
if a < b:    a, b = b, a
print(a, c, b, sep="\n")

#2 без доп знаний 
a=int(input())
b=int(input())
c=int(input())

if a>=b and a>=c:
    max=a
    if b>=c:
        min=c
    else:
        min=b
elif b>=a and b>=c:
    max=b
    if a>=c:
        min=c
    else:
        min=a
else:
    max=c
    if a>=b:
        min=b
    else:
        min=a
        
print(max,'\n',min,'\n',(a+b+c-max-min))

#Задача про окончание слова программист(а/ов)
n=int(input())
if n%10==1 and (n-11)%100!=0:
    print (n, 'программист')
elif n%10==2 and (n-12)%100!=0:
    print (n, 'программиста')
elif n%10==3 and (n-13)%100!=0:
    print (n, 'программиста')
elif n%10==4 and (n-14)%100!=0:
    print (n, 'программиста')
else:
    print (n, 'программистов')

#№2 про программистов 
n=int(input())
if n<0:
    print ('error')
elif n%10==1 and n%100!=11:
    print (n, 'программист')
elif n%10>=2 and n%10<=4 and (n%100<10 or n%100>20):
     print (n, 'программиста')
else:
     print (n, 'программистов')
    
#Задача про числа
a=int(input())
b=int(input())
c=int(input())
d=int(input())
for i in range(c, d + 1):
    print('\t', i, end ="")
for j in range(a, b + 1):
    print('\n',j, end ="")
    for z in range(c, d + 1):
        print('\t',j * z,end="")
        
# Решение задачи: 3.1 Функции, Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два.
l = [int(i) for i in input().split()]
def modify_list(l):
    //[Массив целиком l] = [действие, диапозон, условие] l
    l[:] = [i // 2 for i in l if i % 2 == 0]
    //Возврат измененного массива l
    return l
    
modify_list(l)            

print(l)        
