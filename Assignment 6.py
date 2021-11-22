import random


def quest(n):
    q = ["(Q) What is the smallest country in the world?", "(Q) How many players are there in a rugby league team?",
         "(Q) Who won the FIFA Women's World Cup in 2019?", "(Q) How long does Prime Minister’s Questions last?",
         "(Q) Which vitamin is the only one that you will not find in an egg?",
         "(Q) What is the capital of Westeros in Game of Thrones?",
         "(Q) One Direction is known for being the runners-up in The X Factor in 2010, but who came first?",
         "(Q) Which year was the Premier League founded?",
         "(Q) American singer Stefani Joanne Angelina Germanotta is best known by which stagename?",
         "(Q) Which singer was known amongst other things as 'The King of Pop'?",
         "(Q) There are McDonald’s one every continent except one",
         "(Q) Which footballer has the most Instagram followers in the world - as of 2020?",
         "(Q) Wayne Rooney scored his Premier League first goal against which team?",
         "(Q) What is Japanese sake made from?",
         "(Q) How many Members of Parliament (MPs) are there?",
         "(Q) In tennis, what piece of fruit is found at the top of the men's Wimbledon trophy?",
         "(Q) What is the longest river in the world?", "(Q) What's the biggest animal in the world?",
         "(Q) What's a baby rabbit called?", "(Q) In Harry Potter, what is the name of The Weasley's house?"]
    print(q[n])


def answer():
    ans = {"Vatican City": "A", "13": "C", "USA": "B", "30 minutes": "A", "Vitamin C": "A",
           "King’s Landing": "D", "Matt Cardle": "B", "1992": "D", "Lady Gaga": "B", "Michael Jackson": "B",
           "True": "A", "Cristiano Ronaldo": "B", "Arsenal": "A", "Rice": "A", "650": "D",
           "Pineapple": "C", "River Nile": "C", "The Blue Whale": "D", "A Kit": "A", "The Burrow": "B"}

    answer_v = list(ans.values())
    answer_k = list(ans.keys())
    return answer_v, answer_k


def option(n1):
    opt = ["A) Vatican City \nB) Republic Of San Marino \nC) Tuvalu \nD) Pricipality Of Monaco",
           "A) 11 \nB) 10 \nC) 13 \nD) 9",
           "A) Brazil  \nB) USA \nC) England \nD) Argentina",
           "A) 30 minutes \nB) 20 minutes \nC) 60 minutes \nD) 15 minutes",
           "A) Vitamin C \nB) Vitamin D \nC) Vitamin B \nD) Vitamin K",
           "A) Casterly Rock \nB) The Iron Islands \nC) Meereen \nD) King’s Landing",
           "A) Belle Amie \nB) Matt Cardle \nC) Nicolo Festa \nD) Storm Lee", "A) 1993 \nB) 1982 \nC) 1998 \nD) 1992",
           "A) Ariana Grande \nB) Lady Gaga \nC) Billie Eilish \nD) Dua Lipa",
           "A) Billy Joel \nB) Michael Jackson \nC) Madonna \nD) Phil Collins",
           "A) True \nB) False", "A) Neymar \nB) Cristiano Ronaldo \nC) Virat Kohli \nD) Selena Gomez",
           "A) Arsenal \nB) Chelsea \nC) Manchester United \nD) Leicester city",
            "A) Rice \nB) Bread \nC) Yeast \nD) Wheat", "A) 500 \nB) 450 \nC) 415 \nD) 650",
           "A) Apple \nB) Grapes \nC) Pineapple \nD) Guava",
           "A) Amazon \nB) Mississippi \nC) River Nile \nD) Yangtze",
           "A) Colossal Squid \nB) African Elephant \nC) Whale Shark \nD) The Blue Whale",
           "A) A Kit \nB) Bunny \nC) Lop \nD) Tapeti",
           "A) Wiltshire \nB) The Burrow \nC) Little Whinging \nD) Catchpole"]
    print(opt[n1])


def main():
    cont = "y"
    while cont == 'y' or cont == "Y":
        print()
        t = "QUIZ"
        print(t.center(120))
        score = 0
        ran_ind = random.sample(range(20), 4)
        for i in range(4):

            ind = ran_ind[i]
            quest(ind)
            print()
            option(ind)
            print()
            ans_in = input("Enter Your Option: ")
            if ans_in not in ["a", "A", "b", "B", "c", "C", "d", "D"]:
                print("Please choose a option from the above options!")
                ans_in = input("Enter Your Option: ")
            ans_in = ans_in.upper()
            answer_v, answer_k = answer()
            if ans_in == answer_v[ind]:
                score += 1
                print("Correct Answer!")
            else:
                score = score
                print("Incorrect Answer!\nThe Answer is:", answer_k[ind])
            print()
        print()
        print("Your Score is", score, "out of 4")
        print()
        cont = input("Do you want to play Again(Y/N)? : ")
        print()
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break


main()
