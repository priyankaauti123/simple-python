n=input()

array_data=[input() for i in range(n)]

def max_no(arr):
    max1=0
    for i in range(len(arr)):
        if max1<arr[i]:
            max1=arr[i]
    print max1

max_no(array_data)


