from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine


# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# DB Dependency
def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Create student
@app.post("/students", response_model=schemas.StudentOut)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

    return crud.create_student(db, student)


# Get all students
@app.get("/students", response_model=list[schemas.StudentOut])
def get_students(db: Session = Depends(get_db)):

    return crud.get_students(db)


# Get student by roll number
@app.get("/students/roll/{roll_no}", response_model=schemas.StudentOut)
def get_student(roll_no: str, db: Session = Depends(get_db)):

    student = crud.get_student_by_roll(db, roll_no)

    if not student:
        raise HTTPException(404, "Student not found")

    return student


# Update student by roll number
@app.put("/students/roll/{roll_no}", response_model=schemas.StudentOut)
def update_student(
    roll_no: str,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_student_by_roll(db, roll_no, student)

    if not updated:
        raise HTTPException(404, "Student not found")

    return updated


# Delete student by roll number
@app.delete("/students/roll/{roll_no}")
def delete_student(roll_no: str, db: Session = Depends(get_db)):

    deleted = crud.delete_student_by_roll(db, roll_no)

    if not deleted:
        raise HTTPException(404, "Student not found")

    return {"message": "Deleted successfully"}
