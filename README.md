## This will help you to create branch based on source branch and new branch name

#### Steps

```sh
$ pipenv shell
$ export token=<your-gitlab-token>
$ # add your repo path as given in repo.txt
$ python create-branch.py <source-branch-name> <destination-branch-name>
```
