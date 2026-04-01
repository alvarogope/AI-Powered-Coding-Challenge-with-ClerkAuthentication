from src.database.models import SessionLocal
from src.database import models

db = SessionLocal()
quota = db.query(models.ChallengeQuota).first()
quota.quota_remaining = 15
db.commit()
print("Quota reset to 15")
db.close()
