import click
import subprocess
import sys
from helper import check_git_exists
from switch import switch_user_by_email, switch_user_by_label, switch_user_by_username
from add import add_user
from remove import remove_all, remove_user_by_label, remove_user_by_username, remove_user_by_email

@click.group()
def cli():
    """
    Git user management CLI
    """
    pass

@cli.command("show", help="Show current user info in global config.")
@click.option("-l", "--local", is_flag=True, help="Show user info in local config.")
def show(local):
    username_cmd = (
        ["git", "config", "user.name"]
        if local
        else ["git", "config", "--global", "user.name"]
    )

    email_cmd = (
        ["git", "config", "user.email"]
        if local
        else ["git", "config", "--global", "user.email"]
    )

    result_username = subprocess.run(username_cmd,
                                     text=True,
                                     check=False,
                                     capture_output=True).stdout.strip()

    result_email = subprocess.run(email_cmd,
                                  text=True,
                                  check=False,
                                  capture_output=True).stdout.strip()

    click.echo(result_username)
    click.echo(result_email)

@cli.command("switch", help="Switch to other user.")
@click.option("-lb", "--label", is_flag=False, help="Switch to other user by label.")
@click.option("-u", "--username", is_flag=False, help="Switch to other user by username.")
@click.option("-e", "--email", is_flag=False, help="Switch to other user by email.")
@click.option("-l", "--local", is_flag=True, help="Switch to other user only for local repo.")
def switch(label, username, email, local):
    if label:
        switch_user_by_label(label, local);
    elif username:
        switch_user_by_username(username, local)
    else:
        switch_user_by_email(email, local)

@cli.command("add", help="Add new user to git list.")
@click.argument("username")
@click.argument("email")
@click.option("-lb", "--label", default="", is_flag=False, help="Add a label for quick reference.")
def add(username, email, label):
    add_user(username, email, label)

@cli.command("remove", help="Remove user from git list.")
@click.option("-a", "--all", is_flag=True, help="Remove all user from git list.")
@click.option("-lb", "--label", default="", is_flag=False, help="Remove user from git list by label.")
@click.option("-u", "--username", is_flag=False, help="Remove user from git list by username.")
@click.option("-e", "--email", is_flag=False, help="Remove user from git list by email.")
def remove(username, email, label, all):
    if all:
        remove_all()
    elif label:
        remove_user_by_label(label)
    elif username:
        remove_user_by_username(username)
    else:
        remove_user_by_email(email)

if __name__ == "__main__":
    if not check_git_exists():
        click.echo("Error: Git doesn't exists in your system.")
        sys.exit(1)

    cli()
