from string import ascii_lowercase, ascii_uppercase
from random import choice, randint, shuffle
from Dictionaries import uppercasedict as updict
from Dictionaries import lowercasedict as lowdict
from os import system
import argparse
import sys

sys.path.insert (0, '~/Desktop/Matteo/Informatica/Python/Password/Dictionaries')

pool = []
letters = []
password = ''

parser = argparse.ArgumentParser()
parser.add_argument('--polimi', nargs='*')
parser.add_argument('--spid', nargs='*')
args = vars(parser.parse_args())
polimi = True if args['polimi'] == [] else False
spid = True if args['spid'] == [] and not polimi else False

# LOWERCASE #
for i in range(4):
    pool.append(choice(ascii_lowercase))

# UPPERCASE #
for i in range(2):
    pool.append(choice(ascii_uppercase))

# NUMBER #
for i  in range(2):
    pool.append(str(randint(0,9)))

if spid:
    pool += '!'

# PASSWORD #
shuffle(pool)
password = ''.join(pool)

for i in range(len(password)):
    if password[i] in updict.upperdict:
        letters.append(updict.upperdict[password[i]])
    elif password[i] in lowdict.lowerdict:
        letters.append(lowdict.lowerdict[password[i]])
    else:
        letters.append(password[i])

# FILE #
if polimi:
    file = open('polimi.txt', 'w')
elif spid:
    file = open('spid.txt', 'w')

file.write(password + '\n')
file.write(str( pool ) + '\n')
file.write(str( letters ))
file.close()

# OPEN FILE #
if polimi:
    command = 'gedit ~/polimi.txt &'
elif spid:
    command = 'gedit ~/password.txt &'
system(command)
