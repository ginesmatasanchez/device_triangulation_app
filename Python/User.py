class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.roles = set()

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

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
