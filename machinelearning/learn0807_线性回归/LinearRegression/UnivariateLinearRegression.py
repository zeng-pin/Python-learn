import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from linear_regression import LinerRegression

data=pd.read_csv('G:\\python-learn\\machinelearning\\learn0807_线性回归\\data\\world-happiness-report-2017.csv')

#得到训练数据，和测试数据
train_data = data.sample(frac=0.8)
test_data = data.drop(train_data.index)#得到测试数据

input_param_name='Economy..GDP.per.Capita.'
output_param_name='Happiness.Score'

x_train=train_data[[input_param_name]].values
y_train=train_data[[output_param_name]].values

x_test=test_data[[input_param_name]].values
y_test=test_data[[output_param_name]].values

plt.scatter(x_train,y_train,label='Train data')
plt.scatter(x_test,y_test,label='Test data')
plt.xlabel(input_param_name)
plt.ylabel(output_param_name)
plt.title('Happy')
plt.legend()
plt.show()


num_iterations = 500
learning_rate = 0.01

liner_Regression=LinerRegression(x_train,y_train)#初始化
(theta,cost_history)=liner_Regression.train(learning_rate,num_iterations)#训练数据

print('开始的损失：',cost_history[0])
print('训练后损失：',cost_history[-1])

#随着训练的进行损失分布图
plt.plot(range(num_iterations),cost_history)
plt.xlabel('迭代次数')
plt.ylabel('损失')
plt.title('Happy')
plt.show()

predictions_num=100
x_predictions = np.linspace(x_train.min(),x_train.max(),predictions_num).reshape(predictions_num,1)
y_predictions = liner_Regression.predict(x_predictions)

plt.scatter(x_train,y_train,label='Train data')
plt.scatter(x_test,y_test,label='Test data')
plt.plot(x_predictions,y_predictions,'r',label='Prediction')
plt.xlabel(input_param_name)
plt.ylabel(output_param_name)
plt.title('Happy')
plt.legend()
plt.show()
