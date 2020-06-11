# Enter your code here. Read input from STDIN. Print output to STDOUT
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

"""
sep = '' - code for disabling the softspace feature 
print('G','F','G', sep='') 
output:
GFG

key = order.index - we have already defined the order string so each input element is compared with the index of the order string ie. starting from a till 8 and it is sorted acordingly

in generl list.index(element) will give the index position of that element
"""
