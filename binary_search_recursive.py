l=[1,2,3,4,5,6,7,8]
l1=[4]
n=17

def binary_search(n,key,high,low=0):
    if high>=low:
        mid=(high+low)//2
        if n[mid]==key:
            return mid
        elif n[mid]>key:
            return binary_search(n,key,mid-1,low)
        else:
            return binary_search(n,key,high,mid+1)
    else:
        return 'element not found'
        
result=binary_search(l,n,len(l)-1,0)
if result !=1:
    print(f'{str(result)}')
else:
    print('element not found')




# Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):

# 	# Check base case
# 	if high >= low:

# 		mid = (high + low) // 2

# 		# If element is present at the middle itself
# 		if arr[mid] == x:
# 			return mid

# 		# If element is smaller than mid, then it can only
# 		# be present in left subarray
# 		elif arr[mid] > x:
# 			return binary_search(arr, low, mid - 1, x)

# 		# Else the element can only be present in right subarray
# 		else:
# 			return binary_search(arr, mid + 1, high, x)

# 	else:
# 		# Element is not present in the array
# 		return -1

# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# arr2=[4]
# x = 10

# # Function call
# result = binary_search(arr, 17, len(arr)-1, 4)

# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")

