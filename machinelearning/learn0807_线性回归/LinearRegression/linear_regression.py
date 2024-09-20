import numpy as np
from machinelearning.learn0807_线性回归.utils.features import prepare_for_training
class LinerRegression:

    def __init__(self, data, lables, polynomial_degree=0, sinusoid_degree=0, normalize_data=True):
        '''
        1.对数据进行预处理
        2.得到所有的特征个数
        3.初始化参数矩阵
        '''
        (data_processed,
         features_mean,
         features_deviation)=prepare_for_training(data,polynomial_degree=0,sinusoid_degree=0,normalize_data=True)

        self.data=data_processed
        self.lables=lables
        self.features_mean=features_mean
        self.features_deviation=features_deviation


        self.polynomial_degree=polynomial_degree
        self.sinusoid_degree=sinusoid_degree
        self.normalize_data=normalize_data

        num_features=self.data.shape[1]#矩阵列数，即模型特征数
        self.theta=np.zeros((num_features,1))#初始矩阵创立

    def train(self,alpha,num_iterations=500):#alpha为线性回归中的a为学习率，num_iterations为迭代次数
        #训练模块执行梯度下降，进行调用
        cost_history= self.gradient_descent(alpha,num_iterations)
        return self.theta,cost_history


    def gradient_descent(self,alpha,num_iterations):#单独执行梯度下降
        '''
        迭代模块，会迭代num_iterations次
        '''
        cost_history = []#损失变化记录

        for _ in range(num_iterations):#迭代损失值参数，并进行参数更新
            self.gradient_step(alpha)
            cost_history.append(self.cost_function(self.data,self.lables))
        return cost_history

    def gradient_step(self,alpha):
        '''
        梯度下降参数更新计算方法，为矩阵计算使用numpy.dot
        '''
        num_examples=self.data.shape[0]#确认矩阵行数即样本总个数
        prediction = LinerRegression.hypothesis(self.data,self.theta)
        delta=prediction - self.lables
        theta=self.theta
        theta=theta-alpha*(1/num_examples)*(np.dot(delta.T,self.data)).T
        self.theta=theta
        pass
    def cost_function(self,data,lables):
        '''
        损失值计算
        '''
        num_examples = data.shape[0]#行数，即样本个数
        prediction = LinerRegression.hypothesis(self.data, self.theta)
        delta = prediction - self.lables
        cost = (1/2)*np.dot(delta.T,delta)/num_examples####损失值函数关键，此处使用常见的最小二乘法进行特征缩放
        return cost[0][0]

    @staticmethod
    def hypothesis(data,theta):
        '''
        预测值估计
        '''
        predictions = np.dot(data,theta)#h(xθ)的计算
        return predictions


        #以下为测试集函数
    def get_cost(self,data,lables):
        '''
        得到了哪些损失
        '''
        data_processed=prepare_for_training(data,self.polynomial_degree,self.sinusoid_degree,self.normalize_data)[0]
        self.cost_function(data_processed,lables)#计算方法和损失值获得
        return  self.cost_function(data_processed,lables)

    def predict(self,data):
        '''
        用训练好的参数模型预测得到回归值结果
        '''
        data_processed = prepare_for_training(data, self.polynomial_degree, self.sinusoid_degree, self.normalize_data)[0]
        predictions = LinerRegression.hypothesis(data_processed,self.theta)

        return predictions

















