# hw1

AWS service
-----------
CodeDeploy
- 

Requirements
------------
Platform : Ubuntu 14.04.

Must have installed

1. Python v2.7
2. pip 

How to Run
----------
1. Setup Environment
   - Makes sure all dependencies are satisfies as per requirement.txt 
   ```
   ./setup.sh
   ```
2. Create rootkey.csv file in keys directory with following format.

  ```
  AWS_ACCESS_KEY_ID=<aws access key id>
  AWS_SECRET_KEY=<aws secret key>
  digital_token=<digitalocean token>
  ```
3. Generate Inventory by spinning instance on AWS and digitalocean

   ```
   ./hw1_code.py inventory
   ```
4. Deploy nginx on hosts from generated inventory
   
   ```
   ./hw1_code.py deploy
   ```

