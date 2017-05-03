# Contribution Guidelines

## Best practices
- Never commit sensitive credentials or other information into the repo.
- Sensitive data should be injected into the application through environment variables.

## Git Commit Guidelines
- Use present tense for commit messages

## Git workflow
Based off of the [workflow proposed by Vincent Driessen](http://nvie.com/posts/a-successful-git-branching-model/), we have two main branches -- `master` and `dev`, where `master` is "the main branch where the source code of HEAD always reflects a production-ready state." `dev` is the "the main branch where the source code of HEAD always reflects a state with the latest delivered development changes for the next release."

Our workflow begins with deploying supporting branches off of `dev` for work, which may include branches for "hotfixes" (i.e. urgent bug fixing) or new features. 

### Feature Branches
When new feature development begins, create a branch off of `dev`:

    git checkout -b adding-new-feature dev

New feature branches can be named anything except for `master` or `dev`. Once you are done working on your new feature, commit your code and push your branch to the repo:

    git commit -m 'made some changes'
    git push

Once your branch is pushed up to the repo, navigate to the [pull request section on GitHub](https://github.com/studenton/minor-project/compare?expand=1) and [create a pull-request](https://help.github.com/articles/creating-a-pull-request/) from the base of `dev` to your feature branch. Write any comments that are relevant, tag users or reference issues.  

After the pull-request is submitted and the code is reviewed and approved, the feature branch will be merged into `dev`, and that feature branch will be closed. The can be done on GitHub or via command line:

    git pull origin dev
    git checkout dev
    git merge --no-ff adding-new-feature
    git branch -d myfeature
    git push origin dev

When `dev` is ready to be merged into `master`, it can be merged either via a pull request on GitHub or merged via command line:

    git pull origin master
    git checkout master
    git merge --no-ff dev
    git push origin master
    git checkout dev

### Hotfix Branches
If a critical bug in production needs to be addressed, create a branch off of `master` prefixed with `hotfix-`:
  
    git pull origin master
    git checkout -b hotfix-some-kind-of-bug master

When the bug is squashed, the hotfix branch needs to be merged into `master` and `develop`. first `master`:

    git pull origin master
    git checkout master
    git merge --no-ff hotfix-some-kind-of-bug
    git push origin master

and then `dev`:
    
    git pull origin dev
    git checkout dev
    git merge --no-ff hotfix-some-kind-of-bug
    git push origin dev

After both `master` and `dev` are updated, you can close the hotfix branch:

    git branch -d hotfix-some-kind-of-bug
