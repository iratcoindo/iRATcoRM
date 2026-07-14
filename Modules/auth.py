import pandas as pd

DATABASE = "Data/iRATco_Database.xlsx"


def login(username, password):
    """
    Mengembalikan data user jika login berhasil.
    Mengembalikan None jika gagal.
    """

    users = pd.read_excel(
        DATABASE,
        sheet_name="users"
    )

    user = users[
        (users["username"] == username) &
        (users["password"] == password) &
        (users["active"] == "Yes")
    ]

    if len(user) == 1:
        return user.iloc[0]

    return None
