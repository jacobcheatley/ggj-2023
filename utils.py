import json
import re
from typing import Dict, List

import pandas as pd

with open("settings.json") as f:
    settings = json.load(f)

symbol_pattern = re.compile(r"\[(.)\]")
symbol_render = r'<img class="symbol" src="/symbols/symbol-\1.png" />'


def replace_symbols(s: str) -> str:
    return symbol_pattern.sub(symbol_render, s)


def get_card_data(use_print_count: bool = True, fixed_only: bool = False) -> List[Dict]:
    google_sheets_url = f'https://docs.google.com/spreadsheets/d/{settings["google_sheets_id"]}/gviz/tq?tqx=out:csv&sheet={settings["google_sheets_card_worksheet"]}'
    df = pd.read_csv(google_sheets_url)
    # Duplicate by print_count
    if use_print_count:
        df = df.loc[df.index.repeat(df.print_count)]
    df = df.drop(columns=["print_count"])

    # Filter to fixed if fixed_only
    if fixed_only:
        print(df["fixed"])
        df = df[df["fixed"] == True]

    # Symbol substitution
    df["cost"] = df["cost"].apply(lambda n: replace_symbols(n * "[W]"))
    df["mulch"] = df["mulch"].apply(lambda n: replace_symbols(n * "[N]"))
    df["effect"] = df["effect"].apply(replace_symbols)

    return df.to_dict(orient="records")


def get_goal_data():
    google_sheets_url = f'https://docs.google.com/spreadsheets/d/{settings["google_sheets_id"]}/gviz/tq?tqx=out:csv&sheet={settings["google_sheets_goal_worksheet"]}'
    df = pd.read_csv(google_sheets_url)

    df["condition"] = df["condition"].apply(replace_symbols)
    df["effect"] = df["effect"].apply(replace_symbols)

    return df.to_dict(orient="records")


if __name__ == "__main__":
    # print(get_card_data())
    print(replace_symbols("[W][N]"))
