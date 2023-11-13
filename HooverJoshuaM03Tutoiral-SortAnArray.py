#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ZOT(arr):
    low = count = 0
    high = len(arr)-1 
    while(count<=high):
        
        # if arr[count] == 2 swap(arr[count],arr[high]) high--
        if arr[count] == 2:
            arr[count],arr[high] = arr[high],arr[count]
            high = high - 1
            
        # if arr[count] == 1 Dont swap anything, Increment count i.e, count++     
        elif arr[count] == 1:
            count = count +1
            
        # if arr[count] == 0 swap(arr[count],arr[low]) count++, low++   
        elif arr[count] == 0:
            arr[count],arr[low] = arr[low],arr[count]
            count = count + 1
            low = low + 1
            
        else:
            return -1
            
            
    return arr
if __name__=="__main__":
    arr = [0,1,2,1,2,0,2,0]
    print(ZOT(arr))


# In[ ]:




