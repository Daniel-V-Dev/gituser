from pathlib import Path
from helper import check_email_valid

def add_user(username, email, label):
    if not check_email_valid(email):
        print(f"Error: '{email}' is not a valid email.")
        exit(1)

    home_dir = Path.home()
    file_path = home_dir / ".gitlist"

    new_content = f'\nlabel="{label}"\nusername="{username}"\nemail="{email}"\n'

    try:
        with open(file_path, "a+") as file:
            file.seek(0)
            content = file.read()

            # Check if user already exists
            if (
                (f'label="{label}"' in content and label) or
                f'username="{username}"' in content or
                f'email="{email}"' in content
            ):
                print("Error: User already existed.")
                exit(1)

            file.write(new_content)

    except IOError as e:
        print(f"Error: {e}")
        exit(1)
