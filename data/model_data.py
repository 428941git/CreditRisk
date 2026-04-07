import pandas as pd
import numpy as np
from pathlib import Path


class modelData:
    def __init__(self, path: str = f"{Path(__file__).parent}/Credit_df.csv"):
        self.path = path

    def quantileMethod(self, df: pd.DataFrame) -> dict:
        quantileDict = {}
        for col in df.columns:
            quantileColumn = df[col].quantile(0.75)
            quantileDf = df[df[col] > quantileColumn]
            quantileDict.update({f"{col}": quantileDf})
        return quantileDict
    
    def getData(self) -> pd.DataFrame:
        df = pd.read_csv(self.path)
        needed_cols = ["Age", 
                       "Annual_Income", 
                       "Credit_Utilization_Ratio",
                       "Debt_To_Income_Ratio",
                       "Number_of_Late_Payments",
                       "Tenure_in_Years",
                       "Defaulted"]
        df = df[needed_cols]
        return df

    def loss_f(self, P, D):
         r_loss = -(D * np.log(P) + (1 - D) * np.log(1 - P))
         return r_loss
    
    def learningModel(self, 
                      df: pd.DataFrame,
                      b0: float = 0,
                      b1: float = 0,
                      b2: float = 0,
                      b3: float = 0,
                      b4: float = 0,
                      b5: float = 0,
                      b6: float = 0,
                      loss: float = 0):
        df.reset_index(drop=True, inplace=True)
        params = {
            "Age" : b1,
            "Annual_Income" : b2,
            "Credit_Utilization_Ratio" : b3,
            "Debt_To_Income_Ratio" : b4,
            "Number_of_Late_Payments" : b5,
            "Tenure_in_Years" : b6
        }

        cols = [
            "Age",
            "Annual_Income",
            "Credit_Utilization_Ratio",
            "Debt_To_Income_Ratio",
            "Number_of_Late_Payments",
            "Tenure_in_Years"
        ]
        for i, row in df.iterrows():
            Z = (
                params["Age"] * row["Age"] + 
                params["Annual_Income"] * row["Annual_Income"] + 
                params["Credit_Utilization_Ratio"] * row["Credit_Utilization_Ratio"] + 
                params["Debt_To_Income_Ratio"] * row["Debt_To_Income_Ratio"] + 
                params["Number_of_Late_Payments"] * row["Number_of_Late_Payments"] + 
                params["Tenure_in_Years"] * row["Tenure_in_Years"] + 
                b0  
                )
            p = 1 / (1 + np.exp(-Z))
            d = row["Defaulted"]
            df.loc[i, "PD"] = P
            df.loc[i, "Loss"] = r_loss
            loss = loss + r_loss
            
        return df, loss

if __name__ == "__main__":
    
    data = modelData()
    df = data.getData()
    df_train = df.sample(frac=0.75, random_state=42)
    df_validate = df.sample(frac=0.15, random_state=42)
    df, loss = data.learningModel(df_train)
    print(df)
    print(loss)
    
    

