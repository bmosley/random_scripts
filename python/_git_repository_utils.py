

def _check_git_repository(directory):
    # Verify directory is a git repository
    try:
        _ = git.Repo(directory).git_dir
        return True

    except git.exc.InvalidGitRepositoryError:
        logger.error("{} is not a valid git repository. Unable to clone to directory safely.".format(directory))
        return False


def setup_repository(repository_dict):
    try:
        import git
    except ImportError as import_error:
        logger.warning('GitPython not installed. Installing with setup utility: {}'.format(import_error))
        git_pypi = {"GitPython": "git"}
        setup_pypi_packages(git_pypi)

    try:
        import git
    except ImportError as import_error:
        logger.exception(import_error)
        return

    home_dir = os.path.expanduser("~/")

    for repo, url in repository_dict.items():
        local_dir = os.path.join(home_dir, repo)

        # Check that the local_dir (repository directory) exists in the location
        if not os.path.exists(local_dir):
            # Clone the repository to local_dir
            git.Repo.clone_from(url, local_dir)
            logger.info("{} cloned to {}".format(repo, local_dir))
            continue

        # Update repositories that already exist
        try:
            _ = git.Repo(local_dir).git_dir
        except git.exc.InvalidGitRepositoryError:
            logger.error("{} is not a valid git repository. Unable to clone to directory safely.".format(local_dir))

        # Destroy any non-committed changes in HEAD
        local_repo = git.Repo(local_dir)
        local_repo.head.reset(index=True, working_tree=True)

        # Pull original
        git_repo = git.Repo(local_dir)
        git_repo.remotes.origin.pull()

        # Print some info to the console
        logger.info("{} is up-to-date.".format(repo))
        logger.info("Current active branch is '{}'.".format(git_repo.active_branch))
