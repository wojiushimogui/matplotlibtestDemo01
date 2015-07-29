import matplotlib.pyplot as plt
#plt.xlabel(u'性别')  #中文不能显示，会乱码
plt.xlabel('sex')
plt.ylabel('num')
plt.xticks((0.2,1),('male','female'))#为每个bar进行说明，前面的位置，后面的相应位置的说明
##plt.xticks的用法和我们前面说到的left,height的用法差不多。\
##如果你有几个bar，那么就是几维的元组。第一个是文字的位置，第二个是具体的文字说明。
##不过这里有个问题，很显然我们指定的位置有些“偏移”，最理想的状态应该在每个矩形的中间。
##你可以更改(0,1)=>( (0.2+0.2)/2 ,(1+0.5)/2 )不过这样比较麻烦。
#我们可以通过直接指定bar方法里面的align="center"就可以让文字居中了。
plt.bar(left=(0.2,1),height=(2,1),width=(0.2,0.5),align='center')
plt.title('wojiushimogui')
plt.show()