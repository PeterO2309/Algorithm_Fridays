# Given an array nums, and a value val, write a function to 
# remove all instances of val from the array and return the new length.

# Example: if nums = [5, 2, 2, 5, 3] and val = 5, your function should 
# return 3.

# Explanation: The elements of the array after removing 5 are [2, 2, 3],
# making the length of the array 3.

# def remove_val(nums, val):
#     count = 0 

#     # Edge case
#     if nums == None:
#         return 0

#     # only count if val exists in the nums list
#     if val in nums:
#         for i in nums:
#             if i != val:
#                 count += 1
#         return count
#     else:
#         return len(nums)

# nums = [5, 2, 2, 5, 3]
# val = 8
# print(remove_val(nums, val))


# Uduak's solution in JavaScript https://meekg33k.dev/understanding-how-the-filter-function-works
# interpreted by me in Python
def getCountOfNonEqualElements(nums, val):
    countOfNonEqualElements = 0

    # When nums is null or undefined or an empty array
    if nums == None or len(nums) ==0:
       return countOfNonEqualElements

    start = 0
    end = len(nums) - 1

    while(start <= end):
        if start != end:
        # When pointers are not equal, 
        # check for elements at nums[start] and nums[end]
            if nums[start] != val:
                countOfNonEqualElements += 1
            if nums[end] != val:
                countOfNonEqualElements += 1
        
        else:
            # When pointers are equal, no need to duplicate the work 
            # because nums[start] = nums[end]
            if nums[end] != val:
                countOfNonEqualElements += 1
        
        start += 1  # Move start pointer forwards
        end -= 1    # Move end pointer backwards

    return countOfNonEqualElements




nums = [5, 2, 2, 5, 3]
val = 8
print(getCountOfNonEqualElements(nums, val))
