from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute)
from pynamodb.models import Model


class User(Model):
    class Meta:
        table_name = 'User'
        host = "http://database:8000"

    id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute()

    def __repr__(self):
        return "<User {} name:{}>".format(self.id, self.name)


if __name__ == '__main__':
    if not User.exists():
        print("User Table does not exist, creating one...")
    else:
        print("User Table already exists.")
        print("Deleting and recreating the User Table...")
        User.delete_table()
    User.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

    print("Adding items to the table...")
    user = User(id=0, name="Rohan")
    user.save()

    print("Selecting users from User Table...")
    stored_user = User.get(0)
    print(stored_user)

    print("Scanning users from User Table...")
    for user in User.scan(User.name == "Rohan"):
        print(user)

    print("Exiting...")
