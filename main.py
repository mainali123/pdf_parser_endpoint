from fastapi import FastAPI, UploadFile, File
from pdf_processor import extract_text_from_pdf, count_pages

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Api is working!"}


@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_data = await file.read()
    text = extract_text_from_pdf(pdf_data)

    # If you want to count the number of pages in the PDF, you can use the following line
    # number_of_pages = count_pages(pdf_data)

    return {
        "text": text,
    }
