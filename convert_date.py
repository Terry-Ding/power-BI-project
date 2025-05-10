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

def simplify_department() -> list[str]:
    file_handle = read_file(FILE_PATH)
    depart = file_handle["department"].tolist()
    simplified = []
    for i in depart:
        words = i.split(" ")
        result = ""
        for word in words:
            if word:
                result += word[0].upper()
        simplified.append(result)
    return simplified

def main():
    df = convert_date()
    df["department_abbr"] = simplify_department()
    df.to_excel("power-BI-project/new_top_20.xlsx")

if __name__ == "__main__":
    main()