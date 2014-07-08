#!/bin/bash

git add . --all
git commit -am "commit local changes before merge to master" --no-edit
git checkout master
git reset --hard dev 
cp -r ./src/* ./
rm -rf ./src/
git add . --all
git commit -am "deploy dev to heroku" --no-edit
git push --force heroku master

