def minion_game(string):
    vow='AEIOU'
    str_len=len(string)
    kevin_score,stuart_score=0,0
    for i in range(str_len):
        if s[i] in vow:
            kevin_score+=(str_len-i)
        else:
            stuart_score+=(str_len-i)
    if kevin_score>stuart_score:
        print('Kevin',kevin_score)
    elif kevin_score<stuart_score:
        print('Stuart',stuart_score)
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
