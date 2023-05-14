import pandas as pd
import numpy as np
def load_data(dirname):
    return pd.read_csv(dirname,index_col=0)
def main():
    df = load_data("preproceesed_data")
    data_points =df.drop('0',axis=1).to_numpy()
    answers = df['0'].to_numpy()
    weights = np.random.rand(100)
    bias = np.random.rand()
    epoch=0
    
    while epoch<100:
        np.dot(weights,data_points.T)+bias
        #update somehow
        

        

if __name__ == "__main__":
    main()