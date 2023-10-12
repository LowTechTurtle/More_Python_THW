import argparse, pathlib, sys
parser =  argparse.ArgumentParser()
parser.add_argument('-d', '--delimeter', nargs = 1, type = str, default = '\t')
parser.add_argument('-f', '--field', nargs = 1, default = [])
parser.add_argument('-c', '--characters', nargs = 1, default =[])
parser.add_argument('file', nargs = '*')
args = parser.parse_args()
if args.field != []:
    field_list = list(args.field[0])
    if len(field_list) == 3:
        start_field = int(field_list[0])
        end_field = int(field_list[2])
    elif len(field_list) == 1:
        start_field = int(field_list[0])
        end_field = None
    elif len(field_list) == 0:
        start_field = None
        end_field = None

if args.characters != []:
    char_list = list(args.characters[0])
    if len(char_list) == 3:
        start_char = int(char_list[0])
        end_char = int(char_list[2])
    elif len(char_list) == 1:
        start_char = int(char_list[0])
        end_char = None
    elif len(char_list) == 0:
        start_char = None
        end_char = None


if (args.field != []) and (args.characters == []):
    for item in args.file:
        path = pathlib.Path(item)
        if path.is_file():
            with open(path.resolve()) as file:
                for line in file:
                    try:
                        x = line.split(args.delimeter[0])
                        if end_field:
                            for i in range(start_field-1, end_field):
                                print(x[i], end=' ')
                            print('\n', end='')
                        else:
                            start_field_ = start_field - 1
                            print(x[start_field_])
                    except:
                        print('', end='')
        else:
            print('Target needs to be a file.')
    if args.file == []:
        for line in sys.stdin:
            try:
                x = line.split(args.delimeter[0])
                if end_field:
                    for i in range(start_field-1, end_field):
                        print(x[i], end=' ')
                    print('\n', end='')
                else:
                    start_field_ = start_field - 1
                    print(x[start_field_])
            except:
                print('', end = '')


elif (args.field == []) and (args.characters != []):
    for item in args.file:
        path = pathlib.Path(item)
        if path.is_file():
            with open(path.resolve()) as file:
                for line in file:
                    try:
                        x = list(line)
                        if end_char:
                            for i in range(start_char-1, end_char):
                                print(x[i], end =' ')
                            print('\n', end='')
                        else:
                            start_char_ = start_char - 1
                            print(x[start_char_])
                    except:
                        print('', end='')

    if args.file == []:
        for line in sys.stdin:
            try:
                x = list(line)
                if end_char:
                    for i in range(start_char-1, end_char):
                        print(x[i], end=' ')
                    print('\n', end='')
                else:
                    start_char_ = start_char - 1
                    print(x[start_char_])
            except:
                print('', end='')

else:
    print('Choose only character cut or field cut')

