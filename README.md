# Updating the Website

To push your changes to the live website, first set up a remote pointing to the server.
 - With AFS: `git remote add live /afs/csail.mit.edu/group/cap/www.git`
 - With ssh: `git remote add live ssh://USER@sketch2.csail.mit.edu:/afs/csail.mit.edu/group/cap/www.git`

Then, push to the server. Only the master branch needs to be pushed.
```
git push live +master:refs/heads/master
```

See also https://gist.github.com/Nilpo/8ed5e44be00d6cf21f22
