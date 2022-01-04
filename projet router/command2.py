# -*- coding: utf-8 -*-
"""
Created on Sun May  2 10:28:52 2021

@author: youssef
"""
from ssh1 import ssh
import time
import paramiko

Inter_R="ip a"




def hn1(a1, hostname, port , username,password):  
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo hostnamectl set-hostname "+ a1)
    print("Changement le nom ==> Successfully")
    print("sudo hostnamectl set-hostname " +a1)
    
    
def afficherInterface(Inter_R):
    
    hostname = "192.168.1.40"
    username = "etudiant"
    password = "vitrygtr"
    port = 22
    
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname,username=username,password=password)
    # print ("Successfully connected ")
    
    rm = ssh_client.invoke_shell()

    rm.send( Inter_R + "\n")
    time.sleep(2)

    resp = rm.recv(9999999)
    resultat = resp.decode('ascii').split(',')
    b = (''.join(resultat))
    return(b)