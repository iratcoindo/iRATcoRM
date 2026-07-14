from Modules.data_loader import load_users

def login(username, password):

    users = load_users()

    user = users[
        (users["username"] == username) &
        (users["password"] == password) &
        (users["active"] == "Yes")
    ]

    if len(user) == 1:
        return user.iloc[0]

    return None
