## initialize repository

```sh
mkdir tutorial
cd tutorial/
git init 
git remote add origin git@bitbucket.org:progtec2018/tutorial.git
git add .
git commit -m "first commit"
git config --global user.email "your email"
git config --global user.name "your username"
git commit -m "first commit"
git push origin master
```

## pull from remote to local

```sh
git pull origin master
```

## make branch

```sh
git branch make_p1
git checkout make_p1 
git branch 
git add .
git commit -m "make branch"
git push origin make_p1
```
    
## merge my branch into master

```sh
git checkout master
git pull
git merge --no-ff make_p1
git branch -d make_p1
```
