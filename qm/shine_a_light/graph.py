import matplotlib.pyplot as plt
import numpy as np
# 定义 x 变量的范围 (-3，3) 数量 50 
x=np.linspace(-40,40,1000)
y=np.sin(x)/x
#z=(np.cos(x))**2

# Figure 并指定大小
plt.figure(num=3,figsize=(8,5))
# 绘制 y=x^2 的图像，设置 color 为 red，线宽度是 1，线的样式是 --
l1,=plt.plot(x,y,color='blue',linewidth=1.0,label = '2')
#l2,=plt.plot(x,z,color = 'red',linewidth = 1.0,label = '1')

# 设置 x，y 轴的范围以及 label 标注
plt.xlim(-40,40)
plt.ylim(-0.5,1.1)
plt.xlabel('x')
plt.ylabel('y')
plt.text(13.77,0.78,r'$y=\frac{\sin x}{x}$',fontsize = 20,color = 'blue')
#plt.legend(handles = [l1,l2,],labels = ['$P_2$','$P_1$'],loc = 'best')
# 显示图像
plt.show()
