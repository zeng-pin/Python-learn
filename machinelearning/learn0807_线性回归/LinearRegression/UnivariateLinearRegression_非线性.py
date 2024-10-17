import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from linear_regression import LinerRegression

data=pd.read_csv('G:\\python-learn\\machinelearning\\learn0807_线性回归\\data\\non-linear-regression-x-y.csv')

#得到训练数据，和测试数据

x=data['x'].values.reshape((data.shape[0],1))
y=data['y'].values.reshape((data.shape[0],1))

data.head(10)

plt.plot(x,y)
plt.show()

num_iterations = 50000
learning_rate = 0.01
polynomial_degree=15
sinusoid_degree=15
normalize_data=True

liner_Regression = LinerRegression(x, y, polynomial_degree, sinusoid_degree, normalize_data)#初始化
(theta,cost_history) = liner_Regression.train(learning_rate,num_iterations)#训练数据

print('开始损失:{:.2f}'.format(cost_history[0]))
print('结束损失:{:.2f}'.format(cost_history[-1]))

theta_table = pd.DataFrame({'Model Parameters': theta.flatten()})
plt.plot(range(num_iterations),cost_history)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Gradient Descent Preocess')
plt.show()


predictions_num=1000
x_predictions = np.linspace(x.min(),x.max(),predictions_num).reshape(predictions_num,1)
y_predictions = liner_Regression.predict(x_predictions)

plt.scatter(x,y,label='Train data')
#plt.scatter(x_predictions,y_predictions,label='Test data')
plt.plot(x_predictions,y_predictions,'r',label='Prediction')
plt.title('Happy')
plt.legend()
plt.show()
