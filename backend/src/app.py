import os
import pdfplumber
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()


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

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
