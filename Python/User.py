"""import dbm
from shelve import DbfilenameShelf as db


class User(dbm.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))"""
    
class User:
    def __init__(self, name, password, email, id_company, id_profile, mobile_number, created, last_login, active):
        self.name = name
        self.password = password
        self.email = email
        self.id_company = id_company
        self.id_profile = id_profile
        self.mobile_number = mobile_number
        self.created = created
        self.last_login = last_login
        self.active = active
        self.roles = set()



    
    
    
    # Getter y Setter para la propiedad "name"
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Getter y Setter para la propiedad "password"
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    # Getter y Setter para la propiedad "email"
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    # Getter y Setter para la propiedad "id_company"
    @property
    def id_company(self):
        return self._id_company

    @id_company.setter
    def id_company(self, value):
        self._id_company = value

    # Getter y Setter para la propiedad "id_profile"
    @property
    def id_profile(self):
        return self._id_profile

    @id_profile.setter
    def id_profile(self, value):
        self._id_profile = value

    # Getter y Setter para la propiedad "mobile_number"
    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self._mobile_number = value

    # Getter y Setter para la propiedad "created"
    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value

    # Getter y Setter para la propiedad "last_login"
    @property
    def last_login(self):
        return self._last_login

    @last_login.setter
    def last_login(self, value):
        self._last_login = value

    # Getter y Setter para la propiedad "active"
    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
        
        
    def get_roles(self):
        return self.roles

    def set_roles(self, roles):
        self.roles = roles

    def add_role(self, role):
        self.roles.add(role)

    def remove_role(self, role):
        self.roles.remove(role)


class MapAccessController:
    users = []

    @staticmethod
    def main():
        # Create users
        user1 = User("user1@example.com", "password1")
        user2 = User("user2@example.com", "password2")
        admin = User("admin@example.com", "adminpassword")

        # Assign roles to users
        user1.add_role("user")
        user2.add_role("user")
        admin.add_role("admin")

        # Add users to the list
        MapAccessController.users.append(user1)
        MapAccessController.users.append(user2)
        MapAccessController.users.append(admin)

        # Simulate login
        logged_in_user = MapAccessController.login("user1@example.com", "password1")

        # Verify map access based on user role
        if logged_in_user:
            if "admin" in logged_in_user.get_roles():
                print("Acceso completo al mapa")
                # Code to show the complete map would go here
            elif "user" in logged_in_user.get_roles():
                print("Acceso limitado al mapa")
                # Code to show a map with limited access would go here
            else:
                print("Acceso denegado al mapa")
                # Code to show an access denied message would go here
        else:
            print("Inicio de sesión fallido")
            # Code to show a login failed message would go here

    @staticmethod
    def login(email, password):
        for user in MapAccessController.users:
            if user.get_email() == email and user.get_password() == password:
                return user
        return None
