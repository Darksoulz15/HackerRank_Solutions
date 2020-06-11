studentList= []
sortedScore = []
nameSort  = []
for i in range(int(input())):
    name = input()
    score = float(input())
    studentList.append([name, score])
    #this for loop takes the input parameters and create a nested list which will be like - [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]


#sortedScore = sorted({s[1] for s in studentList})#uncomment this and comment the below three lines of code still the code will work

#the comprehented form of code is the above piece of code it is abrivated as below 3 lines of code ie. the above single line of code is abrivated as following you can either use the above single line of code or below single line of code 


for score_names in studentList:
    sortedScore.append(score_names[1])
    sortedScore = sorted(set(sortedScore))

# sortedScore is a list containing the scores of all the students in a increasing order
#score_names[1] means the "scores" from the studentList 
#score_names[0] means the "names" from the studentList
#set ('{}') is used in order to remove the duplicate entry


#nameSort = sorted(s[0] for s in studentList if s[1] == sortedScore[1]) #uncomment this and comment the below three lines of code still the code will work

#similarly as mentioned for sortedScore the above and below are the comprehention and abrivation of nameSort

for score_names in studentList:
    if score_names[1] == sortedScore[1]:
        nameSort.append(str(score_names[0]))
        nameSort = sorted(list(nameSort))


#sortedScore[1] denotes the second lowest score in the list so it is compared to check the entries in the studentList and when it is equal the corresponding name is printed 
#since the join can take only "string" as parameter namesSort is typecasted to string

print('\n'.join(nameSort))
