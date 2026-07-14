from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA = BASE_DIR / "Data"

def load_users():
    return pd.read_excel(DATA / "users.xlsx")

def load_projects():
    return pd.read_excel(DATA / "projects.xlsx")

def load_milestones():
    return pd.read_excel(DATA / "milestones.xlsx")

def load_budgets():
    return pd.read_excel(DATA / "budgets.xlsx")

def load_reports():
    return pd.read_excel(DATA / "reports.xlsx")
