# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
a=list(map(str,input().split()))
b=list(map(int,input().split()))
dic={}
for i in range(len(b)):
    dic[a[i]]=b[i]
print(dic)
