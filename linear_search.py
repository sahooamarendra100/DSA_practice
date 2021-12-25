lst = [10,20,30,40,50,60] 
 
res = [x for x in range(len(lst)) if lst[x] == 20]
 
print (res) 

lst = [10,10,10,10,20,20,40] 
res = [x for x in range(len(lst)) if lst[x] == 40]
if(len(res) > 1):
	 print(res[0])
elif(len(res)==1):
	print(res)
else:
	print("-1")