if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *percent = input().split()#only the first variable will be stored in name. rest all the other space seperated entries falls within the *percent as a list     
        scores = list(map(float, percent))
        student_marks[name] = scores #student_marks[name] will store the marks of the corresponding name in a dictionary(data structure)
    query_name = input() #the final query_name which is out of the loop takes in the name of student for whom we need the average to be calculated.
#Eloborated explaination for name,*percent with examples
"""
So if you had:

>>> first, *rest = input().split()
>>> print(first)
>>> print(*rest)
and ran it and typed in "hello my name is bob" It would print out

hello
['my', 'name', 'is', 'bob']
Another example would be this:

>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2,3,4])
It can also be used in any position which can lead to some interesting situations

>>> a, *middle, c = range(4)
>>> a, middle, c
(0, [1,2], 3)
"""

average = sum(student_marks[query_name])/3 #sum function adds up all the elements of list and divied by "3" gives the average since there are only 3 subjects given
average = "{:.2f}".format(average) #the "{:.2f}"format function helps to produce the output float to upto only 2 precision
print(average)
