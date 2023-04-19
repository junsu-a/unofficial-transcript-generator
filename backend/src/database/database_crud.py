from sqlalchemy.orm import Session
from src.utilities.api_utilities import fetch_course_title
from . import database_models

def get_total_used_counts(db: Session) -> float:
    instance = db.query(database_models.History) \
        .with_for_update(of=database_models.History) \
        .filter(database_models.History.name == "total_used_counts").first()

    if instance:
        db.commit()
        return float(instance.value)
    else:
        # Add a default row as 0 if there's no 
        instance = database_models.History(name="total_used_counts", value=0)
        db.add(instance)
        db.commit()
        return 0

def get_course_title(db: Session, subject: str, code: str) -> str:
    instance = db.query(database_models.Courses) \
        .with_for_update(of=database_models.Courses) \
        .filter(database_models.Courses.subject == subject and database_models.Courses.code == code).first()

    if instance:
        return str(instance.title)
    else:
        title = fetch_course_title(subject=subject, code=code)
        instance = database_models.Courses(subject=subject, code=code, title=title)
        db.add(instance)
        db.commit()
        return title

def increment_total_requests(db: Session):
    instance = db.query(database_models.History) \
        .with_for_update(of=database_models.History) \
        .filter(database_models.History.id == 1).first()

    if instance:
        instance.value += 1
    else:
        instance = database_models.History(name="total_used_counts", value=1)
        db.add(instance)

    db.commit()
