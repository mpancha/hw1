# Homework 1
Deliverables
------------
1. [Code](hw1_code.py)
2. [Ansible Playbook](server_play.yml)
3. [Screencast](final_screencast.mp4)

Amazon EC2
-----------
Amazon Elastic Compute Cloud is on-demand compute service from Amazon. It provides scalable and flexible compute service which can be payed only for the capacity you actually use. EC2 instance can be provisioned easily from aws web interface or using AWS API.

Requirements
------------
Must have installed

1. Python v2.7
2. pip 

How to Run
----------
1. Clone this repo 

   ```
   git clone https://github.com/mpancha/hw1.git
   ```
2. Create rootkey.csv file in keys directory with following format.

  ```
  AWS_ACCESS_KEY_ID=<aws access key id>
  AWS_SECRET_KEY=<aws secret key>
  digital_token=<digitalocean token>
  ```
3. Setup Environment
   - Makes sure all dependencies are satisfies as per [requirement.txt](requirement.txt) 

   ```
   ./setup.sh
   ```
4. Generate Inventory by spinning instance on AWS and digitalocean

   ```
   ./hw1_code.py inventory
   ```
5. Deploy nginx on hosts from generated inventory

   ```
   ./hw1_code.py deploy
   ```

Screencast
----------
[screencast](https://github.com/mpancha/hw1/blob/master/final_screencast.mp4)
