from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import explain_code, generate_code, debug_code

app = FastAPI()

class CodeRequest(BaseModel):
    language: str
    topic: str
    level: str

@app.post("/explain")
async def explain(data: CodeRequest):
    """
    Endpoint to explain a code snippet in the specified language and topic.
    """
    return {"responce": explain_code(data.language, data.topic, data.level)}

@app.post("/generate")
async def generate(data: CodeRequest):
    """
    Endpoint to generate a code snippet in the specified language and topic.
    """
    #return {"responce": generate_code(data.language, data.topic, data.level)}
    return {"response": generate_code(data.language, data.topic, data.level)}

@app.post("/debug")
async def debug(data: CodeRequest):
    """
    Endpoint to debug a code snippet in the specified language.
    """
    try:
        responce = debug_code(data.language, data.topic)
        if not responce:
            return {"error": "No code provided for debugging."}
        return {"responce": responce}
    except Exception as e:
        return {"error": f"Debugging failed: {str(e)}"}

    
