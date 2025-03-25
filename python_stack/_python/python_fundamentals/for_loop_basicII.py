# Biggie Size 

def biggie_size(arr):
    for i in range(len(arr)):
        if(arr[i]>0):
            arr[i]="big"
    return arr

print(biggie_size([-1,3,-5,8]))

# Count Positives

def count_positives(arr):
    count=0
    for i in range(len(arr)):
        if(arr[i]>0):
            count+=1
    arr[len(arr)-1]=count
    if count==0:
        arr[len(arr)-1]=1
    return arr
print(count_positives([1,-3,4,5,-1]))
            

# Sum Total

def sum_total(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
    return total

print(sum_total([1,4,5,2]))

# Average

def average(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
    
    return total/len(arr)

print(average([1,2,3,4]))

# Length

def length(arr):
    count=0
    for i in range(len(arr)):
        count+=1
    return count
print(length([2,6,9,4,3]))

# Minimum

def minimum(arr):
    if not arr:  
        return False 
    smallest=arr[0]
    for i in range(len(arr)):
        if(arr[i]<smallest):
            smallest=arr[i]
    return smallest  
print(minimum([3,1,-4,-5,3]))
print(minimum([]))

# Maximum

def maximum(arr):
    if not arr:
        return False
    biggest=arr[0]
    for i in range(len(arr)):
        if(arr[i]>biggest):
            biggest=arr[i]
    return biggest
print(maximum([4,9,1,5,-1]))
print(maximum([]))

# Ultimate Analysis

def ultimate_analysis(arr):

    sumTotal=0
    for i in range(len(arr)):
        sumTotal+=arr[i]

    average=sumTotal/len(arr)

    smallest=arr[0]
    for i in range(len(arr)):
        if(arr[i]<smallest):
            smallest=arr[i]
    biggest=arr[0]
    for i in range(len(arr)):
        if(arr[i]>biggest):
            biggest=arr[i]
    length=0
    for i in range(len(arr)):
        length+=1

    return sumTotal,average,smallest,biggest,length
    

print(ultimate_analysis([1,3,6,3]))

# Reverse list

def reverse_list(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1]=arr[len(arr)-i-1], arr[i]
    return arr
    
print(reverse_list([1,6,7,4,9]))