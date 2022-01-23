import pandas as pd

from main import score

if __name__=='__main__':
    df = pd.read_csv('./Data/data.csv', index_col=0)
    print(score(df))