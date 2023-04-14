import os
import sys
import logging
import pdfplumber
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.database.database import engine, SessionLocal
from src.database import database_models, database_crud

app = FastAPI()

# Logger
logging.basicConfig(encoding='utf-8',
                    level=logging.INFO, 
                    format='%(asctime)s %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler(sys.stdout)
                    ])
logging.info("Server started")

load_dotenv()

OFFICIAL_TRANSCRIPT_FEE = float(os.getenv("OFFICIAL_TRANSCRIPT_FEE"))

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

@app.get("/total-student-money-saved")
def get_total_student_money_saved(db: Session = Depends(get_db)):
    total_student_money_saved =  database_crud.get_total_used_counts(db) * OFFICIAL_TRANSCRIPT_FEE
    logging.info(f"Returning total student money saved. Value: {total_student_money_saved}")
    return total_student_money_saved

@app.post("/upload")
async def upload(db: Session = Depends(get_db), file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return JSONResponse(content={"error": "File is not a PDF"}, status_code=400)

    # Save the uploaded file temporarily
    temp_filename = "temp.pdf"
    with open(temp_filename, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text from the PDF using pdfplumber
    with pdfplumber.open(temp_filename) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    # Remove the temporary file
    os.remove(temp_filename)

    for p in pages:
        print(f"{p}\n")

    database_crud.increment_total_requests(db)

    return {"pages": pages}
