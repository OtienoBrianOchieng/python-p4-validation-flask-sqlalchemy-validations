from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class EmailAddress(db.Model):
    __tablename__ = 'emailaddress'
    
    id = Column(Integer, primary_key = True)
    email = Column(String)
    backup_email = Column(String)

    @validates('email', 'backuo_email')
    def validate_email(self, key, adress):
        if '@' not in adress:
            raise ValueError ("failed simple email validation")
        return adress
email = EmailAddress(email = 'banana')
Session = session.add(email)
session = Session()

base.metadata.create_all(db)

email = EmailAddress(email='banana')
session.add(email)

try:
    session.commit()
except sqlalchemy.exc.IntegrityError as e:
    print("Integrity violation blocked!")
    session.rollback()
    


