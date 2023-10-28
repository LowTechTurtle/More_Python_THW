import re, argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('regex')
parser.add_argument('fos', nargs = '*', default = [])
args = parser.parse_args()

if len(args.fos) == 0:
    for line in sys.stdin:
        if re.findall(args.regex, line) != []:
            print(line, end='')

elif (len(args.fos) == 1):
    try:
        file = open(args.fos[0])
        for line in file:
            if re.findall(args.regex, line) != []:
                print(line, end='')
    except:
        string = args.fos[0]
        x = re.findall(args.regex, string)
        if x != []:
            print(string)

elif len(args.fos) >= 2:
    for file_ in args.fos:
        with open(file_) as file:
            for line in file:
                if re.findall(args.regex, line) != []:
                    print(line, end='')
