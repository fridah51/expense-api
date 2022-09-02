from datetime import datetime
from pydantic import BaseModel
from typing import Optional,List
import itertools


# id_iter = itertools.count()
#(next(id_iter))

class ExpenseBase(BaseModel): 
    id: int
    name: str
    amount: int
    category: str
    date: str
   
class ExpenseCreate(ExpenseBase):
   pass
   

class ExpensePut(BaseModel):
    name: Optional[str]
    amount:Optional [int]
    category:Optional[str] 
   
    
class Expenses(ExpenseBase):
    
    class Config:
        orm_mode = True
    
    
