print("Welcome to Destined Hearts.")
Your_name=input("What's your name?\n")
Lover=input("Lovers name?\n")
N=Your_name.lower()
L=Lover.lower()
N=(Your_name.lower()+ Lover.lower())
A=N.count("t")+N.count("r")+N.count("u")+N.count("e")
B=N.count("l")+N.count("o")+N.count("v")+N.count("e")
love_score=int(str(A)+ str (B))
if (love_score <10) or (love_score>90):
    print(f"Your score is {love_score},you go together like coke and mentos.")
elif(love_score >= 40) and (love_score<=50):
    print(f"Your score is {love_score},you are alright.")
else:
    print(f"Your score is {love_score}.")
