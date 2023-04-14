from sqlalchemy.orm import Session
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
