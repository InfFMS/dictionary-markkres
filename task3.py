# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2
a=input().lower()
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
res = " ".join(f"{i}-{j}" for i,j in dic.items())
print(res)
