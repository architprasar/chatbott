from fastapi import FastAPI, HTTPException
from typing import Optional
from functioncalling import generate_hermes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define the list of allowed origins
origins = [
    "*"
    # Add any other origins you want to allow
]

# Add the CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/generate")
def generate(k: Optional[str] = None):
    print(k)
    if k is None:
        raise HTTPException(status_code=400, detail="query parameter is required")
    try:
        response = generate_hermes(k)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
