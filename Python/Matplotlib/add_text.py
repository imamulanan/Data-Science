import matplotlib.pyplot as

x=[1,2,3,4,5]
y=[3,1,5,2,6]

plt.plot(x,y)
plt.title("CIT-220",fontsize=15)
plt.xlabel("Days",fontsize=15)
plt.ylabel("Python",fontsize=15)

plt.text(2,5,"Java",fontsize=15,style="italic",bbox={"facecolor":"red"})


plt.annotate("python",xy=(1,3),xytext=(4,4),arrowprops=dict(facecolor="black",shrink=100))
plt.show()
