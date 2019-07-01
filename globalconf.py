import os

path = os.path.abspath('..')


class TrainConfig(object):

    """
     训练参数
    """
    epoches = 10
    evaluateEvery = 100
    checkpointEvery = 100
    lr = 0.0001

class ModelConfig(object):

    embeddingSize = 200
    numFilters = 128
    filterSizes = [2,3,4,5]
    dropoutKeepProb = 0.5
    l2RegLambda = 0.0

class Config(object):
    sequenceLength = 200
    batchSize = 128
    dataSource = os.path.join(path,'data/labeledTrain.csv')
    stopWordSource = os.path.join(path,'data/english.txt')
    numClasses = 2
    rate = 0.8
    training = TrainConfig()
    model = ModelConfig
