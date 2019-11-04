import hydra
from dotenv import load_dotenv
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute)
from pynamodb.models import Model


class User(Model):
    class Meta:
        table_name = 'User'
        host = None

    id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute()

    def __repr__(self):
        return "<User {} name:{}>".format(self.id, self.name)


@hydra.main(config_path='env-config.yml')
def main(cfg):
    load_dotenv()  # Load env. vars
    set_config(cfg)

    if not User.exists():
        print("User Table does not exist, creating one...")
    else:
        print("User Table already exists.")
        print("Deleting and recreating the User Table...")
        User.delete_table()
    User.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

    print("Adding user to the table...")
    user = User(id=0, name="Rohan")
    user.save()

    print("Selecting users from User Table...")
    stored_user = User.get(0)
    print(stored_user)

    print("Scanning users from User Table...")
    for user in User.scan(User.name == "Rohan"):
        print(user)
    print("Exiting...")


def set_config(cfg):
    """Picks up the settings from the config files and automatically decides between using Local vs AWS DynamoDB"""
    if cfg.db.service == 'docker':
        print("Running with Local DynamoDB...")
        db_path = cfg.get('db').get('path') or None
        User.Meta.host = db_path
    print("Running with AWS DynamoDB using the credentials in the .env file...")


if __name__ == "__main__":
    main()
