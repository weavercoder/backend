#1 BankAccount
class BankAccount:
    def __init__(self, name, amount, interest_rate):
        self.name = name
        self.amount = amount
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.amount *= (1 + self.interest_rate / 100)

account = BankAccount('Juan De Hattatime', 1000, 3)
account.apply_interest()
print(account.amount)
account.interest_rate = 2
account.apply_interest()
print(account.amount)



#2 Item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return '{:s}, {:.2f}'.format(self.name, self.price)

item = Item('hat', 12.40)
print(item)



#3 ShoppingCart
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def remove_items(self, name):
        self.items = [item for item in self.items if item.name != name]
        
    def __str__(self):
        return '\n'.join(str(item) for item in self.items)
        
cart = ShoppingCart()
cart.add(Item('shirt', 18.99))
cart.add(Item('shirt', 22.59))
cart.add(Item('car', 22400))
cart.add(Item('lettuce', 1.49))
print(cart)
cart.remove_items('shirt')
print(cart)



#4 RestaurantCheck
class RestaurantCheck:
    def __init__(self, check_number, sales_tax_percent, subtotal, table_number, server_name):
        self.check_number = check_number
        self.sales_tax_percent = sales_tax_percent
        self.subtotal = subtotal
        self.table_number = table_number
        self.server_name = server_name

    def calculate_total(self):
        return self.subtotal * (1+self.sales_tax_percent/100)

    def print_check(self):
        output_file = open('check' + str(self.check_number) + '.txt', 'w')
        print('Check Number:', self.check_number, file=output_file)
        print('Sales tax: ', self.sales_tax_percent, '%', sep='', file=output_file)
        print('Subtotal: {:.2f}'.format(self.subtotal), file=output_file)
        print('Total: {:.2f}'.format(self.calculate_total()), file=output_file)
        print('Table Number:', self.table_number, file=output_file)
        print('Server:', self.server_name, file=output_file)
        output_file.close()

check = RestaurantCheck(443, 6, 23.14, 'Sonic the Hedgehog', 17)
check.print_check()



#5 Ticket
class Ticket:
    def __init__(self, cost, time):
        self.cost = cost
        self.time = time

    def __str__(self):
        return 'Ticket(' + str(self.cost) + ', ' + str(self.time) + ')'

    def is_evening_time(self):
        hour = int(self.time.split(':')[0])
        return 18 <= hour <= 23

    def bulk_discount(self, n):
        if 5 <= n < 9:
            return 10
        elif n >= 10:
            return 20
        else:
            return 0

ticket = Ticket(49.99, '19:00')
print(ticket)
print(ticket.is_evening_time())
print(ticket.bulk_discount(15))



#6 MovieTicket
class MovieTicket(Ticket):
    def __init__(self, cost, time, movie_name):
        self.cost = cost
        self.time = time
        self.movie_name = movie_name

    def __str__(self):
        return 'Ticket(' + str(self.cost) + ', ' + str(self.time) + ', ' + str(self.movie_name) + ')'

    def afternoon_discount(self):
        hour = int(self.time.split(':')[0])
        if 12 <= hour <= 17:
            return 10
        else:
            return 0
        
m_ticket = MovieTicket(49.99, '14:25', 'Snakes on a Plane')
print(m_ticket)
print(m_ticket.afternoon_discount())
print(m_ticket.is_evening_time())



#7 Course
class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.student_IDs = []

    def is_full(self):
        return len(self.student_IDs) >= self.capacity
    
    def add_student(self, x):
        if not self.is_full() and x not in self.student_IDs:        
            self.student_IDs.append(x)

course = Course('CompSci', 3)
course.add_student('123')
course.add_student('123')
course.add_student('456')
course.add_student('789')
course.add_student('9999')
print(course.is_full())
print(course.student_IDs)



#8 Avatar
from random import randint, sample
from time import sleep

class Avatar:
    def __init__(self, name, hit_points, attack_power, defense_power):
        self.name = name
        self.hit_points = hit_points
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self):
        return randint(1, self.attack_power)

    def defend(self, attack_amount):
        damage = max(attack_amount - self.defense_power, 0)
        self.hit_points -= damage
        return damage

    def is_alive(self):
        return self.hit_points > 0

L = [Avatar('Ogre', 40, 30, 3),
     Avatar('Warrior', 100, 20, 5),
     Avatar('Paladin', 80, 10, 8)]

while len(L) > 1:
    attacker, defender = sample(L, 2)
    attack_amount = attacker.attack()
    damage = defender.defend(attack_amount)
    print(attacker.name, 'attacks!')
    print(defender.name, 'takes', damage, 'damage.')
    if not defender.is_alive():
        print(defender.name, 'is defeated.')
        L.remove(defender)
    for x in L:
        print(x.name, '---', x.hit_points)
    print()
    sleep(.5)



#9 Fighter and Mage
from random import randint

class Fighter(Avatar):
    def special_power(self):
        if randint(1, 5) == 1:
            return 2*self.attack_power
        else:
            return 0

class Mage(Avatar):
    def special_power(self):
        self.hit_points += 10

fighter = Fighter('Fighter', 100, 40, 5)
mage = Mage('Mage', 100, 40, 5)
attacker = fighter
defender = mage

while fighter.is_alive() and mage.is_alive():
    decision = input(attacker.name + ' -- attack (1) or special power (2): ')
    if decision == '2' and attacker == fighter:
        attack_amount = fighter.special_power()
        if attack_amount == 0:
            print('Failed.')
        else:
            damage = defender.defend(attack_amount)
            print(attacker.name, 'attacks!')
            print(defender.name, 'takes', damage, 'damage.')
    elif decision == '2' and attacker == mage:
        attacker.special_power()
        print(attacker.name, 'adds 10 hit points.')
    else:
        attack_amount = attacker.attack()
        damage = defender.defend(attack_amount)
        print(attacker.name, 'attacks!')
        print(defender.name, 'takes', damage, 'damage.')

    if not defender.is_alive():
        print(defender.name, 'has been defeated.')
    else:
        print(fighter.name, ' --- ', fighter.hit_points)
        print(mage.name, ' --- ', mage.hit_points)
        print()
    if attacker == fighter:
        attacker = mage
        defender = fighter
    else:
        attacker = fighter
        defender = mage
    


#10 Timer
import time

class Timer:
    def start(self):
        self.initial_time = time.time()
        
    def elapsed_seconds(self):
        return time.time() - self.initial_time
    
    def formatted_time(self, seconds):
        seconds = int(round(seconds, 0))
        minutes = seconds // 60
        seconds = seconds % 60
        return '{:d}:{:02d}'.format(minutes, seconds)

timer = Timer()
timer.start()
input('Enter something: ')
print(timer.elapsed_seconds())
timer2 = Timer()
timer2.start()
input('Enter something else: ')
print(timer2.elapsed_seconds())
print(timer.formatted_time(timer.elapsed_seconds()))



#11 Calendar
class Calendar:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        return self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0)

    def first_day(self, m):
        p = (14-m) // 12
        q = self.year - p
        r = q + q//4 - q//100 + q//400
        s = m + 12*p - 2
        t = (1 + r + (31*s)//12) % 7
        return t

    def print_calendar(self, m):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() and m == 2:
            days = 29
        else:
            days = month_days[m-1]

        c = 0
        for i in range(self.first_day(m)):
            c += 1
            print('    ', end='')
            
        for i in range(1, days+1):
            print('{:4d}'.format(i), end='')
            c += 1
            if c % 7 == 0:
                print()
        print()

calendar = Calendar(2018)
print(calendar.is_leap_year())
print(calendar.first_day(2))
calendar.print_calendar(2)
