from matplotlib import pyplot as plt

x = [5,6,7,8]
y = [7,3,8,3]

plt.plot(x,y)
plt.title('Memory Leak Growth')
plt.xlabel('x side')
plt.ylabel('y side')

plt.show()
