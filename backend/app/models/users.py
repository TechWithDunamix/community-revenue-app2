from .base import BaseModel,fields,BaseUserModel

class Users(BaseModel,BaseUserModel):
    password = fields.CharField(max_length=50)
    email = fields.CharField(max_length=50)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    date_of_birth = fields.DateField(null=True)
    country_of_residence = fields.CharField(max_length=50)
    quarter = fields.CharField(max_length=50)
    age_grade = fields.CharField(max_length=50)
    kindred = fields.CharField(max_length=50)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'country_of_residence': self.country_of_residence,
            'quarter': self.quarter,
            'age_grade': self.age_grade,
            'kindred': self.kindred
        }
    class Meta:
        order_by = ('username',)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.get_obj(email=email)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.get_obj(username=username)

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get_obj(id=user_id)

    @classmethod
    def get_all(cls):
        return cls.query.all_data()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    