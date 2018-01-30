#!/bin/bash
# Update the EC2 instance once we have connected

yes | sudo yum update
yes | wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
yes | sudo yum install git
yes yes | bash Anaconda3-5.0.1-Linux-x86_64.sh
