import pandas as pd
    

if __name__ == "__main__":
    contents = pd.read_csv("data/CRDC2013_14content.csv")
    print(contents[300:370])