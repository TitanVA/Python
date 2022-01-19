# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)
#
#
# my_nums = square_numbers([1, 2, 3, 4, 5])
my_nums = (x*x for x in range(1, 6))

print(my_nums)
for i in my_nums:
    print(i)