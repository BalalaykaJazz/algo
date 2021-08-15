from algorithms.BinarySearch import lower_bound


# from bisect import bisect, bisect_left, bisect_right
#
# store = [1, 5, 8, 12, 16, 22, 34, 45, 53, 62]
# target = 12
#
# print("-- classic")
#
# result = binary_search(store, target)
# print(result)
#
# result_python = bisect(store, target)
# print(result_python)
#
# print("-- lower")
#
# result = lower_bound(store, target)
# print(result)
#
# result_lower = bisect_left(store, target)
# print(result_lower)
#
# print("-- upper")
#
# result = upper_bound(store, target)
# print(result)
#
# result_upper = bisect_right(store, target)
# print(result_upper)


#
# n_count = int(input())
#
# n = input().split()
# n = n[0: n_count]
# n = [int(x) for x in n]
#
# print(n)
# # for _ in range(0, n_count):
# #     n.append(int(input()))

# n = [1, 3, 3, 3, 4, 6, 8]
# m = [3] # ,0,9
#
# for i in m:
#     r = upper_bound(n, i)
#     print(r)
#

#
# def CanBuild(milestones: list, new_cafe_count: int, max_dist: int) -> bool:
#     built = 0
#     last = 0
#
#     for i in range(0, len(milestones)):
#         while milestones[i] - last > max_dist and built <= new_cafe_count:
#             built += 1
#             last += max_dist
#
#         last = milestones[i]
#
#     return built <= new_cafe_count
#
#
# def run_task1():
#     x = input().split()
#     road_length = int(x[0])
#     new_cafe_count = int(x[1])
#     max_dist = int(x[2])
#     milestone_count = int(input())
#
#     milestones = input().split()
#     milestones = [int(x) for x in milestones]
#     milestones.append(road_length)
#     milestones = sorted(milestones)
#
#     print("YES" if CanBuild(milestones, new_cafe_count, max_dist) else "NO")
#
#
# # run_task1()
#
# def run_task2():
#     # x = input().split()
#     road_length = 14  # int(x[0])
#     new_cafe_count = 4  # int(x[1])
#
#     milestone_count = 2  #int(input())
#
#     milestones = [4, 10]  #input().split()
#     milestones = [int(x) for x in milestones]
#     milestones.append(road_length)
#     milestones = sorted(milestones)
#
#     l = 1
#     r = road_length
#
#     while l <= r:
#         m = int(l + (r - l) / 2)
#
#         if CanBuild(milestones, new_cafe_count, m):
#             r = m - 1
#         else:
#             l = m + 1
#
#     print(int(r) + 1)



# # https://leetcode.com/problems/first-bad-version/
#
# def isBadVersion(version: int):
#     pass
#
#
# def binary_search_by_answer(n):
#     l = 1
#     r = n
#     while l <= r:
#         m = l + (r - l) / 2
#
#         if isBadVersion(m):
#             r = m - 1
#         else:
#             l = m + 1
#
#         return r + 1


# user_input = input().split()
# user_input = [int(x) for x in user_input]
# money, price1, price2 = [2, 1, 1]  # user_input
#
# print(money)

n = 4#int(input())
# values = input().split()
values = [3,1,4,2]#[1, 5 ,4, 3, 2, 12]#[int(x) for x in values]

if values[0] < values[len(values)-1]:
    print(len(values)-2)
else:
    print(0)