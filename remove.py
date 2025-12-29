from pathlib import Path

def remove_all():
    home_dir = Path.home()
    file_path = home_dir / ".gitlist"

    try:
        with open(file_path, "w") as _:
            pass

    except IOError as e:
        print(f"Error: {e}")

def remove_user_by_label(label):
    home_dir = Path.home()
    file_path = home_dir / ".gitlist"

    found = None

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

    except IOError as e:
        print(f"Error: {e}")
        exit(1)

    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith(f'label="{label}"'):
            found = True
            i += 4
        else:
            new_lines.append(lines[i])
            i += 1

    if not found:
        print(f"Error: '{label}' is not found.")
        exit(1)

    try:
        with open(file_path, "w") as file:
            file.writelines(new_lines)

    except IOError as e:
        print(f"Error: {e}")
        exit(1)

def remove_user_by_username(username):
    home_dir = Path.home()
    file_path = home_dir / ".gitlist"

    found = None

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

    except IOError as e:
        print(f"Error: {e}")
        exit(1)

    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith(f'username="{username}"'):
            found = True

            # Pop the line before
            new_lines.pop()

            i += 3
        else:
            new_lines.append(lines[i])
            i += 1

    if not found:
        print(f"Error: '{username}' is not found.")
        exit(1)

    try:
        with open(file_path, "w") as file:
            file.writelines(new_lines)

    except IOError as e:
        print(f"Error: {e}")
        exit(1)

def remove_user_by_email(email):
    home_dir = Path.home()
    file_path = home_dir / ".gitlist"

    found = None

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

    except IOError as e:
        print(f"Error: {e}")
        exit(1)

    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith(f'email="{email}"'):
            found = True

            # Pop the lines before
            new_lines.pop()
            new_lines.pop()

            i += 2
        else:
            new_lines.append(lines[i])
            i += 1

    if not found:
        print(f"Error: '{email}' is not found.")
        exit(1)

    try:
        with open(file_path, "w") as file:
            file.writelines(new_lines)

    except IOError as e:
        print(f"Error: {e}")
        exit(1)

