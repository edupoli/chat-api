from fastapi import APIRouter, HTTPException, UploadFile, File
from src.services.uploadService import UploadService

router = APIRouter(prefix="/api/v1", tags=["upload"])
service = UploadService()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = await service.upload_file(file)
        return {"filename": file.filename, "path": file_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao fazer upload do arquivo: {str(e)}")