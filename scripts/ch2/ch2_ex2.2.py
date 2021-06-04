# Ex 2.2
# 1
# The volume of a sphere with radius r is 4 πr3. What is the volume of a sphere with radius 5?
print("Q1")
pi=3.1415926535897932
r = 5
vol = (4/3)*pi*r**3
print(vol)

# 2
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
print("Q2")
price=24.95;
pricewithdisc=price*0.6
pricewithdisc_all = pricewithdisc*60
shipping=0.75*59+3
cost=pricewithdisc_all+shipping
print(cost)

# 3
# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
print("Q3")
firstpart_sec = 8*60 + 15;
secocdpart_sec = (7*60 + 15)*3;
lastpart_sec = firstpart_sec;
minutes = (firstpart_sec + secocdpart_sec + lastpart_sec)/60
print("Minutes running:",minutes)

leaveTime = (6*60+52)
print(leaveTime)
arriveTimeHours = (leaveTime+minutes)//60
print("arriveTimeHours=", arriveTimeHours)
arriveTimeMinutes = (leaveTime+minutes) - arriveTimeHours * 60
print("arriveTime=", arriveTimeHours, arriveTimeMinutes)
print ('Finish time was %d:%d' % (arriveTimeHours, arriveTimeMinutes))
