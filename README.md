# hw1
DevOps HW1

Requirements
------------
Must have following installed
1. Python
2. pip installed

How to Run
----------
1. Setup Environment
   - Makes sure all dependencies are satisfies as per requirement.txt 
   ```
   ./setup.sh
   ```
2. Generate Inventory by spinning instance on AWS and digitalocean

   ```
   ./hw1_code.py inventory
   ```
3. Deploy nginx on hosts from generated inventory
   
   ```
   ./hw1_code.py deploy
   ```

