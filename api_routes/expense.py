from fastapi import APIRouter,Depends, HTTPException
from typing import List,Dict,Generator
import json
from schema import ExpenseCreate,ExpensePut,Expenses

expense_router = APIRouter()


@expense_router.get("", 
summary="get a list of all todo items",
status_code=200,
response_model=List[Expenses]
)
def expenses():
   
    with open('db.json', 'r') as f:
       payload = json.load(f)
       
    return payload


@expense_router.get("/{expID}", 
response_model=Expenses,
summary="get a todo item",
status_code=200
)
def expense(expID:int):
    
    with open('db.json', 'r') as f:
       payload = json.load(f)
   
    return payload[expID]


@expense_router.post("", 
response_model=Expenses,
summary="add a todo item",
status_code=201
)
def  post_expense( payload:ExpenseCreate):
    pay = dict(payload)
    
    with open('db.json', 'r') as f:
       data = json.load(f)
    
    data.append(pay)
    
    with open('db.json', 'w') as f:
        json.dump(data, f)

    return payload


@expense_router.put("/{expID}", 
response_model=ExpensePut,
summary="update a todo item",
status_code=200
)
def  update_expense(expID:int, payload:ExpensePut):
    
    with open('db.json', 'r') as f:
       data = json.load(f)
   
   #update some 
    pay = data[expID] 
    payloadz = dict(payload)
    pay["name"] = payloadz["name"]
    pay["category"] =payloadz["category"]
    pay["amount"] = payloadz["amount"]
    
    #update the file
    with open('db.json', 'w') as f:
        json.dump(data, f)

    return payload


@expense_router.delete("/{expID}", 
status_code=200,
summary="delete item",
response_model=Dict[str,str]
)
def  delete_expense(expID:int):
    with open('db.json', 'r') as f:
       payload = json.load(f)
   
   #delete some 
    payload.remove(payload[expID])
    
    #update the file
    with open('db.json', 'w') as f:
        json.dump(payload, f)

    
    return {"message":"TodoID deleted"}