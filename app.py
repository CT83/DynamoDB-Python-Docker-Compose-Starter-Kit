import time

from pynamodb.attributes import (
    UnicodeAttribute
)
from pynamodb.models import Model


class User(Model):
    class Meta:
        table_name = 'User'
        host = "http://database:8000"

    full_name = UnicodeAttribute(hash_key=True)


if __name__ == '__main__':
    time.sleep(5)
    if not User.exists():
        print("User Table does not exist, creating one...")
        User.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    else:
        print("User Table already exists. Nice!")

    print("Exiting...")
