import pandas as pd



def load_data():
    return pd.read_csv("data/bikes_completed.csv")

if __name__ == "__main__":
    create_main_layout()
