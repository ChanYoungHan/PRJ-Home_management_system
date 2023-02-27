from fastapi import FastAPI
from typing import Union
import requests

from app.database.db_sqlalchemy import DB_SQLAlchemy, UserInfo, CreditCradInfo


app = FastAPI()
db = DB_SQLAlchemy()


@app.get("/")
def read_root():
    return {"Hello": "host1 server"}

@app.get("/clinets/get_connection_check")
def read_client_info():
    x = requests.get('http://10.28.157.3')
    return x.json()



@app.get("/get_user_credit_info/{name}")
def read_item(name: str, q: Union[str, None] = None):
    res_user_info: UserInfo = db.get_user_info(name=name)
    res_credit_card_info: CreditCradInfo = db.get_credit_card_info(name=name)

    return {
        "user_name": name,
        "user_id": res_user_info.id,
        "credit_card_id": res_credit_card_info.id,
        "credit_card_bank_name": res_credit_card_info.bank_name,
    }

@app.get("/user_info/{name}")
def read_item(name: str, q: Union[str, None] = None):
    res_user_info: UserInfo = db.get_user_info(name=name)
    return {
        "user_name": name,
        "user_id": res_user_info.id,
        "credit_card_id": res_user_info.credit_card_id
    }