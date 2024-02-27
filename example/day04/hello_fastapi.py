from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class ListOption(str, Enum):
    user = "user"
    department = "department"
    account = "account"


@app.get("/{list_option}/list")
async def generic_list(list_option: ListOption):
    # Usando pattern matching
    match list_option:
        case ListOption.user:
            data = ["jim", "pam", "dwight"]
        case ListOption.department:
            data = ["Sales", "Management", "IT"]
        case ListOption.account:
            data = [1234, 8888, 9898]
    # if list_option == ListOption.user:
    #     data = ["jim", "pam", "dwight"]
    # if list_option == ListOption.department:
    #     data = ["Sales", "Management", "IT"]
    # elif list_option.value == "account":
    #     data = [1234, 8888, 9898]

    return {list_option: data}


@app.get("/user/{username}")  # Path / Roteamento
async def user_profile(username: str):
    return {"data": username}


@app.get("/account/{number}")
async def account_detail(number: int):
    return {"account": number}


# O fast API consegue lidar naturalmente com path basta usar o conversor
@app.get("/import/{filepath:path}")
async def import_file(filepath: str):
    return {"importing": filepath}


# @app.post()     # Create
# @app.get()      # Read
# @app.put()      # Update
# @app.delete()   # Delete