class Profile:
    def __init__(self, description, created, active):
        self._description = description
        self._created = created
        self._active = active

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
