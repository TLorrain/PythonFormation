# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 17:51:08 2017

@author: t.lorrain
"""

#A Donuts
def donuts(count):
    output=''  
    if count >= 10:
        output='Number of donuts: many'
    else: output = 'Number of donuts: %s' %(count)
    return output
    
#B Both_ends
def both_ends(s):
    output=''
    TwoFirst= s[:2]
    TwoLast= s[-2:]
    if len(s) < 2:
        output=''
    else: output = '%s%s' %(TwoFirst,TwoLast)
    return output
    
#C Fix_start
def fix_start(s):
    FirstLetter=s[0]
    s = s.replace(FirstLetter,'*')
    output = FirstLetter + s[1:]
    return output
    
#D MixUp
def mix_up(a, b):
    New_a = '%s%s' %(b[0:2],a[2:])
    New_b = '%s%s' %(a[0:2],b[2:])
    output = '%s %s' %(New_a,New_b)
    return output
    
#D' Verification of above functions

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

main()

#D'' Verbing

""" Not done Yet ! """

"""
def verbing(s):
    out
    if len(s) >=3:
        else: pass
    return output"""

#E Not_bad

""" Not done Yet ! """

#F front_back

""" Not done Yet ! """

#F' Verification of above functions
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')
    
main()
