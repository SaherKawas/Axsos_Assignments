def countDown(n):
    arr=[]
    for i in range(n):
        arr.append(n-i)
    return arr
# print(countDown(5))
 
def print_and_return(arr):
    print(arr[0])
    return arr[1]
 
# print(print_and_return([7,2]))
 
def first_pluse_length(arr):
    return arr[0]+len(arr)
# print(first_pluse_length([1,2,3,4,5]))
 
def values_greater_than_second(arr):
    if(len(arr)<2):
        return False
    count =0
    newList=[]
    for i in range(len(arr)):
        if(arr[i]>arr[1]):
            count+=1
            newList.append(arr[i])
    print(count)
    return newList
# print(values_greater_than_second([5,2,3,2,1,4]))

def this_length_that_value(x,y):
    arr=[]
    for i in range (x):
        arr.append(y)
    return arr
# print(this_length_that_value(6,2))