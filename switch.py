import subprocess
from pathlib import Path

def switch_user(username, email, local):
    username_cmd = (
        ["git", "config", "user.name", username]
        if local
        else ["git", "config", "--global", "user.name", username]
    )

    email_cmd = (
        ["git", "config", "user.email", email]
        if local
        else ["git", "config", "--global", "user.email", email]
    )

    subprocess.run(username_cmd)
    subprocess.run(email_cmd)

def switch_user_by_label(label, local):
    home_dir = Path.home()
    file_path = home_dir / ".gitlist"

    try:
        username = None
        email = None
        found = False

        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if line.startswith(f'label="{label}"'):
                    found = True
                elif found:
                    if line.startswith("username="):
                        username = line.split('"')[1]
                    elif line.startswith("email="):
                        email = line.split('"')[1]

                    if username and email:
                        break

        if found and username and email:
            switch_user(username, email, local)
        else:
            print(f"Error: '{label}' is not found in git list.")
            exit(1)

    except IOError as e:
        print(f"Error: {e}")
        exit(1)

def switch_user_by_username(username, local):
    home_dir = Path.home()
    file_path = home_dir / ".gitlist"

    try:
        email = None
        found = False

        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if line.startswith(f'username="{username}"'):
                    found = True
                elif found:
                    if line.startswith("email="):
                        email = line.split('"')[1]

                    if username and email:
                        break

        if found and username and email:
            switch_user(username, email, local)
        else:
            print(f"Error: '{username}' is not found in git list.")
            exit(1)

    except IOError as e:
        print(f"Error: {e}")
        exit(1)

def switch_user_by_email(email, local):
    home_dir = Path.home()
    file_path = home_dir / ".gitlist"

    try:
        lines_buf = []
        username = None
        found = False

        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if line.startswith(f"label="):
                    continue

                lines_buf.append(line)

                # Limit buffer just to free up some spaces
                if len(lines_buf) > 2:
                    lines_buf.pop(0)

                if line.startswith(f'email="{email}"'):
                    found = True

                    for prev_line in reversed(lines_buf[:-1]):
                        if prev_line.startswith("username="):
                            username = prev_line.split('"')[1]

                    break

        if found and username and email:
            switch_user(username, email, local)
        else:
            print(f"Error: '{email}' is not found in git list.")
            exit(1)

    except IOError as e:
        print(f"Error: {e}")
        exit(1)

