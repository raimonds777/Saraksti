print("Kuru no uzdevumiem vēlies realizēt")
print("Izvēlies ciparu")
print("1 - pirmo uzdevumu")
print("2 - otro uzdevumu")
print("3 - trešo uzdevumu")
print("____________________")
print("Tu es izvēlējies uzdevumu nr. ")


def 1.uzdevums

a = int(1)
b = int(2)
c = int(3)
d = int(4)

print(a, b, c, d)

mul=b*d;

print("Result",mul)


#2.uzd
visi_skaitli = []
for i in range(5):
  skaitlis = int(input("Ievadi skaitli intervālā [-10 ; 10]"))
  visi_skaitli.append(skaitlis)
print("saraksta garums ir ", len(visi_skaitli))
lielaki_skaitli = 0
if visi skaitli[0]> visi_skaitli[3]:
  lielaki_skaitli += 1
if visi_skaitli[1]> visi_skaitli[3]:
  lielaki_skaitli += 1
if visi_skaitli[2]> visi_skaitli[3]:
  lielaki_skaitli += 1
if visi_skaitli[4]> visi_skaitli[3]:
  lielaki_skaitli += 1
print(lielaki_skaitli)
print(visi_skaitli)

#3.uzd


def check_guess(guess, answer):

global score

still_guessing = True

attempt = 0

while still_guessing and attempt < 3:

if guess.lower() == answer.lower():

print("Correct Answer")

score = score + 1

still_guessing = False

else:

if attempt < 2:

guess = input("Sorry Wrong Answer, try again")

attempt = attempt + 1

if attempt == 3:

print("The Correct answer is ",answer )

score = 0

print("atbildi uz jautajumiem")

guess1 = input("popularaka programa kodešanai? ")

check_guess(guess1, "python")

guess2 = input("python autors ")

check_guess(guess2, "Gvido van Rosums")

guess3 = input("vai c++ ir programma kodešanai ja vai ne? ")

check_guess(guess3, "ja")

guess4 = input("vai tu māki programmet? ")

check_guess(guess4, "ja")

print("Your Score is "+ str(score))