from fractions import Fraction

a, b = map(int, input().split())
c, d = map(int, input().split())
ans = Fraction(a*d+b*c, b*d)
print(ans.numerator, ans.denominator)