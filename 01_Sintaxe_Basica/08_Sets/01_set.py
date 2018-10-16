#!/usr/bin/env python3

x = set('spam')
y = {'h', 'a', 'm'}

print(x,y)

print(x & y)  # intersection
print(x | y) #union
print(x - y) # diference
print(x > y) # super set


# set comprehension
print({n**2 for n in [1,2,3,4,5]})

# filtering duplicates
print(list(set([1,2,1,3,1])))
print(set('spam') - set('ham')) # finding differences in collections
print(set('spam') == set('asmp'))

# sets also supports membership test operation
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])