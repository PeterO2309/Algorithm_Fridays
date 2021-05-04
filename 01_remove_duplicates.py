# Given a sorted array nums, write a function to remove the duplicates
# from the array such that each element appears only once. Your function 
# should return the new length.

# For example, if nums = [0, 0,1, 1,2, 2, 3, 3, 4]. Your function should 
# return 5.


# def find_array_length(nums):
#     new_length = 0
#     no_duplicate = []

#     for i in nums:
#         if i not in no_duplicate:
#             no_duplicate.append(i)
#             new_length += 1

#     return new_length


# nums = [0, 0,1, 1,2, 2, 3, 3, 4]
# print(find_array_length(nums))

def find_array_length(nums):
    new_length = 0
    if nums == None:
        return 0

    for i in range(len(nums)):
        if nums[i - 1] != nums[i]:
            new_length += 1

    return new_length


nums = [0, 0,1, 1,2, 2, 3, 3, 4]
print(find_array_length(nums))

# https://meekg33k.dev/how-to-find-the-number-of-unique-elements-in-a-sorted-array