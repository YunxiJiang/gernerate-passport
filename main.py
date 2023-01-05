import secrets
import string
import typer

def password(
    length: int = typer.Argument(16, help="The length of password."), 
    punctuation: bool = typer.Option(False,"--punctuation", "-P", help="Include punctuations in your password.", show_default=True)
    ):
    alphabet = ""
    if punctuation == True:
        alphabet = string.ascii_letters + string.digits+string.punctuation
    else:
        alphabet = string.ascii_letters + string.digits
    
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    print(password)


if __name__ == "__main__":
    typer.run(password)