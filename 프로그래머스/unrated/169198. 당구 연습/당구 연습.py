def solution(m, n, startX, startY, balls):
    answer = []
    for i, j in balls:
        if startX == i:
            if startY < j:
                y = 2*startY + j - startY
            else:
                y = 2*(n-startY) + startY - j
            answer.append(min(((startX+i)**2 + (startY-j)**2), ((m-startX+m-i)**2 + (startY-j)**2), y**2))
        elif startY == j:
            if startX < i:
                x = 2*startX + i - startX
            else:
                x = 2*(m-startX) + startX - i
            answer.append(min(((startX-i)**2 + (startY+j)**2), ((startX-i)**2 + (n-startY+n-j)**2), x**2))
        else:
            a = (startX-i)**2 + (startY+j)**2
            b = (startX+i)**2 + (startY-j)**2
            c = (m-startX+m-i)**2 + (startY-j)**2
            d = (startX-i)**2 + (n-startY+n-j)**2
            answer.append(min(a, b, c, d))
    return answer