from typing import Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend to access server
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

data_store = {
    "grade_school": {
        "math": {},
        "science": {},
        "english": {}
    },
    "middle_school": {
        "math": {},
        "science": {},
        "english": {}
    },
    "high_school": {
        "math": {},
        "science": {},
        "english": {}
    }
}


class QAPair(BaseModel):
    question: str
    answer: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

# get q/a item
@app.get("/{category}/{subject}/{item_id}")
def read_item(category: str, subject: str, item_id: int):
    if category in data_store and subject in data_store[category] and item_id in data_store[category][subject]:
        return data_store[category][subject][item_id]
    raise HTTPException(status_code=404, detail="Item not found")

# add a new q/a pair
@app.post("/{category}/{subject}/")
def create_item(category: str, subject: str, item: QAPair):
    if category not in data_store or subject not in data_store[category]:
        raise HTTPException(status_code=400, detail="Invalid category or subject")

    item_id = len(data_store[category][subject])
    data_store[category][subject][item_id] = item.dict()
    return data_store[category][subject][item_id]

# get all q/a pairs from category subject in datastore
@app.get("/{category}/{subject}/")
def read_all_items(category: str, subject: str) -> Dict[int, QAPair]:
    if category in data_store and subject in data_store[category]:
        return data_store[category][subject]
    raise HTTPException(status_code=404, detail="Category or subject not found")