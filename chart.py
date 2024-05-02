# import matplotlib.pyplot as plt
# x=('bjp','congres')
# y=(200,400)
# plt.bar(x,y,label='voting')
# plt.xlabel("party")
# plt.ylabel('voting')
# plt.title("voting the toe party")
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# x=('bjp','congres','aap','svernaval','hansaben','bet')
# y=(2000,400,20,10,4,1)
# plt.plot(x,y,label='voting')
# plt.xlabel("party")
# plt.ylabel('voting')
# plt.title("voting the toe party")
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# x=('bjp','congres','aap','svernaval','hansaben','bet')
# y=(2000,400,20,10,4,1)
# plt.pie(y,labels=x)
# plt.title("voting the toe party")
# plt.legend()
# plt.show()


import matplotlib.pyplot as plt
x=('bjp','congres')
y=(200,400)
d=(20,20)
plt.bar(x,y,label='voting')
plt.bar(x,d,label='voting')
plt.xlabel("party")
plt.ylabel('voting')
plt.title("voting the toe party")
plt.legend()
plt.show()