import requests
import pandas as pd

def lambda_handler(event, context):
    print("Event Data -> ", event)
    response = requests.get("https://www.google.com/")
    print(response.text)

    d = {'col1' : [4,8],
         'col2' : [5,10]}
    df = pd.Dataframe(data=d)
    print(df)
    print('Demo completed !')