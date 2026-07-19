from getpass import getpass
from hashlib import sha256

from data_layer.repositories.UserRepository import UserRepository


def hash_password(password: str) -> str:
    return sha256(password.encode("utf-8")).hexdigest()


def main() -> None:
    repo = UserRepository()

    print("Create a new user")
    email = input("Email: ").strip()
    name = input("Name: ").strip()
    password = getpass("Password: ")

    hashed_password = hash_password(password)
    user_id = repo.create(email=email, name=name, password=hashed_password)
    print(f"User created with id: {user_id}")

    lookup_id = input("Enter user id to fetch details: ").strip()
    user = repo.get_by_id(lookup_id)

    if user:
        print("\nUser details:")
        print(f"ID: {user.id}")
        print(f"Email: {user.email}")
        print(f"Name: {user.name}")
        print(f"Password hash: {user.password}")
        print(f"Created at: {user.created_at}")
    else:
        print("No user found with that id.")


if __name__ == "__main__":
    main()
