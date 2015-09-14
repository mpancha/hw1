#!/bin/sh

echo "build package"
npm install

echo "Create droplet"
node createDroplet.js

echo "Destroy droplet"
node destroyDroplet.js
