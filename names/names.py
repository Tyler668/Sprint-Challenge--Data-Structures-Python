import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open("C:\\Users\\tyler\\Documents\\github\\Sprint-Challenge--Data-Structures-Python\\names\\names_1.txt", 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("C:\\Users\\tyler\\Documents\\github\\Sprint-Challenge--Data-Structures-Python\\names\\names_2.txt", 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements


# name1 = BSTNode(names_1[0])
# for name in names_1:
#     name1.insert(name) 

# for name in names_2:
#     if name1.contains(name):
#         duplicates.append(name)


duplicates = list(set(names_1).intersection(names_2))




# duplicates.sort()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"{len(duplicates2)} duplicates:\n\n{', '.join(duplicates)}\n\n")


print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# Stretch
