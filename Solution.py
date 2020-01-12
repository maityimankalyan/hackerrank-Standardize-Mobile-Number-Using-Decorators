# This is based on python 3
# For python 2: Should work if you change line#19 input() -> rae_input() and print() -> print ""

def wrapper(f):
    def fun(l):
        all_numbs = []
        import re
        for i in l:
            r = re.search(r'^([\+910]*)(\d{5})(\d{5})$', str(i))
            if r: all_numbs.append('{} {} {}'.format('+91', r.group(2), r.group(3)))
        print('\n'.join(sorted(all_numbs)))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
