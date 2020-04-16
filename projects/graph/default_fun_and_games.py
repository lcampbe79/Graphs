'''
A new list is created once when the function is defined, 
and the same list is used in each successive call.
Used for caching, fibonacci is best
'''
def foo(list_to_set, the_set=()):
    for item in list_to_set:
        the_set.add(item)
    print(the_set)

foo([1,2,3])
foo([4,5,6])