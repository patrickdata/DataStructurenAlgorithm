#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Solution:
    def TwoSum(nums, target):
        listtoreturn = {}
        for i in range(len(nums)):
            currentmapvalue = listtoreturn.get(nums[i])
            if currentmapvalue == None:
                numbertofind = target - nums[i]
                listtoreturn[numbertofind] = i
            else:
                return (currentmapvalue,i)
            
    test = [1,3,7,9,2]
    result = TwoSum(test,11)
    print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




