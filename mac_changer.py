import os
import random

def get_hex():
     letters = ['a', 'b', 'c', 'd', 'e', 'f', '0' , '1', '2', '3', '4', '5', '6', '7', '8', '9']
     return random.choice(letters)

def get_mac():
     new_mac = ""
     for i in range(0,5):
          new_mac += get_hex() + get_hex() + ":"
     new_mac += get_hex() + get_hex()
     print new_mac
  
command = "sudo ifconfig en1 ether"
print "Old MAC address: ",
os.system("ifconfig en1 | grep ether")
new_mac = get_mac()
os.system(command + " " + new_mac)
print "\nNew MAC address: ",
os.system("ifconfig en1 | grep ether")