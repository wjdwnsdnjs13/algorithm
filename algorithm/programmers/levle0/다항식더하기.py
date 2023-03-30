def solution(polynomial):
    polynomial = polynomial.split(" + ")
    x, none = 0, 0
    for i in range(len(polynomial)):
        if "x" in polynomial[i]:
            x += int(polynomial[i][:-1]) if polynomial[i][0] != "x" else 1
        else: none += int(polynomial[i])
    x = str(x) if x != 1 else ""
    none = str(none)
    answer = (x + "x + " + none) if (x != "0" and none != "0") else (x + "x") if x != "0" else none
    return answer