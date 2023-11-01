from tempfile import SpooledTemporaryFile
import pandas as pd
import numpy as np
from models.client import Client

class ParseService:
    
    def clean_csv(self, file: SpooledTemporaryFile) -> list[Client]:
        df = pd.read_csv(file)
        cleaned = (
            df.pipe(self.drop_columns)
            .pipe(self.merge_emails)
            .pipe(self.extract_website)
            .replace({np.nan: None})
        )
        return [
            Client(**cl) for cl in cleaned.to_dict('records')
        ]
    
    def drop_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        df.drop(df.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 18, 19, 20, 21, 22, 23, 24, 28]], axis=1, inplace=True)
        df.drop(df.columns[6:13], axis=1, inplace=True)
        df.drop(df.columns[7:], axis=1, inplace=True)
        df.rename(columns={'location_name': 'location'}, inplace=True)
        return df

    def merge_emails(self, df: pd.DataFrame) -> pd.DataFrame:
        df['email'] = df.apply(
            lambda row: row['third_party_email_1'] if pd.isnull(row['email']) or row['email'] == '' else row['email'],
            axis=1)
        df.drop('third_party_email_1', axis=1, inplace=True)
        return df
    
    def extract_website(self, df: pd.DataFrame) -> pd.DataFrame:
        df['website'] = df['email'].str.replace(".*@", "", regex=True)
        return df