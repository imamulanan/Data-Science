import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[3,2,3,6,5]

plt.step(x,y,color="r",marker="o",ms=15,mfc="g",label="python")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Python")
plt.legend(loc=2)

plt.savefig("1st",dpi=2000,facecolor="g",transparent="true",bbox_inches="tight")
plt.show()
