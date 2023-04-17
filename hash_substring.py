# python3

def read_input():
   
    ch= input()

    if 'I'in(ch):
        #keybord
        return (input().rstrip(), input().rstrip())
    else:
        with open('tests/06',"r") as fails:

            return (fails.readline().rstrip(), fails.readline().rstrip())

    

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    num= 101
    math= lambda s:sum(ord(c) for c in s)
    list=[]

    phash= math(pattern) % num
    for i in range(len(text)- len(pattern)+1):
        sub= text[i:i+len(pattern)]
        sub_hash= math(sub) % num
        if sub_hash == phash:
            if sub == pattern:
                list.append(i)
    return(list)
   
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
