from datetime import date,timedelta

def js(j):
    dist1 = {0:13,1:1,2:2,3:3,4:5,5:4,6:4,7:2,8:2,9:2}
    shuju = str(j)
    conts = 0
    for sums in shuju:
        conts += dist1[int(sums)]
    return conts

s = date(2000,1,1)
e = date(2024,4,13)
data1 = []
day1 = 0
while s <= e:
    data1.append(int(s.strftime('%Y%m%d')))
    s += timedelta(days=1)
for i in data1:
    if js(i) > 50:
        day1 += 1
print(day1)