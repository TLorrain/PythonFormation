# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:39:26 2017

@author: t.lorrain
"""

#A  match_ends
def match_ends(words): 
    x=0
    for entry in words:
        if (len(entry)>=2) and (entry[0]==entry[-1]):
            x+=1
    return x

#B  front_x
def front_x(words): 
    List_BeginWithX=[]  
    List_BeginWithoutX=[]
    List_Sorted=[]
    for entry in words:
        if entry[0]=='x':
            List_BeginWithX.append(entry) 
        else: 
            List_BeginWithoutX.append(entry)
        List_BeginWithX.sort()        
        List_BeginWithoutX.sort()
        List_Sorted = List_BeginWithX+List_BeginWithoutX
    return List_Sorted
 
 #C  sort_last
def sort_last(tuples): 
    output = sorted(tuples,key= lambda x: x[-1])
    return output
    
#C' Validation of above functions
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
         
main()

#D Remove_adjacent

[1, 2, 2, 3]

def remove_adjacent(nums):
    List_Clean = []
    for i in nums:
        if len(List_Clean)==0 or i != List_Clean[-1]:
            List_Clean.append(i)
    return List_Clean
 
#E linear_merge
def linear_merge(list1, list2):
    List_Fusion=[]
    List_Fusion = (list1 + list2)
    List_Fusion.sort()
    return List_Fusion
   
#E' Validation of above functions
def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])
        
main()
