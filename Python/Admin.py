from Python.User import User


class Admin(User):
    def __init__(self, email, password, admin_id):
        super().__init__(email, password)
        self.admin_id = admin_id

    def get_admin_id(self):
        return self.admin_id

    def set_admin_id(self, admin_id):
        self.admin_id = admin_id


# admin = Admin("admin@example.com", "adminpassword", "A123")
