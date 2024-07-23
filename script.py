import os

def print_repo_name():
    repo_name = os.getenv('REPO_NAME')
    if repo_name:
        print(f"The repository name is: {repo_name}")
    else:
        print("REPO_NAME environment variable is not set.")

if __name__ == "__main__":
    print_repo_name()
