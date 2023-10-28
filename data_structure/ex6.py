import glob, argparse, subprocess
import re

parser = argparse.ArgumentParser(prog = 'lesserfind',
                                 description = 'a lesser version of find command')

parser.add_argument('path')
parser.add_argument('--name', default = '*', nargs = '+')
parser.add_argument('-exec')
parser.add_argument('-type', choices = ['f', 'd', 'l'])
args = parser.parse_args()
savefile = open('ex6_savefile')
subprocess.run(['bash', '-c', f'ls -RlA {args.path} > ex6_savefile'])
if re.findall('.*/$', args.path) == None:
    path = args.path + '/'
else:
    path = args.path
path_list = []
name = args.name[0]
for i in glob.glob(f'{path}**/{name}', recursive = True):
    path_list.append(i)

for line in savefile:
    if args.type == 'd':
        if re.findall('^d*', line) == ['d']:
            print(line, end = '')

        else:
            pass

    elif args.type =='f':
        if args.type == 'f':
            if re.findall('^-*', line) == ['-']:
                print(line, end = '')
            else:
                pass

    elif args.type == 'l':
        if re.finall('^l*', line) == ['l']:
            print(line, end = '')
        else:
            pass

