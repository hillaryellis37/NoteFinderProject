import matplotlib.image as img
import matplotlib.pyplot as plt

import pylab as plb


# plb.figure("how to get to work")
# plb.axes([.035, .035, .9, .9])
#
# l = "car", "truck", "boat", "dingie", "train", "plane", "bus", "rocket", 'tram', 'other'
# b = plb.round_(plb.random(10), decimals=2)
# c = ['blue', 'red', 'green', 'grey', "cyan", 'orange', 'yellowgreen', 'gold', 'lightcoral', 'lightskyblue']
# e = (0,0,0,0,0,0,0,0.05, 0,0) #explode the 8th slice only
#
# plb.cla()
# plb.pie(b, explode = e, labels=l, colors=c, radius=.75, autopct='%1.2f%%', shadow=True, startangle=15)
# plb.axis('equal')
# plb.xticks(()); plb.yticks(())
# plb.show()

#polar plot:

a = plb.axes([.065,.065,.88,.88], polar=True)

# q = 24
#t is position
# t = plb.arange(.015, 3*plb.pi, 3*plb.pi /q)
# t = plb.arange(0.0,3.6, .15)
t = plb.arange(0.0,3.6, .15)*3
t = plb.arange(0.0, 12.0, .1)
# t = plb.full((24), .1)

print("t = ", t)
print(len(t))
#rad is height. color is based on height
# rad = 12 * plb.rand(q)
# rad = plb.arange(1,13, .5)
rad = []

for i in plb.arange(-1,11):
    rad = plb.append(rad, [plb.full((10), i)])


print(len(rad))

print("rad = ", rad)

# w = plb.pi /4* plb.rand(q)
# print(w)
# print(len(w))
# w = plb.arange(0,.6,.025)
# print(w)
# print(len(w))

w = plb.full((120), 10)
print("w = ", w)
print(len(w))



ba = plb.bar(t, rad, width = w)

print("ba = ", ba)

for r, bar in zip(rad, ba):
    bar.set_facecolor(plb.cm.jet(r/12.))
    bar.set_alpha(0.75/50)

plb.show()