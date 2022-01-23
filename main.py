import pandas as pd

from model import linearModel


class Weights:
    '''Затычка для демонстрации'''
    pass


def train(data: pd.DataFrame) -> Weights:
    pass


def score(data: pd.DataFrame) -> pd.DataFrame:
    dataValues = data.values
    return linearModel.predict(dataValues)


