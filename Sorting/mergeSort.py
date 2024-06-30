def mergeSort(arr, low, high):
    # base case:
    if (low == high):
        return arr
    mid = int((low+high)/2)
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)

def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid+1
    while(left<=mid and right<=high):
        if(arr[left]<=arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    while (left<=mid):
        temp.append(arr[left])
        left+=1
    
    while (right<=high):
        temp.append(arr[right])
        right+=1
        
    for i in range(low,high):
        arr[i] = temp[i-low]

def main():
    arr = [3,2,4,1,3]
    low = 0
    high = len(arr)-1
    mergeSort(arr,low,high)
    print(arr)
        
main()
    
