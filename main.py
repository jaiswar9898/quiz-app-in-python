#Dictorinaries contains keys and values 

q1 = """Which of the following is not keyword
a.Yes
b.assert
c.local
d.pass"""

q2 = """Which one of these is floor division
a./
b.//
c.%
d.None"""

q3= """Is Python case senstive when dealing with identifiers
a.Yes
b.assert
c.local
d.pass"""

q4 = """What is the output of this 3*1**3?
a.27
b.9
c.3
d.1"""

q5 = """"a"+"bc"=??
a.a
b.bc
c.bca
d.abc"""

questions = {q1:"a",q2:"a",q3:"b",q4:"c",q5:"d"}

name = input("enter your name")
print("hello")
score=0
for i in questions:
    print()
    print(i)
    
    ans = input("enter the answer (a/b/c/d)") # in bracket the a b c d will store its is neccesary to abcd option in extra bracket 
    if ans==questions[i]:
       print("correct answer got one point")
       score = score+1  # if answer will right then it will increment the score by adding one point 
       print("current score is:",score)
    else:
        print("wrong answer")
        score=score-1  #if wil wrong it wil dicrement the score by subtracting the one point 
        print("current score is:",score)
print("Final score is:",score)
