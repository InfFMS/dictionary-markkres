# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор
dic1={'a':'@','b':'#','c':'$','d':'%','e':'&','f':'*','g':'(','h':')','i':'-','j':'=','k':'+','l':'[','m':']','n':'{','o':'}','p':'|','q':';','r':':','s':'<','t':'>','u':'?','v':'/','w':'~','x':'^','y':'_','z':'`'}
dic2={}
for a in dic1:
    dic2[dic1[a]]=a
def shifr(a):
    b=''
    for c in a:
        if c in dic1:
            b+=dic1[c]
        else:
            b+=c
    return b
def deshifr(a):
    b=''
    for c in a:
        if c in dic2:
            b+=dic2[c]
        else:
            b+=c
    return b
a='hello world'
b=shifr(a)
print(b)
print(deshifr(b))
