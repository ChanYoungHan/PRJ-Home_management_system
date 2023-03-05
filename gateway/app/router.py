from fastapi import FastAPI
from typing import Union
import requests


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "control server"}


@app.get("/clinets/get_connection_check")
def read_client_info():
    x = requests.get("http://10.28.157.3")
    return x.json()


@app.get("/get_user_credit_info/{name}")
def read_item(name: str, q: Union[str, None] = None):

    user_info = requests.get(f"http://10.0.0.142/user_info/{name}").json()
    credit_card_info = requests.get(
        f'http://10.0.0.142:81/credit_info/{user_info["credit_card_id"]}'
    ).json()

    return {
        "user_name": name,
        "user_id": user_info["user_id"],
        "credit_card_id": user_info["credit_card_id"],
        "credit_card_bank_name": credit_card_info["credit_card_bank_name"],
    }
