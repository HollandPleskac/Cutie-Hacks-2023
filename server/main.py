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

class QAPair(BaseModel):
    question: str
    answer: str
data_store = {
    "grade_school": {
        "math": {
            0: {"question": "What is 7 + 5?", "answer": "12"},
            1: {"question": "How many sides does a triangle have?", "answer": "3"},
            2: {"question": "If you have 2 apples and get 3 more, how many apples do you have?", "answer": "5"}
        },
        "science": {
            0: {"question": "What causes day and night?", "answer": "The rotation of the Earth."},
            1: {"question": "What do plants need to grow?", "answer": "Water, sunlight, and soil"},
            2: {"question": "What is the boiling point of water?", "answer": "100 degrees Celsius"}
        },
        "english": {
            0: {"question": "What is the plural form of 'fox'?", "answer": "Foxes"},
            1: {"question": "What are the vowels in the English alphabet?", "answer": "A, E, I, O, U"},
            2: {"question": "What is the past tense of 'run'?", "answer": "Ran"}
        }
    },
    "middle_school": {
        "math": {
            0: {"question": "Solve for x: 3x + 5 = 14.", "answer": "3"},
            1: {"question": "What is the area of a rectangle with length 4cm and width 3cm?", "answer": "12 square cm"},
            2: {"question": "What is the square root of 64?", "answer": "8"}
        },
        "science": {
            0: {"question": "What is photosynthesis?", "answer": "The process by which green plants use sunlight to make food from carbon dioxide and water."},
            1: {"question": "What is the chemical formula for water?", "answer": "H2O"},
            2: {"question": "What are the three states of matter?", "answer": "Solid, liquid, gas"}
        },
        "english": {
            0: {"question": "Identify the adverb in this sentence: 'She ran quickly.'", "answer": "Quickly"},
            1: {"question": "What is a synonym for 'happy'?", "answer": "Joyful"},
            2: {"question": "What is the main idea of a story called?", "answer": "Theme"}
        }
    },
    "high_school": {
        "math": {
            0: {"question": "Find the derivative of the function f(x) = 2x².", "answer": "4x"},
            1: {"question": "Solve the equation: 2x - 6 = 8.", "answer": "7"},
            2: {"question": "What is the value of Pi (π) to two decimal places?", "answer": "3.14"}
        },
        "science": {
            0: {"question": "What is the law of conservation of mass?", "answer": "Matter is not created or destroyed in a chemical reaction."},
            1: {"question": "What is the primary source of energy for Earth?", "answer": "The Sun"},
            2: {"question": "What is the DNA double helix?", "answer": "The structure of DNA"}
        },
        "english": {
            0: {"question": "Analyze the theme of 'freedom' in Mark Twain's 'Adventures of Huckleberry Finn.'", "answer": "The theme of freedom in the novel explores the conflict between civilization and individuality."},
            1: {"question": "What is an example of a metaphor?", "answer": "Time is a thief"},
            2: {"question": "Identify the protagonist in Shakespeare's 'Romeo and Juliet'.", "answer": "Romeo"}
        }
    }
}


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