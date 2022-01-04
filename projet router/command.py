# -*- coding: utf-8 -*

from ssh1 import ssh
import time
import paramiko



rout="ip route"
Inter_R="ip a"

ping = " ping "


## Affichage de table de routage 

#def affiche_interface(rout;hostname, port , username,password):  
#    connect=ssh(hostname=hostname, port=port, username=username, password=password)
#    connect.sendCommand("sudo ip a")
#    print(" Successfully")
#    print("sudo ip a")

## Affichage de tous les interfaces 
#def affiche_TRoutage(rout;hostname, port , username,password):  
#    connect=ssh(hostname=hostname, port=port, username=username, password=password)
#    connect.sendCommand("sudo ip route")
#    print(" Successfully")
#    print("sudo ip route")
## Affichage de tous les interfaces 
#def showip():
#    l=[" sudo ip a"]
#    return l
#
## Affichage de table de routage 
#def showr(): # affiche @ip des interfaces
#    l=[" sudo ip route"]
#    return l
# changement le nom de routeur 
def hn1(a1, hostname, port , username,password):  
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo hostnamectl set-hostname "+ a1)
    print("Changement le nom ==> Successfully")
    print("sudo hostnamectl set-hostname " +a1)

    
#ajouter une adresse Ip et masque     
def confR(a3,a4,hostname, port , username,password): #configurer @ip
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr add "+ a3 + " dev " + a4)
    print("Ajouter @ IP et Masque ==> Successfully")
    print("sudo ip addr add "+ a3 + " dev " + a4)
    
    
#Supprimer une address ip et masque     
def dellip(a3,a4,hostname, port , username,password):
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr del "+ a3 + " dev " + a4) 
    print("Supprimer @ IP et Masque ==> Successfully")
    print("sudo ip addr del "+ a3 + " dev " + a4)



#Desactiver une interface
def shut(a4,hostname, port , username,password):
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand(" sudo ifdown " + a4)
    print("Interface Activer ==> Successfully")
    print(" sudo ifdown " + a4)


#activer une interface    
def up(a4,hostname, port , username,password):
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ifup " + a4)
    print("Interface Desactiver ==> Successfully")
    print("sudo ifup " + a4)

#Ajouter une Passarelle Par Defaut    
#def Defaut(a2,hostname, port , username,password):
#    connect=ssh(hostname=hostname, port=port, username=username, password=password)
#    connect.sendCommand("sudo ip route add default via " + a2)
#    print("ajouter une Passarelle par Defaut ==> Successfully")
#    print("sudo ip route add default via " + a2)

def add_defaut_R1(a4, hostname, port, username, password): #configurer @ip
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip route add default via "+ a4 +"eth1 ")    
   
    
    
    
 #affichage de table de routage    
def afficherRoutage1(rout):
    
    hostname = "192.168.1.39"
    username = "etudiant"
    password = "vitrygtr"
    port = 22
    
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname,username=username,password=password)
    # print ("Successfully connected to", ip_address)
    
    rm = ssh_client.invoke_shell()

    rm.send( rout + "\n")
    time.sleep(2)

    resp = rm.recv(9999999)
    resultat = resp.decode('ascii').split(',')
    a = (''.join(resultat))
    return(a) 
 #affichage d'interface reseaux   
def afficherInterface(Inter_R):
    
    hostname = "192.168.1.39"
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
    
    
#affichage le ping ( la resuktat ) si sa fonctionne ou non  
def afficherPing(ping):
    
    hostname = "192.168.1.39"
    username = "etudiant"
    password = "vitrygtr"
    port = 22
    
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname,username=username,password=password)
    # print ("Successfully connected to", ip_address)
    
    rm = ssh_client.invoke_shell()

    rm.send( ping + "\n")
    time.sleep(1)

    resp = rm.recv(9999999)
    resultat = resp.decode('ascii').split(',')
    c = (''.join(resultat))
    return(c)
    
#def shw_ip(hostname, port , username,password):  
#    connect=ssh(hostname=hostname, port=port, username=username, password=password)
#    connect.sendCommand("sudo ip a ")
#    print("show ==> Successfully")
#    print(connect.sendCommand("sudo ip a "))
#for x in addUser():
    #print(x)
    
#def ss(): #configurer @ip
    #l=["ssh -l rt 192.168.2.2","vi"]
    #return l

    
