import numpy as np
from scipy.optimize import minimize
from utils.features import prepare_for_training
from utils.hypothesis import sigmoid

class LogisticRegression:
    def __init__(self, data, labels, polynomial_degree=0, sinusoid_degree=0, normalize_data=False):
        """
            1.对数据进行预处理操作
            2.先得到所有的特征个数
            3.初始化参数矩阵
        """
        (data_processed,
         features_mean,
         features_deviation) = prepare_for_training(data, polynomial_degree, sinusoid_degree, normalize_data=False)

        self.data = data_processed
        self.labels = labels
        self.unique_labels = np.unique(labels)
        self.features_mean = features_mean
        self.features_deviation = features_deviation
        self.polynomial_degree = polynomial_degree
        self.sinusoid_degree = sinusoid_degree
        self.normalize_data = normalize_data

        num_features = self.data.shape[1]
        num_unique_labels = np.unique(labels).shape[0]
        self.theta = np.zeros((num_unique_labels, num_features)) # theta初始化，多一个维度，多分类内容

    def train(self,max_iterations = 1000):
        cost_histories = []
        num_features = self.data.shape[1]
        for label_index,unique_label in enumerate(self.unique_labels):
            current_initial_theta = np.copy(self.theta[label_index].reshape(num_features,1))
            current_lables = (self.labels == unique_label).astype(float)
            (current_theta,cost_history) = LogisticRegression.gradient_descent(self.data,current_lables,current_initial_theta,max_iterations)

    @staticmethod
    def gradient_descent(self):

        
        
        
        
        
        
        
        
        


