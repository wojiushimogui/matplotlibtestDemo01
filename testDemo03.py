import matplotlib.pyplot as plt
#left、height、width可以设置多个值，但是，这三个的长度如果要设置的话，必须长度要一致
plt.bar(left=(0.2,1),height=(2,1),width=(0.2,0.5))
#plt.bar(left=(0.2,1,2),height=(2,1),width=(0.2,0.5))报错，长度不一致
plt.show()