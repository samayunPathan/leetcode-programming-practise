def rank_arr(nums):
    n=sorted(list(set(nums)));d={}
    for i in range(len(n)):
        d[n[i]]=i+1
    return [d[i] for i in nums]

n=[3,7,1,5]
m=[1,1,1]
ns=[37,12,28,9,100,56,80,5,12]

print(rank_arr(ns))