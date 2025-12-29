import re
import shutil

def check_git_exists() -> bool:
    exists = shutil.which("git")
    if exists:
        return True
    else:
        return False

def check_username_valid(username) -> bool:
    """
    Check if username match the following rules:

    1. Usernames may only contain alphanumeric characters (letters and numbers) or single hyphens (-).
    2. Usernames cannot have multiple consecutive hyphens.
    3. Usernames cannot begin or end with a hyphen.
    4. The maximum length for a username is 39 characters
    """

    pattern =  f"^(?!.*--)[A-Za-z0-9]+(-[A-Za-z0-9]+)*$"

    if not re.fullmatch(pattern, username) or len(username) > 39:
        return False
    else:
        return True

def check_email_valid(email) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.fullmatch(pattern, email):
        return True
    else:
        return False
