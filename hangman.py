import random

word_list=("canteen","scent","community","autopilot","foothold","spring","lunatic","unpredictability","vowel","turnaround")
word=word_list[random.randint(0,9)]

copy_word=word

obs_word=""
for char in word:
    obs_word+='*'

end_word=""
for char in word:
    end_word+='#'

tries=10

print("The game has begun, you have {} tries\n".format(tries))
print(obs_word)

guess=""
found=0
won=0

while tries>0:
    if won==1:
        break
    won=1
    guess=input("Guess a letter: ")
    found=0
    for c in word:
        if c==guess:
            found=1
            pos=word.find(c)
            word=word[:pos]+'#'+word[pos+1:]
            obs_word=obs_word[:pos]+c+obs_word[pos+1:]
    if found==1:
        print("\nCorrect!\n")
        print(obs_word)
        found=0
    else:
        print("\nWrong\n")
        tries-=1
        print("You have {} tries remaining".format(tries))
    for c in word:
        if c!='#':
            won=0
            break

if won==0:
    print("The word is {}.".format(copy_word))
    print("========= Game Over =========")
else:
    print("========= You've Won =========")
