# SQLAlchemy & Alembic
# Alembic keep a hierarchical model of our tables. This way, any change of the model will be registered by Alembic.
# By running migrations, a new migrations file will be added in order to apply the table change. Through this method,
# we can easily do a rollback to a previous version. While adding a new column it's better to set a 'default' for the
# new column so that the previous data will not be affected in any way. You can change the database model without losing
# the already inserted data.
# Alembic also allows to execute a downgrade specifying the number of levels you want to go back. Similarly, the
# version we downgraded from can be restored. It is better not to manually change the files located in the versions
# folder because these versions may depend one from another and any change may result into unexpected errors.

# SQLAlchemy is a useful tool that helps us manage database entries using an object oriented manner. For example, here
# each table is an object and it's attributes represent the table headers for each column. Using SQLAlchemy we can
# easily insert data into our database or retrieve it without using SQL statements.

from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, DOUBLE, DATETIME
from sqlalchemy.orm import relationship

SQLAlchemyBase = declarative_base()


class CustomBaseModel:
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    created_at = Column(DATETIME, server_default=func.now())
    update_at = Column(DATETIME, server_default=func.now(), server_onupdate=func.now())

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Student(SQLAlchemyBase, CustomBaseModel):
    __tablename__ = 'students'
    first_name = Column(VARCHAR(128), nullable=False)
    last_name = Column(VARCHAR(128), nullable=False)
    email = Column(VARCHAR(128), nullable=False, unique=True)
    graded_subjects = relationship('Subject', secondatory='student_grades')


class Subject(SQLAlchemyBase, CustomBaseModel):
    __tablename__ = 'subjects'
    name = Column(VARCHAR(128), nullable=False, unique=True)
    graded_users = relationship(Student, secondatory='')


class Grade(SQLAlchemyBase, CustomBaseModel):
    __tablename__ = 'student_grades'
    user_id = Column(INTEGER, ForeignKey(Student.id))
    user = relationship(Student)
    subject_id = Column(INTEGER, ForeignKey(Subject.id))
    subject = relationship(Subject)
    value = Column(DOUBLE(precision=4, scale=2), nullable=False)


a = Student(first_name='Ionel')







