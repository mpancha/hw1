#!/bin/sh
#install pip
#sudo python get_pip.py
sudo pip install -r requirement.txt
chmod 500 keys/hw1.key
chmod 500 keys/aws_hw1.key
export ANSIBLE_HOST_KEY_CHECKING=false

