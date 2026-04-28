from sqlalchemy.orm import Session
import models, schemas


# Create student
def create_student(db: Session, student: schemas.StudentCreate):

    db_student = models.Student(
        name=student.name,
        roll_no=student.roll_no,
        course=student.course,
        marks=student.marks
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


# Get all students
def get_students(db: Session):
    return db.query(models.Student).all()


# Get student by roll number
def get_student_by_roll(db: Session, roll_no: str):

    return db.query(models.Student)\
             .filter(models.Student.roll_no == roll_no)\
             .first()


# Update student by roll number
def update_student_by_roll(
    db: Session,
    roll_no: str,
    student: schemas.StudentUpdate
):

    db_student = get_student_by_roll(db, roll_no)

    if not db_student:
        return None

    db_student.name = student.name
    db_student.course = student.course
    db_student.marks = student.marks

    db.commit()
    db.refresh(db_student)

    return db_student


# Delete student by roll number
def delete_student_by_roll(db: Session, roll_no: str):

    student = get_student_by_roll(db, roll_no)

    if not student:
        return None

    db.delete(student)
    db.commit()

    return student
