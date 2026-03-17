def is_leap(y):return y%400==0 or y%4==0 and y%100!=0
w=6
y=2024
while 1:
 if is_leap(y+1):w=(w+2)%7
 else:w=(w+1)%7
 y+=1
 if w==6:print(y);break