array_size=input()
list_data=[input() for i in range(array_size)]


def check_step_size(list_1):
    for i in range(1,len(list_1)):
        if abs(list_1[i-1]-list_1[i])==1:
            pass
        else:
            return 0
    return 1


def max_step_no1(list_data):
     step_arr=[]
     list_data=list(set(list_data))
     list_data.sort()
     print list_data
     i=0
     j=i+2
     while(i<j):
         if j<len(list_data):
             if (check_step_size(list_data[i:j+1]))==1:
                 step_arr.append(list_data[i:j+1])
                 print step_arr
                 j+=1
         else:
             i+=1
             j=i+2
     print step_arr


max_step_no1(list_data)




