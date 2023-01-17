input_list=[]
even_list=[]
odd_list=[]

input_list=list(map(int,input("This is input: ").split()))

for num in input_list:
  if num<0:
      input_list.remove(num)
  else:
      pass

for num in input_list:
    if num%2==0:
        even_list.append(num)
        
    else:
        odd_list.append(num)

arr2=list(set(odd_list))
arr1=list(set(even_list))
print("This is output arr1: ",arr1)
print("This is output arr2: ",arr2)
