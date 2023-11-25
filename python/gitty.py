from github import Github
from github import Auth


auth = Auth.Token("kl;lkkjl")
gh = Github(base_url="https://github.com/api/v3", auth=auth)
repos = gh.get_repos()
#'user_login'
for r in repos:
    print(r.name)
