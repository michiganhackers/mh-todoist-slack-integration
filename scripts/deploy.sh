#!/bin/bash

git checkout master
git reset --hard dev 
cp -r ./src/* ./
rm -rf ./src/
git commit -am "deploy dev to heroku" --no-edit
git push --force heroku master

