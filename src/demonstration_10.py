"""
Challenge #10:

Create a function that applies a discount d to every number in the list.

Examples:
- get_discounts([2, 4, 6, 11], "50%") ➞ [1, 2, 3, 5.5]
- get_discounts([10, 20, 40, 80], "75%") ➞ [7.5, 15, 30, 60]
- get_discounts([100], "45%") ➞ [45]

Notes:
- The discount is the percentage of the original price (i.e the discount of
"75%" to 12 would be 9 as opposed to taking off 75% (making 3)).
- There won't be any awkward decimal numbers, only 0.5 to deal with.

to do:
- convert percentage to a decimal
- create a new_list [list = array]
- loop through the initial list of nums
- for each item, apply the discount 
    [divide num by the percentage]
- return the new_list
"""
def get_discounts(nums, percentage):
    decimal = float(percentage.strip('%')) / 100.0
    new_list = []

    i = 0
    while i < len(nums):
       discount = nums[i] * decimal
       new_list.append(discount)
       i += 1
    return new_list
    

print(get_discounts([2, 4, 6, 11], "50%"))
print(get_discounts([10, 20, 40, 80], "75%"))
print(get_discounts([100], "45%"))