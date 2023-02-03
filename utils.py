import json
from typing import Dict, List

import pandas as pd

with open("settings.json") as f:
    settings = json.load(f)


def get_card_data(use_print_count=True) -> List[Dict]:
    google_sheets_url = f'https://docs.google.com/spreadsheets/d/{settings["google_sheets_id"]}/gviz/tq?tqx=out:csv&sheet={settings["google_sheets_card_worksheet"]}'
    df = pd.read_csv(google_sheets_url)
    # Duplicate by print_count
    if use_print_count:
        df = df.loc[df.index.repeat(df.print_count)]
    df = df.drop(columns=["print_count"])
    return df.to_dict(orient="records")


if __name__ == "__main__":
    print(get_card_data())
