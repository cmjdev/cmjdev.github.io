rem String input as only argument
rem Commit -m 'date update'
rem Push to remote

set mdate=%date:~10,4%%date:~7,2%%date:~4,2%

git pull
update.py %1
git add .
git commit -m "%mdate% update"
git push origin master

echo %1