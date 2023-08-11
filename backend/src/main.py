import os
import sys
import logging
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, File, UploadFile, BackgroundTasks
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.orm import Session
from src.utilities.transcript_utilities import Transcript, TranscriptParser
from src.database.database import engine, SessionLocal
from src.database import database_models, database_crud
from src.utilities.pdf_utilities import PdfUtilities

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

@app.post("/generate-unofficial-transcript")
async def generate_unofficial_transcript(background_tasks: BackgroundTasks, db: Session = Depends(get_db), file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return JSONResponse(content={"error": "File is not a PDF"}, status_code=400)

    pages = await PdfUtilities.extract_text_from_pdf(file)

    transcript = TranscriptParser(db, pages).parse()

    file_path = transcript.generate_transcript_pdf()

    response = FileResponse(file_path, headers={"Content-Disposition": f"attachment; filename={transcript.student_given_name}_{transcript.student_surname}_{transcript.student_number}_transcript.pdf"})
    background_tasks.add_task(PdfUtilities.delete_file, file_path)

    database_crud.increment_total_requests(db)
    
    return response
