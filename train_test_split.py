#-*- coding:utf_8 -*-
import random
import numpy as np
# 对样本列表AugList.txt(包含标签)进行随机划分，划分为训练集和测试集，比例为8:2

# 将文件列表乱序
#TrainNoLabels = 'train_No_labels.txt'
#TestNoLabels = 'test_No_labels.txt'

TrainLabels = 'train.txt'
TestLabels = 'test.txt'

trainfile = file(TrainLabels, 'a+')
testfile = file(TestLabels, 'a+')

with open('AugNonLabels.txt', 'rt') as handle:
    dataset = np.array([map(str, ln.split()) for ln in handle]).reshape(58060,)
    print 'dataset:\n', len(dataset)
    # dataset.shape:(58060,)
    # 打乱文件顺序
    random.shuffle(dataset)
    pos = int(len(dataset) * 0.8)
    train_list = dataset[:pos]
    test_list = dataset[pos:]


    for i in np.arange(pos):
        name = train_list[i]
        label = name.split('/')[1]
        #print 'name={}, label={}'.format(name, label)
        trainfile.write(name+' '+label+'\n')
    trainfile.close()
    
    for j in np.arange(len(test_list)):
        name = test_list[j]
        label = name.split('/')[1]
        testfile.write(name+' '+label+'\n')
    testfile.close()

