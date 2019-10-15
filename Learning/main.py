# This is file is created by Rohit Makhija while learning Python
# Date Started 03.Aug.2019

# Python Tutorials: New Boston
# FORMAT
# <Video Number> <Title>
#
# CODE 1
# -------
# CODE 2
#
# *** for reference / comments for function used
# End <Video Number> ==================================

# 1, 2, 3, 4, 5, 6, 7

# Basic of Python like print('Hello World'), variables,
# strings, lists, installing IDE, add substract, if else

# End 1, 2, 3, 4, 5, 6, 7 =================================

# 8
#foods = ["bacon", "tuna", "Ham", "salad", "beef"]
'''
for f in foods[:2]:
    print(f)
    print(len(f))
'''
# End 8 ====================================================

# 9 Range and while
#
# *** range(starting point, ending point, increment)
'''
for x in range(100, 400, 50):
    print(x)
'''
#------------------------------------------------------
'''
buttcrack = 5
while buttcrack < 10:
    print(buttcrack)
    buttcrack += 1
'''
# End 9 ====================================================

# 10 Comments and Break
'''
magicNumber = 26
# *** range(101) is shows range (0 to 100)
# how to print (Number, "String") print(9, "Bucky")

for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number")
        break
    else:
        print(n)
'''

# Homework Q. Make a program for multiple of 4
'''
for n in range(101):
    if((n % 4) is 0):
        print(n)
'''
# End 10 ====================================================

# 11 Continue
# Skip the numbers from range which are in numbersTaken
'''
numbersTaken = [2, 5, 12, 33, 17]

print("Here are the numbers that are still available:")
for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)
'''
# End 11 ====================================================

# 12 Functions
# Define a function by using "def" <Name of function>(arg1, ...):
'''
def beef():
    print("Functions are cool")

def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)

beef()
bitcoin_to_usd(1)
bitcoin_to_usd(13)
bitcoin_to_usd(23)
'''
# End 12 ====================================================


# 13 Return Values
'''
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

print(allowed_dating_age(26))
'''
# End 13 ====================================================


# 14 Default Values
'''
def get_gender(sex = 'Unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()
'''
# End 14 ====================================================


# 15 Variables Scope

# same as c / cpp
'''
def corn():
    a = 7823
    print(a)

def fudge():
    print(a)

corn()
fudge()
'''
# End 15 ====================================================


# 16 Keyowrd Arguments
'''
def dumb_sentence(name="Rohit", action="ate", item="chicken"):
    print(name, action, item)

dumb_sentence()
dumb_sentence("Bittu", "eats", "eggs")
dumb_sentence(item="sira", action="is")
'''
# End 16 ====================================================


# 17 Flexible Number of arguments
# Variable Arguments
'''
def add_number(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_number(3)
add_number(3,3,4,5,7)
add_number(7,0,928,202)
'''
# End 17 ====================================================


# 18 Unpacking Arguments

'''
def health_calculator(age, apples_ate, drinks_taken):
    answer = (100-age) + (apples_ate + 3.5) - (drinks_taken * 2)
    print(answer)

rohit_data = [25, 20, 0]

health_calculator(rohit_data[0], rohit_data[1], rohit_data[2])
# unpacking arg -- replace above line with below
health_calculator(*rohit_data)
'''
# End 18 ====================================================


# 19 Sets

# Useless to having same item twice
'''
groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'lotion', 'beer'}
print(groceries)

if 'milk' in groceries:
    print("already have it")
else:
    print("need it")
'''
# End 19 ====================================================


# 20 Dictionary

'''
classmates = {'Tony':'cool but smells', 'Emma': 'sits behind me', 'Lucy': 'asks too many questiosn'}
print(classmates)
print(classmates['Emma'])

# for key, value in Dictionary.items()
for k, v in classmates.items():
    print(k + v)
'''
# End 20 ====================================================


# 21 Modules

'''
import tuna
import random
tuna.fish()

x = random.randrange(1, 1000)
print(x)
'''
# End 21 ====================================================


# 22 Download an image from internet

'''
import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = "/home/latitude5490/ROHIT/Qt_Python/untitled/" + str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://www.facebook.com/photo.php?fbid=2055012541253135&set=a.105906569497085&type=3&theater")
print("downloaded")
'''
# End 22 ====================================================

# 23 How to read and write files

'''
fw = open('/home/latitude5490/ROHIT/Qt_Python/untitled/sample.txt', 'w')
fw.write('writing some stuffs in my text file\n')
fw.write('I like bacon')
fw.close()

fr = open('/home/latitude5490/ROHIT/Qt_Python/untitled/sample.txt', 'r')
text = fr.read()
print(text)
fw.close()
'''
# End 23 ====================================================


# 24 Downloading Files from the web

'''
from urllib import request
goog_url = 'http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv'

def download_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'/home/latitude5490/ROHIT/Qt_Python/untitled/goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_data(goog_url)
'''
# End 24 ====================================================
# 25, 26, 27 How to build Web Crawler
# Skipped
# End 25, 26, 27====================================================

# 28 Exceptions

'''
while True:
    try:
        print("try")
        number = int(input("Fav Number: "))
        print("tried")
        print(18/number)
        break
    except ValueError:
        print("Make sure to enter a number.")
    except ZeroDivisionError:
        print("Make sure to enter a number.")
    except:
        print("otherwise")
    finally:
        print("execute no matter what (error or not error)")
'''
# End 28 ===========================================================

# 29 Classes and Objects
'''
class Enemy:
    life = 3

    # self means use something with the same class.
    def attack(self):
        print("ouch!")
        self.life -= 1

        # Tip: Never check life = to Zero, life can go to negative
    def checkLife(self):
        if self.life <= 0:
            print("Dead")
        else:
            print(str(self.life) + " life left")

#Object
enemy1 = Enemy()
enemy1.attack()
enemy1.checkLife()

# Each object is copy of its class.
enemy2 = Enemy()
enemy2.checkLife()
'''
# End 29 ===========================================================


# 30 Init
'''
class Tuna:
    def __init__(self):
        print("init")

    def swim(self):
        print("Swim")

flipper = Tuna()
#__init__ is just like constructor. It is called when we call any other method of same class
flipper.swim()
'''
# ------------------------------------------------------------------
'''
class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()
'''
# End 30 ===========================================================

# 31 Class vs Instance
'''
class Girl:
    gender = 'female'           # Class Variable

    def __init__(self, name):
        self.name = name        # Instance Variable

r = Girl('Rachel')
s = Girl('Stanky')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
'''
# End 31 ===========================================================

# 32 Inheritance
'''
class Parent():
    def print_last_name(self):
        print('Makhija')

class Child(Parent):
    def print_first_name(self):
        print('Rohit')

    # function overridding
    def print_last_name(self):
        print('Singh')

rohit = Child()
rohit.print_first_name()
rohit.print_last_name()
'''
# End 32 ===========================================================

# 33 Multiple Inheritance
'''
class Mario():
    def move(self):
        print('I am moving !')

class Shroom():
    def eat_shroom(self):
        print('No I am Big !')

class BigMario(Mario, Shroom):
    pass                            # need a line but dont want to write code.

bm = BigMario()
bm.move()
bm.eat_shroom()
'''
# End 33 ===========================================================


# 34 Threading
'''
import threading

class RohitMessenger(threading.Thread):
    def run(self):
        for _ in range(10):              # loop for 10 times dont want to use a Variable
            print(threading.currentThread().getName())

x = RohitMessenger(name='Send out messages')
y = RohitMessenger(name='Receive messages')
x.start()
y.start()
'''
# End 34 ===========================================================

# 35 36 37 Word Frequencing counter Part-1
'''
import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class', 'index_singleListingTitles'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)

start('www.')
not completed this code
'''
# 35 36 37 =========================================================


# 38 Unpack List or Tuples
'''
item = ['December 23, 2015', 'Bread Gloves', 8.51]
date = item[0]
name = item[1]
price = item[2]
'''
# ------------------------------------------------------------------------
'''
# Unpacking of above variable list (same size Input = Output)
date, name, price = ['December 23, 2015', 'Bread Gloves', 8.51]
print(name)
'''
# -------------------------------------------------------------------------
'''
def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    print(avg)
    print("first = ", first)
    print("middle = ", middle)
    print("last = ", last)

drop_first_last([65, 67, 53, 75, 61])
drop_first_last([65, 67, 53, 75, 61, 90, 32])
'''
# End 38 ===========================================================


# 39 Zip
'''
first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)
# o/p Bucky Roberts, Tom Hanks, Taylor Swift

for a, b in names:
    print(a, b)
'''
# End 39 ===========================================================

# 40 Lambda
'''
answer = lambda x: x*7
print(answer(5))
'''
# End 40 ===========================================================


# 41 Min, Max and Sorting Dictionary
'''
stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YAHOO': 39.28,
    'AMAZON': 306.21,
    'APPLE': 99.76
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))

print(sorted(zip(stocks.values(), stocks.keys())))

'''
# End 41 ===========================================================

# 42 Pillow
'''
from PIL import Image

img = Image.open("/home/latitude5490/Pictures/Makhija/rohitmakhijaimage.png")
print(img.size)
print(img.format)

img.show()
'''
# End 42 ===========================================================

# 43 Cropping Images
'''
from PIL import Image

img = Image.open("rohitmakhijaSports.jpg")
area = (100, 100, 300, 375)
cropped_img = img.crop(area)

img.show()
cropped_img.show()
'''
# End 43 ===========================================================


# 44 Combine Images Together
'''
from PIL import Image

image1 = Image.open("/home/latitude5490/Pictures/Makhija/rohitmakhijaSports.jpg")
image2 = Image.open("/home/latitude5490/Pictures/Makhija/RohitMakhijaSports2.jpg")

area = (100, 100, 300, 300)
image1.paste(image2, area)

image1.show()
''' # not working
# End 44 ===========================================================

# 45 Getting Individual Channels
'''
from PIL import Image

image1 = Image.open("/home/latitude5490/Pictures/Makhija/rohitmakhijaSports.jpg")
#print(image1.mode) #RGB
r,g,b = image1.split() #returns Tuples
r.show()
g.show()
b.show()
'''
# End 45 ===========================================================


# 46 Awesome Merge Effect
'''
from PIL import Image

image1 = Image.open("/home/latitude5490/Pictures/Makhija/rohitmakhijaSports.jpg")
r,g,b = image1.split()

new_img = Image.merge("RGB", (b,g,r))
new_img.show()

# we can merge 2 different images but size should be same.
'''
# End 46 ===========================================================


# 47 Basic Transformation
'''
from PIL import Image

image1 = Image.open("/home/latitude5490/Pictures/Makhija/rohitmakhijaSports.jpg")
square = image1.resize((250, 250))
flip = image1.transpose(Image.FLIP_LEFT_RIGHT)
spin = image1.transpose(Image.ROTATE_90)

square.show()
flip.show()
spin.show()
'''
# End 47 ===========================================================


# 48 Modes and Filters
'''
from PIL import Image
# Below code is not working as expected
image1 = Image.open("/home/latitude5490/Pictures/Makhija/rohitmakhijaSports.jpg")
black_white = image1.convert("L") #Luminant ~ Black and White
image1.show()
'''
# -------------------------------------------------------------------
'''
from PIL import Image
from PIL import ImageFilter
image1 = Image.open("/home/latitude5490/Pictures/Makhija/rohitmakhijaSports.jpg")
blur = image1.filter(ImageFilter.BLUR)
detail = image1.filter(ImageFilter.DETAIL)
edges = image1.filter(ImageFilter.FIND_EDGES)
blur.show()
detail.show()
edges.show()
'''
# End 48 ===========================================================

# 49 Struct
'''
from struct import *

# Store as bytes data
packed_data = pack('iif', 6, 19, 4.73) # iif means ~ 2 intergers and a float
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get bytes data back to normal (b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
original_data = unpack('iif', packed_data)
print(original_data)
print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))
'''
# End 49 ===========================================================

# 50 Map
'''
income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

map(double_money, income)

new_income = list(map(double_money, income))
print(new_income)
'''
# End 50 ===========================================================

# 51 Bitwise Operator
'''
# Binary AND
a = 50          # 110010
b = 25          # 011001
c = a & b       # 010000
print(c)

# Binary RIGHT SHIFT
x = 240         # 11110000
y = x >> 2      # 00111100
print(y)
'''
# End 51 ===========================================================

# 52 Finding Largest or Smallest Items
'''
import heapq
grades = [32, 43, 654, 34, 132, 66, 99, 532]
# print largest 3 from the list
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'APPLE', 'price': 201},
    {'ticker': 'GOOGLE', 'price': 800},
    {'ticker': 'FB', 'price': 54},
    {'ticker': 'MS', 'price': 313},
    {'ticker': 'TUNA', 'price': 68},
]

print(heapq.nsmallest(2, stocks, key = lambda stock: stock['price']))
'''
# End 52 ===========================================================

# 53 Dictionary Calculations
'''
stocks = {
    'APPLE': 201,
    'GOOGLE': 800,
    'FB': 54,
    'MS': 313,
    'TUNA': 68,
}

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)
'''
# End 53 ===========================================================

# 54 Finding Most Frequent Items
'''
from collections import Counter

text = "latitude5490@rohit:~$ nmap -sV 192.168.1.1"\
"Starting Nmap 7.01 ( https://nmap.org ) at 2019-08-07 10:22 CDT"\
"Nmap scan report for Vission2020-dev (192.168.1.1)"\
"Host is up (0.0033s latency)."\
"Not shown: 986 closed ports"\
"PORT      STATE    SERVICE     VERSION"\
"22/tcp    filtered ssh"\
"24/tcp    open     ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)"\
"25/tcp    open     ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)"\
"26/tcp    open     ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)"\
"53/tcp    open     domain      dnsmasq 2.78"\
"80/tcp    open     http        lighttpd 1.4.39"\
"139/tcp   open     netbios-ssn Samba smbd 3.X (workgroup: WORKGROUP)"\
"443/tcp   filtered https"\
"445/tcp   open     netbios-ssn Samba smbd 3.X (workgroup: WORKGROUP)"\
"5002/tcp  open     rfe?"\
"5925/tcp  open     vnc         VNC (protocol 3.8)"\
"5959/tcp  open     vnc         VNC (protocol 3.8)"\
"10000/tcp open     http        lighttpd 1.4.39"\
"49152/tcp open     upnp        Portable SDK for UPnP devices 1.6.19 (Linux 3.10.39; UPnP 1.0)"\
"Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel, cpe:/o:linux:linux_kernel:3.10.39"\
""\
"Service detection performed. Please report any incorrect results at https://nmap.org/submit/ ."\
"Nmap done: 1 IP address (1 host up) scanned in 43.52 seconds"

words = text.split()
counter = Counter(words)

top_three = counter.most_common(3)
print(top_three)
'''
# End 54 ===========================================================

# 55 Dictionary Multiple Key Sorting
'''
from operator import itemgetter

users = [
    {'fname': 'Rohit', 'lname': 'Makhija'},
    {'fname': 'Bittu', 'lname': 'Pathak'},
    {'fname': 'Bhaiyu', 'lname': 'Byju'},
    {'fname': 'Likhit', 'lname': 'Badval'},
]

# it is not true sort coz when same fname or lname is present it will not give expected results
for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('-----------')
for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)
'''
# End 55 ===========================================================


# 56 Sorting Custom Objects
'''
from operator import attrgetter

class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

# Representation
    def __repr__(self):
        return self.name + ":" + str(self.user_id)

users = [
    User('Bucky', 43),
    User('Sally', 5),
    User('Tuna', 61),
    User('Brain', 2),
    User('Joby', 77)
]

for user in users:
    print(user)

print('--------')

for user in sorted(users, key=attrgetter('name')):
    print(user)

print('--------')

for user in sorted(users, key=attrgetter('user_id')):
    print(user)
'''
# End 56 ===========================================================


# ******* Congrats Makhija :D ********
# Finished 08.Aug.2019
