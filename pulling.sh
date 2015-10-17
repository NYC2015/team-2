#!/bin/bash
echo $HOME
export HOME='/home/ubuntu'
echo $HOME
x = $(env -i git config --global credential.helper 'cache --timeout=360000')
while true; do
env -i git pull
sleep 1
done
