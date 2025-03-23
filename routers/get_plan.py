from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/getfile/{filename}")
async def get_file(filename: str):
    file_path = os.path.join("/home/plans", filename)  # Adjust the directory path

    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='application/octet-stream', headers={"Content-Disposition": f"attachment; filename={filename}"})
    else:
        return {"error": "File not found"}

