#!/bin/bash
#get Chromewebdriver

curl https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_mac64.zip -o $(pwd)/chromedriver.zip &&
unzip chromedriver.zip
