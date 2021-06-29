n = int(input())
dict = {}

for i in range(n):
    a = input().split()
    dict[a[0]] = a[1]
  
for j in range(n):
    b = str(input())
    if b not in dict:
        print ("Not found")
    else:
        print (str(b) + "=" + str(dict[b]))
