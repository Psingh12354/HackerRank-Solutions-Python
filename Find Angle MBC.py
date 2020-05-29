import math
AB=int(input())
BC=int(input())
AC=math.sqrt(AB**2+BC**2)
AC=AC/2.0
ADJ=BC/2.0
print(str(int(round(math.degrees(math.acos(ADJ/AC)))))+"°")
