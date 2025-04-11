from sqlalchemy.orm import Session
import models, schemas

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.client_id == client_id).first()

def delete_client(db: Session, client_id: int):
    client = get_client(db, client_id)
    if client:
        db.delete(client)
        db.commit()
    return client

def create_diet_plan(db: Session, plan: schemas.PlanCreate):
    db_plan = models.Plan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def update_body_fat(db: Session, client_id: int, body_fat_percentage: float):
    client = get_client(db, client_id)
    if client:
        client.body_fat_percentage = body_fat_percentage
        db.commit()
        db.refresh(client)
    return client
