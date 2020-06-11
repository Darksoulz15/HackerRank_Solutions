# Enter your code here. Read input from STDIN. Print output to STDOUT

N,n = int(input()),input().split()
print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))

"""

first the list is checked for the positive numbers 
and then it is cecking for the same number when revesed is also same(pallindrome)
then if it is true then it pints true or else it prints false
j[::-1] checks for reverse number 
actual syntax is "sequence[start:end:step_size]"

"""
