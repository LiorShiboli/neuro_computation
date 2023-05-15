import pandas as pd
import numpy as np
def load_data(dirname):
    return pd.read_csv(dirname,index_col=0)
def adaline_training(answers,data_points,alpha,epochs):
    data_size = len(data_points)
    weights = np.random.rand(100)
    bias = np.random.rand()
    for iteration in range(epochs):
        predictions =np.dot(weights,data_points.T)+bias
        error = predictions - answers
        weights = weights -(1/data_size)*2*alpha*np.dot(error,data_points)
        bias = bias - (1/data_size)*2*alpha*error.sum()


    return (weights,bias)
def main():
    datafile = input("datafile:")
    df = load_data(datafile)
    while input("do you want to predict[Y/N]")=="Y":
        to_predict1= int(input("which number do you want to be 1 in the predicition "))
        to_predict0= int(input("which number do you want to be 0 in the predicition "))
        learning_rate = float(input("learning rate(suggested 0.01): "))
        epochs = int(input("epochs(suggested 10000): "))
        df_relevant = df[df['0'].isin( [to_predict0,to_predict1])]
        df_relevant = df_relevant.sample(frac=1).reset_index(drop=True)
        data_points =  df_relevant.drop('0',axis=1).to_numpy()
        answers = df_relevant['0'].to_numpy()
        answers = (answers==to_predict1).astype(float)
        index = np.arange(len(answers))

        test_accuracies =[]
        train_accuracies =[]
        for i in range(5):
            weights,bias = adaline_training(answers[index%5 !=i],data_points[index%5 !=i],learning_rate,epochs)
            training_predictions = np.rint(np.dot(weights,data_points[index%5 !=i].T)+bias)
            test_predictions = np.rint(np.dot(weights,data_points[index%5 ==i].T)+bias)
            training_accuracy = (training_predictions == answers[index%5 !=i]).sum()/len(answers[index%5!=i])
            test_accuracy = (test_predictions == answers[index%5 ==i]).sum()/len(answers[index%5==i])
            test_accuracies+= [test_accuracy]
            train_accuracies += [training_accuracy]
            print("train accuracy = "+str(training_accuracy))
            print("test accuracy = "+str(test_accuracy))
        
        print("average(mean) train: "+str(np.mean(train_accuracies)))
        print("standard deviation training:"+ str(np.std(train_accuracies)))
        print("average(mean) test: "+str(np.mean(test_accuracies)))
        print("standard deviation test:"+ str(np.std(test_accuracies)))
        

if __name__ == "__main__":
    main()