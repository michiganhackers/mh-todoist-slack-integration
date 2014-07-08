#!/bin/bash

git checkout master
git reset --hard dev 
git commit -am "merge dev into master" --no-edit

