def solution(s, n):
    answer = ''
    dict_alpha = {0:'z', 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h',
           9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 
           18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'
           }
    dict_alpha_reverse = {v:k for k,v in dict_alpha.items()}
    for x in s:
        if x == ' ':
            answer += ' '
        elif x.isupper():
            answer += dict_alpha.get((dict_alpha_reverse.get(x.lower())+n)%26).upper()
        else:
            answer += dict_alpha.get((dict_alpha_reverse.get(x.lower())+n)%26)
    return answer