from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Todo
from schemas import TodoSchema

# Create the actual database file
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/todos")
def list_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

@app.post("/todos")
def create_todo(item: TodoSchema, db: Session = Depends(get_db)):
    new_todo = Todo(title=item.title, is_done=item.is_done)
    db.add(new_todo)
    db.commit()
    return new_todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, item: TodoSchema, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    
    todo.title = item.title
    todo.is_done = item.is_done
    db.commit()
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    
    db.delete(todo)
    db.commit()
    return {"message": "Deleted successfully"}