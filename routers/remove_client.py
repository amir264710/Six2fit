from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud
from database import get_db

router = APIRouter()

@router.delete("/clients/{client_id}")
def remove_client(client_id: int, db: Session = Depends(get_db)):
    # Ensure the client exists before deletion
    client = crud.get_client(db=db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return crud.delete_client(db=db, client_id=client_id)