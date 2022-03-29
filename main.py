import matplotlib.pyplot as plt
import numpy as np

y = np.array([206, 196, 118, 92 , 83 , 39 , 1])
mylabels = ["SPD", "CDU/CSU", "Greens", "FDP", "AFD", "Left Party","Others"]
mycolors = ["#ff0000", "black", "#66ff66", "#ffff66","#66ccff" ,"#cc0052","#e6e6e6"]
plt.pie(y, labels = mylabels, startangle = 100,colors = mycolors)
plt.legend(title = "wybory do bundestagu 2021:")
plt.show()