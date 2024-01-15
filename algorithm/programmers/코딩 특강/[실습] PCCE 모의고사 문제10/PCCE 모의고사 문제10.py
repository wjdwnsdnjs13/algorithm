def solution(text, anagram, sw):
#     text : 암호화할 문자열
#     anagram : 애너그램 테이블
#     sw : 암호화할 지 복호화할 지 저장된 변수
    
    strList = ["" for i in range(len(text))]
    if(sw): #암호화
        for i in range(len(anagram)):
            strList[anagram[i]] = text[i]
            
    else: #복호화
        for i in range(len(anagram)):
            strList[i] = text[anagram[i]]
    return "".join(strList)