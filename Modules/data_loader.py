import pandas as pd

USER_FILE = "data/users.xlsx"
PROJECT_FILE = "data/projects.xlsx"
MILESTONE_FILE = "data/milestones.xlsx"
PUBLICATION_FILE = "data/publications.xlsx"
BUDGET_FILE = "data/budget.xlsx"


def load_users():
    return pd.read_excel(USER_FILE)


def load_projects():
    return pd.read_excel(PROJECT_FILE)


def load_milestones():
    return pd.read_excel(MILESTONE_FILE)


def load_publications():
    return pd.read_excel(PUBLICATION_FILE)


def load_budget():
    return pd.read_excel(BUDGET_FILE)
