#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binary_search(arr, K):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == K:
            return mid  # Found K at position mid
        elif arr[mid] < K:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # K is not present in the array

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 5
position = binary_search(sorted_array, K)

if position != -1:
    print(f"{K} is present at position {position}.")
else:
    print(f"{K} is not present in the array.")


# In[ ]:




