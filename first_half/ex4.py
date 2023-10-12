from sys import argv
from re import search, findall
list_arg = argv
verbose = 0 
interactive = 0
arg_q = 0
arg_w = 0
arg_e = 0
for i in range(1, len(list_arg)):
    try:
        x = findall('-[hvis]+', list_arg[i])
        list_argument = list(x[0])
        if 'h' in list_argument:
            print('Help message for ex4 written in python 3.')
        if 'v' in list_argument:
            verbose = 1
        if 's' in list_argument:
            verbose = -1
        if 'i' in list_argument:
            interactive = 1
    except:
        pass
    if list_arg[i] == '-q':
        arg_q = i+1
    elif list_arg[i] == '-w':
        arg_w = i+1
    elif list_arg[i] == '-e':
        arg_e = i+1
       

    if i == arg_q:
        print(f'i need to do {list_arg[i]} from option -q')
    elif i == arg_w:
        print(f'i need to do {list_arg[i]} from option -w')
    elif i == arg_e:
        print(f'i need to do {list_arg[i]} from option -e')



        
        
        
