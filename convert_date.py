import pandas as pd

FILE_PATH = "power-BI-project/top_20_downloaded_open_info.csv"

def read_file(filename: str):
    df = pd.read_csv(filename)
    new_df = df.dropna().drop_duplicates()
    return new_df

def convert_date():
    file_handle = read_file(FILE_PATH)
    month_str = file_handle["month_mois"].astype(str)
    year_str = file_handle["year_annee"].astype(str)
    file_handle["month_year"] = month_str + "/" + year_str
    return file_handle

def main():
    df = convert_date()
    df.to_excel("power-BI-project/new_top_20.xlsx")

if __name__ == "__main__":
    main()