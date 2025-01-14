ll = ["amey", 11, "gawade", True , 11.11]

ll[3] = not[ll]

print(ll[3])

nums = [1,4,2,77,43,88,11,9]

nums.sort()
print(nums)

ll.append("python")
print(ll)

ll.insert(3,39)
print(ll)

v = ll.pop(2)
print(v)
print(ll)

nums.remove(43)
print(nums)


#extends and add list from the another list or also can do like this to add multiple values li.extend([1,2,3,5])
ll.extend(nums)
print(ll)

#counts the occurence of the value in the list integer, string.......
c = ll.count(11)
print(f"count value is {c}")

d = ll.count("amey")
print(d)

print(ll.index(11))