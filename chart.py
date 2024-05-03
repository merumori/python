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



#gropchart
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('stationary.xlsx')
print(df)

year = [2021, 2022, 2023]
x = df['Pencil']
x1 = df['Pen']
xaxis = np.arange(len(year))

plt.bar(xaxis - 0.2, x, 0.4, label='Pencil')  
plt.bar(xaxis + 0.2, x1, 0.4, label='Pen')    

plt.xticks(xaxis, year)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.legend()
plt.show()