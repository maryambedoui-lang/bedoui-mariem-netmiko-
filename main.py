print("Hello, Git!")
# main.py
from netmiko import ConnectHandler

def acces_netmiko():
    cisco_router = {
        "device_type": "cisco_xr",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }

    # Connexion au routeur
    net_connect = ConnectHandler(**cisco_router)
    
    # Afficher la date côté routeur
    clock = net_connect.send_command("show clock")
    print("Date du routeur:", clock)
    
    # Afficher les interfaces dans un fichier
    interfaces = net_connect.send_command("show interfaces")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)
    
    net_connect.disconnect()

def dire_bonjour():
    print("Hello, Git!")

# Exemple d'utilisation
if __name__ == "__main__":
    dire_bonjour()
    acces_netmiko()
def dire_salut():
    print("Salut, Git!")

# Exemple d'utilisation
if __name__ == "__main__":
    dire_bonjour()
    acces_netmiko()
    dire_salut()
