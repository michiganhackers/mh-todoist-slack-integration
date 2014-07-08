#!/bin/bash

if git diff-index --quiet HEAD --; then
# no changes
git checkout master
git reset --hard dev 
cp -r ./src/* ./
rm -rf ./src/
git add . --all
git commit -am "deploy dev to heroku" --no-edit
git push --force heroku master
git checkout dev
else
    echo "Deploy failed. You have unsaved changes in your branch."
fi
