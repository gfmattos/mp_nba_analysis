import joblib
import pandas as pd

def manage_data(filename, df=pd.DataFrame(), action=['store','load']):

    path = f'D:\\DOCS\\my_workspace\\projects_git\\mp_nba_analysis\\data\\dataframes\\{filename}.pkl'

    if action == 'store':
        if df.empty:
            print('You must pass a Dataframe to be stored.')
        else:
            joblib.dump(df, path)

    elif action == 'load':
        df = joblib.load(path)
        return df