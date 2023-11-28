#1 Read expenses.txt and print out all the expenses over $2000.
lines = [line.strip() for line in open('expenses.txt')]
for item in lines:
    if int(item) > 2000:
        print(item, end=' ')
print()



#2 Read expenses.txt, add 10% tax to each and write to a new file.
output_file = open('new_expenses.txt', 'w')
lines = [line.strip() for line in open('expenses.txt')]
for item in lines:
    print('{:.2f}'.format(int(item)*1.1), file=output_file)
print()



#3 Read secret_message.txt and print out the first letter of each line.
lines = [line.strip() for line in open('secret_message.txt')]
s = ''
for item in lines:
    s += item[0]
print(s)



#4 Use wordlist.txt to do a few things
words = [line.strip() for line in open('wordlist.txt')]

#a words that contain "quo".
for word in words:
    if 'quot' in word:
        print(word, end=' ')
print()

#b Percentage of words the contain all the vowels.
count = 0
for word in words:
    if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
        count += 1
print(count/len(words)*100)

#c Average word length
total = 0
for word in words:
    total += len(word)
print(total/len(words))

#d All words >= 6 letters that start and end with same three letters.
for word in words:
    if len(word) >= 6 and word[:3] == word[-3:]:
        print(word, end=' ')
print()        

#e Longest word that starts and ends with the same letter.
longest = 'a'
for word in words:
    if word[0] == word[-1] and len(word) > len(longest):
        longest = word
print(longest)

#f All words that contain four alphabetically consecutive letters.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for word in words:
    for i in range(23):
        if alphabet[i:i+3] in word:
            print(word, end=' ')
            break
print()


#5 Read from wordlist.txt and create a new file of all the words that are 5 letters or less
output_file = open('new_wordlist.txt', 'w')
lines = [line.strip() for line in open('wordlist.txt')]
for line in lines:
    if len(line) <= 5:
        print(line, file=output_file)
output_file.close()



#6 Given files of first and last names, create 10 random names.
from random import choice
first = [line.strip() for line in open('first_names.txt')]
last = [line.strip() for line in open('last_names.txt')]

for i in range(10):
    print(choice(first), choice(last))



#7 Given population.txt that has country names and populations, print all countries whose names start with G and have at least 500,000 people.
lines = [line.strip() for line in open('population.txt')]
for line in lines:
    L = line.split('\t')
    country = L[0]
    population = int(L[1])
    if country[0] == 'G' and population >= 500000:
        print(country, population)



#8 Grade paragraphs from ~studentParagraphs.txt~ based on length.
text = open('studentParagraphs.txt').read()
L = text.split('\n\n')
for x in L:
    name, paragraph = x.split(': ')
    if len(paragraph) >= 200:
        grade = 'A'
    elif len(paragraph) >= 150:
        grade = 'B'
    elif len(paragraph) >= 100:
        grade = 'C'
    elif len(paragraph) >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print(name, grade)
    
    

#9 Read elements.txt and reformat, writing to a new file.
output_file = open('new_elements.txt', 'w')
lines = [line.strip() for line in open('elements.txt')]
for line in lines:
    L = line.split(' - ')
    print(L[1], L[0], sep=',', file=output_file)
output_file.close()

    

#10 Given a file baseball.txt of baseball stats, print out all the players that hit at least 20 homeruns with an average of at least .300.
lines = [line.strip() for line in open('baseball.txt')]
for line in lines:
    L = line.split('\t')
    name = L[0]
    team = L[1]
    home_runs = L[8]
    average = L[14]
    if int(home_runs) >= 20 and float(average) >= .300:
        print(name, team, home_runs, average)



#11 Read from high_temperatures.txt, reformat, and rewrite to new file.
output_file = open('new_high_temperatures.txt', 'w')
lines = [line.strip() for line in open('high_temperatures.txt')]
month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
for line in lines:
    L = line.split()
    month, day = [x for x in L[0].split('/')]
    temp = round(5/9*(int(L[1])-32), 0)
    print(month_names[int(month)-1] + ' ' + day + ' ' + str(temp), file=output_file)
output_file.close()



#12 Read countries.txt and create a list of lists of all the A countries, B countries, etc.
lines = [line.strip() for line in open('countries.txt')]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
L = [[] for i in range(26)]
for line in lines:
    L[alphabet.index(line[0].lower())].append(line)
print(L)



#13 Use wordlist.txt to find all the words that can be made from a user's string
words = [line.strip() for line in open('wordlist.txt')]
s = input('Enter a string of lowercase letters: ')
d = {} # dictionary of frequencies in user's word
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
for word in words:
    e = {} # dictionary of frequencies in current word
    for c in word:
        if c in e:
            e[c] += 1
        else:
            e[c] = 1
    okay = True
    for c in e:
        if c not in d or e[c] > d[c]:
            okay = False
    if okay:
        print(word, end=' ')
print()



#14 Use countries.txt, ask for country name and a number, find country that is n lines before given country, wrapping around if needed.
lines = [line.strip() for line in open('countries.txt')]
country = input('Enter a country name: ')
country = country.lower().capitalize()
if country not in lines:
    print('That name is not in the list.')
else:    
    n = eval(input('Enter a number: '))
    print('N countries before:', lines[(lines.index(country)-n)%len(lines)])



#15 Using football_teams.txt and basketball_teams.txt, find NFL team nickname where if you remove a single letter, you get a basketball team nickname.    
football = [line.strip() for line in open('football_teams.txt')]
basketball = [line.strip() for line in open('basketball_teams.txt')]

for team in football:
    for i in range(len(team)):
        if team[:i] + team[i+1:] in basketball:
            print(team, team[:i] + team[i+1:])



#16 Create word frequency dictionary for romeoandjuliet.txt.
text = open('romeoandjuliet.txt').read()
for c in '!@#$%^&*()+=[{]}|\\;:",<>.?/':
    text = text.replace(c, '')
text = text.replace('\n', ' ')    
text = text.lower()
d = {}
for word in text.split():
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(sorted(list(d.items()), key=lambda x:-x[1])[:10])



#17 Guess-a-number with a save-game feature.
from random import randint

restart = input('Restart a game (r) or start from scratch (s)? ')
if restart == 'r':
    text = open('guess_a_number.txt').read()
    right, wrong = [int(x) for x in text.split()]
else:
    right = wrong = 0
keep_going = True
while keep_going:
    r = randint(1, 5)
    guess = eval(input('Enter your guess: '))
    if guess == r:
        print('Right!')
        right += 1
    else:
        print('Wrong.')
        wrong += 1
    print('You have gotten', right, 'right, and', wrong, 'wrong.')
    response = input('Keep going? (y/n): ')
    if response == 'n':
        keep_going = False
        output_file = open('guess_a_number.txt', 'w')
        print(right, wrong, file=output_file)
        output_file.close()



#18 continents.txt has country names arranged by continent.  Use it to write a quiz giving a country and asking what continent it is on.
from random import choice

lines = [line.strip() for line in open('continents.txt')]
current_continent = ''
d = {}
for line in lines:
    if len(line) > 0 and line == line.upper():  # Continent names are in upper case
        current_continent = line
    elif len(line) > 0: # not a blank line
        d[line] = current_continent

country = choice(list(d.keys()))
ans = input('What continent is ' + country + ' on? ')
if ans.upper() == d[country]:
    print('Right!')
else:
    print('Wrong.  Answer is', d[country])



#19 Read multiple_choice.txt and reorder the answer choices of each question.
from random import shuffle

alphabet = 'abcdefghijklmnopqrstuvwxyz'
output_file = open('new_multiple_choice.txt', 'w')
lines = [line.strip() for line in open('multiple_choice.txt')]
for line in lines:
    if len(line) > 0 and line[0].isdigit():
        print(line, file=output_file)
        choices = []
    elif len(line) > 0 and line[0] == '(':
        choices.append(line[4:]) # only include answer, not letter
    else: # blank line signals question is done
        shuffle(choices)
        for i in range(len(choices)):
            print('(' + alphabet[i] + ')', choices[i], file=output_file)
        print(file=output_file) # blank line
# These three lines are for the last question, since there won't be a blank line at the end of the file to signal that a question is done.
shuffle(choices)
for i in range(len(choices)):
    print('(' + alphabet[i] + ')', choices[i], file=output_file)
output_file.close()



#20 Read high_temperatures.txt and find the 30-day period over which there is the biggest increase in high temperature.
lines = [line.strip() for line in open('high_temperatures.txt')]

largest = 0
values = []
for i in range(len(lines)):
    date, temp = lines[i].split(' ')
    date30, temp30 = lines[(i-30)%365].split(' ')
    diff = int(temp) - int(temp30)
    if  diff > largest:
        largest = diff
        values = [date30 + ' to ' + date + '   ' + temp30 + '-' + temp]
    elif diff == largest:
        values.append(date30 + ' to ' + date + '   ' + temp30 + '-' + temp)

for x in values:
    print(x)
    


#21 Ask user to enter two NFL team names, read nfl1978-2013.csv, and print out all the games where either one of the two teams shut out the other.
lines = [line.strip() for line in open('nfl1978-2013.csv')]
t1 = input('Enter team 1 (full name required): ').lower()
t2 = input('Enter team 2 (full name required): ').lower()
for line in lines[1:]:
    date, team1, score1, team2, score2 = line.split(',')
    if ((team1.lower() == t1 and team2.lower() == t2) or\
        (team2.lower() == t1 and team1.lower() == t2)) and\
       (int(score1) == 0 or int(score2) == 0):
        print(line)



#22 Read the file nfl_scores.txt and print out all the scores that have never happened.
lines = [line.strip() for line in open('nfl_scores.txt')]
d = {}
for line in lines[1:]:
    L = line.split(',')
    winning_score = int(L[2])
    losing_score = int(L[3])
    if winning_score in d:
        d[winning_score].append(losing_score)
    elif winning_score < 20: 
        d[winning_score] = [losing_score]
for i in range(20):
    if i not in d and i != 1:
        for j in range(i+1):
            print(i, j, sep='-', end=', ')
for x in d:
    for y in range(x+1):
        if y not in d[x] and  y != 1:
            print(x, y, sep='-', end=', ')
print()
