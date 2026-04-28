from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    roll_no: str
    course: str
    marks: int


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentOut(StudentBase):
    id: int

    class Config:
        orm_mode = True
