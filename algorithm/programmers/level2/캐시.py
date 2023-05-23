from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    for c in cities:
        c = c.lower()
        if c in cache:
            answer += 1
            cache.remove(c)
        else:
            answer += 5
        cache.append(c)
        if len(cache) > cacheSize:
            cache.popleft()
        
    return answer