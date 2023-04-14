import os
import pdfplumber
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from src.database.database import engine, SessionLocal
from src.database import database_models, database_crud

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        return JSONResponse(content={'error': 'File is not a PDF'}, status_code=400)

    # Save the uploaded file temporarily
    temp_filename = 'temp.pdf'
    with open(temp_filename, 'wb') as buffer:
        buffer.write(await file.read())

    # Extract text from the PDF using pdfplumber
    with pdfplumber.open(temp_filename) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    # Remove the temporary file
    os.remove(temp_filename)

    for p in pages:
        print(f"{p}\n")

    return {'pages': pages}
