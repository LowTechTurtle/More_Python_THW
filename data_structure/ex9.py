import argparse, sys, re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--regex', action = 'store_true')
parser.add_argument('pattern')
parser.add_argument('file', nargs = '*')
args = parser.parse_args()
stdin = False
part = args.pattern.split('/')
if (not args.regex):
    if ('s' in part):
        try:
            if (args.file[0]) and (Path(args.file[0]).resolve().is_file()):
                with open(Path(args.file[0]).resolve()) as file:
                    for line in file:
                        if 'g' in part:
                            print(line.replace(part[1], part[2]), end='')
                        else: 
                            print(line.replace(part[1], part[2], 1), end='')
        except IndexError:
            stdin = True
        except:
            print('Unknown error has occured #1')
        if stdin:
            with open('ex9_stdin', 'w') as file:
                file.write(sys.stdin.read())
            with open('ex9_stdin') as file:
                for line in file:
                    if 'g' in part:
                        print(line.replace(part[1], part[2]), end='')
                    else:
                        print(line.replace(part[1], part[2], 1), end='')
else :
    if ('s' in part):
        try:
            if (args.file[0]) and (Path(args.file[0]).resolve().is_file()):
                with open(Path(args.file[0]).resolve()) as file:
                    for line in file:
                        result = re.findall(part[1], line)
                        if result != []:
                            if 'g' in part:
                                print(line.replace(result[0], part[2]), end='')
                            if (not ('g' in part)):
                                print(line.replace(result[0], part[2], 1), end='')
                        else:
                            print(line, end='')
        except IndexError:
            stdin = True
        except:
            print('Unknown error has occured #2')
        if stdin:
            with open('ex9_stdin', 'w') as file:
                file.write(sys.stdin.read())
            with open('ex9_stdin') as file:
                for line in file:
                    result = re.findall(part[1], line)
                    if result != []:
                        if 'g' in part:
                            print(line.replace(result[0], part[2]), end='')
                        if (not ('g' in part)):
                            print(line.replace(result[0], part[2], 1), end='')
                    else:
                        print(line, end='')

