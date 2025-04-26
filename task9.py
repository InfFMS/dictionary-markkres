friends_graph = {
    "Анна": ["Борис", "Виктор", "Дарья"],
    "Борис": ["Анна", "Виктор"],
    "Виктор": ["Анна", "Борис", "Дарья"],
    "Дарья": ["Анна", "Виктор", "Елена"],
    "Елена": ["Дарья"],
    "Данияр": []
}
lonely=[]
for i,j in  friends_graph.items():
    if j==[]: lonely.append(i)
for k in lonely:
    print(k,end=" ")
print()
sosed=input("Для кого надо найти соседей: ")
mas1=friends_graph[sosed]
for k in mas1:
    print(k,end=" ")
print()
print("Являются ли друзьями: ")
a,b=map(str,input().split())
L=False
mas2=friends_graph[a]
for k in mas2:
    if k==b:
        L=True
        break
print(L)
