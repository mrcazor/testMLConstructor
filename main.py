import pandas as pd

from model import linearModel


def score(data: pd.DataFrame) -> pd.DataFrame:
    dataValues = data.values
    return linearModel.predict(dataValues)


