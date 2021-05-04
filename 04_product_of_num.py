# Given an integer array nums, write a function that returns 
# an array products, such that each entry at position i, in 
# products is a product of all the other elements in nums except
# nums[i].

# Example: If nums = [4, 5, 10, 2], your function should return
# [100, 80, 40, 200].

# Explanation: 100 is the product of 5, 10, and 2 - All numbers in 
# nums array except 4.Similarly, 80 is the product of 4, 10, 2, 
# which are all the numbers in nums array except 5.

from math import prod

def array_of_products(nums):
    result = []

    if nums == None or len(nums) == 1:
        return []
    
    product_of_array_elements = int((prod(nums)))
    
    for i in range(len(nums)):
        if nums[i] != 0:
            var = product_of_array_elements / nums[i]
            result.append(int(var))
        else:
            outcome = 1
            for num in nums:
                if num != 0:
                    outcome *= num
            result.append(outcome)

    return result

# nums = [4, 5, 10, 2]
# print(array_of_products(nums))

print('\n********Test Case 1************')
# Test case 1: When nums is null.
nums = None
print(array_of_products(nums))


print('\n********Test Case 2************')
# Test case 2: When nums is an empty array, should return [-1, -1]
nums = []
print(array_of_products(nums))

print('\n********Test Case 3************')
# Test case 3: When nums has just one occurrence of val, should return [0, 0]
nums = [3]
print(array_of_products(nums))


print('\n********Test Case 4************')
# Test case 4: When nums has multiple occurrences of val,  should return [0, 2]
nums = [3, 2, 0]
print(array_of_products(nums))


# print('\n********Test Case 5************')
# # Test case 5: All zeros.
nums = [3, 2, 3]
print(array_of_products(nums))