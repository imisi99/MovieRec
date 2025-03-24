import pandas as pd
import numpy as np
def preprocessing(filepath: str) -> [pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(filepath)
    print("Data before preprocessing")
    print(df.head())
    metadata = df
    df = df.drop(columns=["Title", "Duration", "Release Year"])

    for column in df.columns:
        df[column] = df[column].fillna(df[column].iloc[0])

    df["Type"] = df["Type"].apply(lambda x: 1 if x == "Movie" else 0)
    # One hot encoding
    df = pd.get_dummies(df, columns=["Genre", "Rating", "Country"])

    df = df.astype(int)

    print("Data after preprocessing")
    print(df.head())
    return df, metadata

def create_synthetic_ratings(movie: pd.DataFrame) -> pd.DataFrame:
    np.random.seed(42)
    num = movie.shape[0]
    target = np.random.uniform(0.5, 1, num) * 5
    target = pd.DataFrame(target, columns=["rating"])
    return target

def create_synthetic_users(movie: pd.DataFrame) -> pd.DataFrame:
    np.random.seed(42)
    num, row = movie.shape
    user = np.random.random_integers(0, 1, (num, row))
    user = pd.DataFrame(user, columns=movie.columns)
    return user