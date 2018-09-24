#!/bin/bash
# Connect to AWS EC2 Instance
echo -e "Please enter your public DNS: "
read dns
ssh -i testInstancekeypair.pem ec2-user@$dns 'bash -s' < ec2-update.sh
ssh -i testInstancekeypair.pem ec2-user@$dns

