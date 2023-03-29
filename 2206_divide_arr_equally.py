def divide_arr(arr):
    if len(arr)%2==0:
        return all([for i in arr if arr.count(i)%2==0])
        # for i in arr:
        #     if arr.count(i)%2==0:
        #         print(i)
    #             return True
    return False

a=[18,19,5,5,18,19,5,6,12,19,13,4,16,11,4,16,10,8,12,8,2,1,8,17,4,18,3,5,16,2,16,12,17,16,7,16,2,17,19,9,1,20,17,17,4,6]
print(divide_arr(a))