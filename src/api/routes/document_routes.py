import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException

from pathlib import Path

import shutil

from src.config import UPLOAD_DIR

from src.services.document_service import process_document


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
def upload_document(file: UploadFile = File(...)):

    try:

        # Step 1: Validate file extension
        if Path(file.filename or "").suffix.lower() != ".pdf":
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed"
            )

        # Step 2: Create upload directory
        upload_path = Path(UPLOAD_DIR)

        upload_path.mkdir(
            parents=True,
            exist_ok=True
        )

        # Step 3: Generate a safe unique filename
        saved_filename = f"{uuid.uuid4()}.pdf"

        file_path = upload_path / saved_filename

        # Step 4: Save uploaded PDF
        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(file.file, buffer)

        # Step 5: Process PDF
        result = process_document(file_path)

        # Step 6: Return API response
        return {
            "message": "Document uploaded successfully",
            **result
        }

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

    finally:
        file.file.close()