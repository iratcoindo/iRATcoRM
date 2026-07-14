from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA = BASE_DIR / "Data"

def load_users():

    df = pd.read_excel(DATA / "users.xlsx")

    print(df.head())
    print(df.columns.tolist())

    return df

def load_projects():
    return pd.read_excel(DATA / "projects.xlsx")

def load_milestones():
    return pd.read_excel(DATA / "milestones.xlsx")

def load_budgets():
    return pd.read_excel(DATA / "budgets.xlsx")

def load_reports():
    return pd.read_excel(DATA / "reports.xlsx")
