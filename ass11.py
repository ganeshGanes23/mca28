arr=[]
sum=int(input())
for i in range(len(arr)):
    for j in range(len(arr)):
        if j>i:
            for k in range(len(arr)):
                if K>j:
                    if arr[i]+arr[j]+arr[k]==sum:
                        print({arr[i],arr[j],arr[k]})
                       