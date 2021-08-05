"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []

when do we need to use a lambda function?
lambda is the same as any other function, they are simple functions that you write in one line. Whenever you need a function to get something done, you can use a lambda function to make things easier.
They are kinda like lambda functions
"""
def sort_by_length(lst):
    # sort the list in ascending order based on the length of the str
    sorted_list = (sorted(lst, key=lambda item: len(item)))
    return sorted_list

print(sort_by_length(["apple", "pie", "shortcake"]))
