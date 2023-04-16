def solution(word):
    alphabet = {0 : "", 1 : "A", 2 : "E", 3 : "I", 4 : "O", 5 : "U"}
    count = [0, 0, 0, 0, 0]
    dictionary = [""]
    while(count != [5, 5, 5, 5, 5]):
        if 0 in count:
            count[count.index(0)] += 1
        else:
            count[4] += 1
            for index in range(4, 0, -1):
                flag = plus_count(count, index)
                if flag == False: break
        tmp = alphabet[count[0]] + alphabet[count[1]] + alphabet[count[2]] + alphabet[count[3]] + alphabet[count[4]]
        dictionary.append(tmp)
    return dictionary.index(word)
    

def plus_count(count, index):
    if count[index] == 6:
        count[index - 1] += 1
        count[index] = 0
        return True
    return False