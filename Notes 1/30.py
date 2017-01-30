def fun(param):
    print(param)

fun(10)



# anonymous functions with lambda function (function shortcut)
# obj_var = lambda params: function
# make a lambda function to add numbers
add_two = lambda num1,num2: num1 + num2
print(add_two(2,3))


print()
# iterating through lists
this_list = [2, 4, 6, 8, 10]
for number in this_list:
    print(number)
    number += 1
print(this_list)

for i in range(len(this_list)):
    print(this_list[i])
    this_list[i] += 1
print(this_list)

# python's map function
# map(function, list)
squares = (map(lambda x: x **2, this_list))
print(list(squares))
# this will iterate through the entire list and will perform the function on every number in the list
print()

# index and slicing lists
my_list = [1,2,3,4,5,6,7]
my_list2d = [[10,20], [30,40] , [50,60]]

print(my_list[1:4])
print(my_list2d[1][1])
print(my_list2d[1:][1][1])

# list methods
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

# append (adds to the end of the list)
a.append(4)
print(a)

# extend (adds two lists together)
a.extend([5,6,7])
a.extend(b)
print(a)

print()
# insert (places an object at the index) (index, value)
b.insert(2, 100) # puts a 100 in index 2
b[2] = "World" # you can always override
b[3] = "world"
print(b)

# remove (item you want to remove, only removes one at a time)
b.remove("World")
print(b)

# pop (takes the last item off the list)
print(c)
next_in_line = c.pop()
print(c)
print(next_in_line)

print()
# count (how many of these do I have in the list
print(a.count(4))


# reverse
print(c.reverse())
