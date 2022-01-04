# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:17:56 2021

@author: youssef
"""

from paramiko import client
import getpass, sys


class ssh :
    client =None 
    
    def __init__(self,hostname, port, username, password):
        try:
            print("Connecting to server.") # message à afficher si ça fonctionne
            self.client=client.SSHClient() #Instance d'un client SSH
            self.client.set_missing_host_key_policy(client.AutoAddPolicy()) #ajouter automatiquement les clé RSA si n'existe pas 
            self.client.connect(hostname, port=port, username=username, password=password) #La connexion avec le serveur SSH (secure shell)
            
        except:
            print("Exception raised !")
            
    def sendCommand(self, command):
        if(self.client):
            stdin,stdout,stderr= self.client.exec_command(command)
            #j'execute une commande a distance sur mon ssh
            #la commande exec_command enregistre des fichiers tel que 
            #stdin: Passer des configurations 
            #stdout: contient le resultat du terminal
            #stderr: contient les erreurs du terminal
            print (stdout.read().decode())  
            #on affiche le contenu du fichier stdout
        else:
            print("Connection not opened.")
        self.client.close()
        # on ferme la connexion 

#hostname="192.168.1.39"
#username="etudiant"
#password="vitrygtr"
#port=22
#hostname= sys.argv[1]
#port=sys.argv[2]
#username=sys.argv[3]
#password=getpass.getpass("Mot de passe: ")

if __name__ == "__main__":
    user = ssh(hostname,port,username,password)
    
    user.sendCommand("ip a")


            
            