import matplotlib.pyplot as plt
L=[x*x for x in range (100)]
for i in range(100):
	plt.plot(i,L[i],'bo')

plt.show()