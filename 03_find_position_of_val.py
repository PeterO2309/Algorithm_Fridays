'''
*******Link to Author's Solution Using JavaScript******
https://meekg33k.dev/sorting-algorithms-when-not-to-use-them


Given an unsorted array nums, write a function to find the start and end 
positions of a given number val in the array after sorting it.

Your function should return [-1, 1] if val isn't found in the array.
E.g: If nums =[0, 8, -2, 5, 0] and val=0, Your function should return [1, 2].

Explanation: The nums array after sorting becomes [-2, 0, 0, 5, 8], while
the start and end positions of 0 are of 1 and 2. 


'''

def findStartAndPositionOfVal(nums, val):
    if type(val) is not int:
        return [-1, -1]

    if nums == None or len(nums) == 0:
        return [-1, -1]

    countOfNumsLessThanVal = 0
    countOfVal = 0

    for num in nums:
        if (num < val):
            countOfNumsLessThanVal += 1
        if (num == val):
            countOfVal += 1
    
    # val is not found in array.
    if (countOfVal == 0):
        return [-1, -1]

    # Edge case: Val is smallest number in array.
    if countOfNumsLessThanVal == 0:
        return [0, countOfVal - 1]

    startOfVal = countOfNumsLessThanVal

    # Substract one because of zero based indexing
    endOfVal = startOfVal + countOfVal - 1


    return [startOfVal, endOfVal]


print('\n********Test Case 1************')
# Test case 1: When nums is null, should return [-1, -1] 
nums = None
val = 5
print(findStartAndPositionOfVal(nums, val))

print('\n********Test Case 2************')
# Test case 2: When nums is an empty array, should return [-1, -1]
nums = []
val = 5
print(findStartAndPositionOfVal(nums, val))

print('\n********Test Case 3************')
# Test case 3: When nums has just one occurrence of val, should return [0, 0]
nums = [0]
val = 0
print(findStartAndPositionOfVal(nums, val))

print('\n********Test Case 4************')
# Test case 4: When nums has multiple occurrences of val,  should return [0, 2]
nums = [3, 3, 3]
val = 3
print(findStartAndPositionOfVal(nums, val))

print('\n********Test Case 5************')
# Test case 5: When val is the smallest number in nums, should return [0, 2]
nums = [0, 8, 0, 0, 3, 12]
val = 0
print(findStartAndPositionOfVal(nums, val))

print('\n********Test Case 6************')
# Test case 6: When val is the biggest number in nums, should return [5, 5]
nums = [0, -8, 0, 0, 0, 3]
val = 3
print(findStartAndPositionOfVal(nums, val))

print('\n********Test Case 7************')
# Test case 7: When val is not the smallest nor biggest number in nums, should return [1, 4]
nums = [0, -8, 0, 0, 0, 3]
val = 0
print(findStartAndPositionOfVal(nums, val))




