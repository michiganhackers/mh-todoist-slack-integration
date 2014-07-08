#!/bin/bash

git checkout master
git reset --hard dev 
cp -r ./src/* ./
rm -rf ./src/
git commit -am "merge dev into master" --no-edit
git push --force origin master

