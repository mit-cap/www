# Updating the Website

To push your changes to the live website, first set up a remote pointing to the server.
```
git remote add live /afs/csail.mit.edu/group/cap/www.git
```
Then, push to the server. Only the master branch needs to be pushed.
```
git push live +master:refs/heads/master
```

See also https://gist.github.com/Nilpo/8ed5e44be00d6cf21f22
