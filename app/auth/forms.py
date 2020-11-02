from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email Address',validators=[Required(),Email()])
    author = StringField('Author',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Password must match')])
    password_confirm = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_author(self,data_field):
        if User.query.filter_by(author = data_field.data).first():
            raise ValidationError('The author name is exists')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
