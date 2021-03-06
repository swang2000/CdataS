'''
Three in One: Describe how you could use a single array to implement three stacks.
'''

'''
Approach 1: Fixed Division
We can divide the array in three equal parts and allow the individual stack to grow in that limited space.
Note: We will use the notation "[" to mean inclusive of an end point and "(" to mean exclusive of an end
point.
• For stack 1 , we will use [e, ~ ).
• For stack 2, we will use [ ~, 2~).
• For stack 3, we will use [ 2~, n).
'''