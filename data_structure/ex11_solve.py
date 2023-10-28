import sys
def print_uniq(filelist):
    all_lines = set()
    for f in filelist:
        all_lines |= set(f.readlines())
    print(''.join(all_lines))

if len(sys.argv) > 1:
    print_uniq(open(f) for f in sys.argv[1:])
else:
    print_uniq([sys.stdin])
