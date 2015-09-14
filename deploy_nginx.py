#!/usr/bin/python

import boto.ec2
import subprocess
import ansible.runner
from ansible.inventory import Inventory
import digitalocean
import time
import webbrowser

aws_access = 'AKIAI6HVXS3JHOZYQF6Q'
aws_secret = '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'
digital_token = "22e87341d8662ea4d49d35dc2fcaccf6a6e50d7e43bb486509e50a1639d3e234"
droplet=''
aws_con=''
def create_aws_instance():
   ''' use access key and '''
   aws_con = boto.ec2.connect_to_region("us-east-1")
   aws_con.run_instances('ami-d05e75b8',key_name='aws_hw1',instance_type='t2.micro', security_groups=['hw1'])

def create_digital_instance():
    droplet = digitalocean.Droplet(token=digital_token, 
                                   name='hw1droplet', 
                                   region='nyc2', 
                                   image='ubuntu-14-04-x64', 
                                   size_slug='512mb',
				   ssh_keys = [1271814])
    droplet.create()
    print droplet
    print "Droplet Created"

def destroy_digital_instance():
    manager = digitalocean.Manager(digital_token)
    droplets = manager.get_all_droplets()
    for drop in droplets:
         drop.shutdown()

#print "Creating instance"
#create_instance()
dns_name=''
def get_aws_reservation():
   con = boto.ec2.connect_to_region("us-east-1")
   reservations = con.get_all_reservations()
   print reservations
   for res in reservations:
       print res
       for instance in res.instances:
          print instance
          print instance.state
          if instance.state == "running":
             return instance.ip_address
   return None

def get_digital_reservation():
   manager = digitalocean.Manager(token=digital_token)
   droplets = manager.get_all_droplets()
   for droplet in droplets:
      actions = droplet.get_actions()
      for action in actions:
         action.load()
         if action.status == "completed":
              return droplet.ip_address
   return None

def run_script_on_instance():
   cmd = "ssh -i hw1.pem ubuntu@"+dns_name+" myscript.sh"
   subprocess.check_output(cmd)

#print "Get reservation"
#get_reservation()
#print "Run script"
#run_script_on_instance()
# create inventory file
print "Creating digitalocean droplet"
create_digital_instance()
print "Creating AWS EC2 instance"
create_aws_instance()
dropletIp=None
while dropletIp == None:
   time.sleep(30)
   dropletIp = get_digital_reservation()
   print "Droplet not ready, retry after 30 sec" 
print "Droplet IP ="+dropletIp
aws_ip=None
while aws_ip == None:
   time.sleep(30)
   aws_ip = get_aws_reservation()
   print "AWS Instance not ready, retry after 30 sec"
print "AWS instance IP =" + aws_ip
   
digital_inv = "droplet ansible_ssh_host="+dropletIp+" ansible_ssh_user=root ansible_ssh_private_key_file=./keys/hw1.key\n"
aws_inv = "aws ansible_ssh_host="+aws_ip+" ansible_ssh_user=ubuntu ansible_ssh_private_key_file=./keys/aws_hw1.key"
print digital_inv
print aws_inv
with open("inventory","w") as f:
    f.write(digital_inv)
    f.write(aws_inv)
print "Inventory updated"

runner = ansible.runner.Runner(
   module_name='ping',
   module_args='',
   pattern='*',
   forks=10,
   inventory=Inventory('inventory')
)
nginx_install = ansible.runner.Runner(
   module_name='apt',
   module_args='pkg=nginx state=installed update_cache=true',
   pattern='*',
   forks=10,
   inventory=Inventory('inventory')
)
nginx_start = ansible.runner.Runner(
   module_name='shell',
   module_args='nginx',
   pattern='*',
   forks=10,
   inventory=Inventory('inventory')
)
print "Run ansible task: nginx_install"
datastructure = nginx_install.run()
#print( datastructure )
print "Run ansible task: nginx_start"
datastructure = nginx_start.run()
#print( datastructure )
webbrowser.open_new_tab("http://"+aws_ip)
webbrowser.open_new_tab("http://"+dropletIp)
