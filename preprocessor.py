import pandas as pd


def preprocess(df, region_df):
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df_encoded = pd.get_dummies(df['Medal'])
    df_encoded = df_encoded * 1
    df = pd.concat([df, df_encoded], axis=1)

    return df
