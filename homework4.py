#########
# Write a python program to create all possible strings using the letters 'a', 'e', 'i', 'o', 'u'. Each character should only be used once.
#########
# import itertools
# [print(''.join(i)) for i in itertools.permutations('aeiou')]

# Bruteforce
# for i in range(0, 5):
#     for j in range(0, 5):
#         for k in range(0, 5):
#             for l in range(0, 5):
#                 for m in range(0, 5):
#                     if (i != j and i != k and i != l and i != m and j != k and j != l and j != m and k != l and k != m and l != m):
#                         print('aeiou'[i] + 'aeiou'[j] + 'aeiou'[k] + 'aeiou'[l] + 'aeiou'[m])
