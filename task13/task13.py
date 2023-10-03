# Task 1
def count_local_variables():
    a = 10
    b = "Hello, World!"
    c = [1, 2, 3]

    local_vars = locals()

    count = len(local_vars) - 1

    return count

num_locals = count_local_variables()
print(f"Number of local variables: {num_locals}")


# Task 2
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function

add_10 = outer_function(10)

result = add_10(5)

print(result)

# Task 3
def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
