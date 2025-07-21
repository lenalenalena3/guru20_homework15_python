from model.pages.login_page import LoginPage
from model.pages.github_page import GitHubPage


class Application:
    def __init__(self):
        self.github_page = GitHubPage()
        self.login_page = LoginPage()


app = Application()
