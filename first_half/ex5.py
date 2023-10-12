import argparse
import sys
parse = argparse.ArgumentParser(prog = 'catisdog', 
                                description = 'a lesser version of the cat command written by a turlte'
                                )

parse.add_argument('infile', nargs = '+', type = argparse.FileType('r'), default = sys.stdin)
parse.add_argument('-o', '--outfile', nargs = '?', type = argparse.FileType('a'), default = sys.stdout)
parse.add_argument('-n', '--number', action = 'store_true')
args = parse.parse_args()


if args.outfile.name == '<stdout>':
    if args.number == False:
        for fileobj in args.infile:
            print(fileobj.read(), end='')
    if args.number == True:
        num = 1
        for fileobj in args.infile:
            for line in fileobj:
                print(f'{num}   {line}', end='')
                num += 1
                

if args.outfile.name != '<stdout>':
    for fileobj in args.infile:
        args.outfile.write(fileobj.read())

