#Python programs on Shallow and Deep Copy

import copy
l1 = [2, 3, [4, 5]]
l2 = l1.copy()
l2[0] = 88
print("l1 =",l1)
print("l2 =",l2)

#Output
'''
l1 = [2, 3, [4, 5]]
l2 = [88, 3, [4, 5]]
'''

l1 = [10, 20, 30, [40]]
l2 = copy.deepcopy(l1)
l1[3][0] = 90
print("l1 =",l1)
print("l2 =",l2)

#Output
'''
l1 = [10, 20, 30, [90]]
l2 = [10, 20, 30, [40]]
'''

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list
new_list[2][2] = 9
print('Old List:', old_list)
print('New List:', new_list)

#Output
'''
Old List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
New List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)

#Output
'''
Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
'''