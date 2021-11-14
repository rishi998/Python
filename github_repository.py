def largest( arr, n):
    maxi=arr[0]
    for i in range(0,len(arr)):
        if maxi<arr[i]:
            maxi=arr[i]
    return maxi
arr=[]
n=int(input("Enter size of array!"))
for i in range(0,n):
    arr=int(input())
print(largest(arr,n))