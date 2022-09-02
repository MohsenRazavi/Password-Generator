# password generator

import random



lowers = [chr(i) for i in range(97, 123)]
uppers = [chr(i) for i in range(65,91)]
nums = [int(i) for i in range(0, 9)]
symbols = [chr(i) for i in range(32, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]

options = {
    'l' : lowers,
    'u' : uppers,
    'n' : nums,
    's' : symbols
}

user_options = []

pass_len = int(input('enter password length : '))

print('enter options y/n : ')

l = input('using lowers ? ')
if l == 'y':
    user_options.append('l')
u = input('using uppers ? ')
if l == 'u':
    user_options.append('u')
n = input('using nums ? ')
if n == 'y':
    user_options.append('n')
s = input('using symbols ? ')
if s == 'y':
    user_options.append('s')



result = ''



for _ in range(pass_len):
    result += str(random.choice(options[random.choice(user_options)]))


print(result)