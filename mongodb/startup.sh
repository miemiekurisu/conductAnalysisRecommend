#!/bin/sh
currentpath=$(dirname $_)
$currentpath/bin/mongod --dbpath $currentpath/data