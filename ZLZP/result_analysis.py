# Author : Hellcat
# Time   : 2018/7/14
#把五险一金\带薪休假\员工旅游\周末双休\弹性工作\餐补\交通补助\年底双薪\股票期权看作公司福利，请对各种类型公司提供的福利多少分别进行降序排序，并打印输出
#对不同最低学历要求的月薪分布绘制直方图，对其均值绘制柱状图；对不同最低学历要求的招聘总人数绘制饼图
#以月薪为因变量，以其他特征为自变量（特征自选），建立特征对月薪的预测模型。要求至少选择两种机器学习算法，从中选择较优的算法并确定最优超参数（如果算法有超参数）

import csv
import pandas as pd
f_csv=pd.read_csv('zlzp_position.csv',header=0,index_col=0)
job_list=f_csv
print(job_list.index.name)
