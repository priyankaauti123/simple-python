n=input()
arr_data=[input() for i in range(n)]

#print arr_data

def remove_from_position(arr_data,count1,pos):
    pos-=count1
    print pos
    for i in range(count1):
        arr_data.pop(pos)
    arr_data.insert(pos,count1)
    print arr_data

def replacement_fun(arr_data,n):
    cnt=0
    i=0
    while(i!=n):
        if arr_data[i]%2==0 and i!=n-1:
            cnt+=1
        else:
            if arr_data[i]%2==0 and i==n-1:
                cnt+=1
                remove_from_position(arr_data,cnt,i)
                cnt=0
            else:
                if ((cnt>=2) or (i==n-1)):
                    print cnt,i
                    cnt+=1
                    remove_from_position(arr_data,cnt,i-1)
                    cnt=0
                else:
                    cnt=0
        i+=1
    #print arr_data

def even_data_replacement(arr_data,n):
    replacement_fun(arr_data,n)


even_data_replacement(arr_data,n)






