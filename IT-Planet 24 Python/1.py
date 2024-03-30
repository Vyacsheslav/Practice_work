# arr = [1, 2, 3, 4, 5]
# sum = 0
# for i in range(0,5):
#     sum += arr[i]
# print(sum)

# str = "Hello, World!"
# count = sum(1 for c in str if c.lower() in 'aeiou')
# print(f"Number of vowels: {count}")

# def fff (numbers):
#     min_val = numbers[0]
#     for num in numbers:
#         if num < min_val:
#             min_val = num
#         return min_val
# nums = [3, 1, 4, 1, 5, 9, 2, 6]
# print("Min:", fff(nums))

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")

# def merge_lists(a, b):
#     for i in range(0, 2):  #Задание 19
#         b[i] += a[i]
#     print(b)
# a = [1, 3, 5]
# b = [2, 4, 6]
# merged = merge_lists(a, b)
# print(merged)

# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num % 2 == 0:
#         print(f"{num} is even", end=" ")
#     else:
#         print(f"{num} is odd", end=" ")

# def fff(n):
#     if n ==0:
#         return 1
#     return n * fff(n-1)
# print("factorial of 5:", fff(5))