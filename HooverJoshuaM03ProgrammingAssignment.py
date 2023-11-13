#!/usr/bin/env python
# coding: utf-8

# In[1]:


thing=["mozzarella", "cinderella ", "salmonella"]
print("Initial list of things")
print(thing)
thing[1]=thing[1].capitalize()
print("List with person being capitalized")
print(thing)
thing[0]=thing[0].upper()
print("List with cheesy thing converted to upper")
print(thing)
print("List with disease removed ")
thing.remove(thing[2])
print(thing)
print("List with new element")
thing.append("Noble Prize")
print(thing)


# In[2]:


def good():
  list_1 = ['Harry', 'Ron', 'Hermione']
  return list_1
def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num

count = 0
for num in get_odds():
    if count == 2:
        print(num)
        break
    count += 1


# In[ ]:




