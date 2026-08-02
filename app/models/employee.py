from app.extentions import db

class Employee(db.Model):

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key = True)

    first_name = db.Column(db.String(50), nullable = False)

    last_name = db.Column(db.String(50), nullable = False)

    email = db.Column(db.String(120), unique = True, nullable = False)

    phone = db.Column(db.String(15), nullable = True)

    gender = db.Column(db.String(10), nullable = True)

    joining_date = db.Column(db.Date, nullable = False)

    salary = db.Column(db.Numeric(10, 2), nullable = True)

    status = db.Column(db.String(20), default = 'Active')

    def __repr__(self):
          return f"<Employee {self.first_name} {self.last_name}>"