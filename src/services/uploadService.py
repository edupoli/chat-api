import os
from fastapi import UploadFile
from uuid import uuid4
class UploadService:
    def __init__(self):
        self.upload_dir = "uploads"  # Diretório onde os arquivos serão salvos
        os.makedirs(self.upload_dir, exist_ok=True)  # Cria o diretório se não existir

    async def upload_file(self, file: UploadFile) -> str:
      file_ext = os.path.splitext(file.filename)[1]
      unique_filename = f"{uuid4()}{file_ext}"
      file_path = os.path.join(self.upload_dir, unique_filename)
      with open(file_path, "wb") as buffer:
          content = await file.read()
          buffer.write(content)
      return file_path