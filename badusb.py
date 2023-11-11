from pyadb import adb

# Connecter le PC et le téléphone Android via USB
d = adb.device()

# Exemple de commande pour contrôler le PC à partir du téléphone Android
d.shell("ls")  # Exécuter la commande "ls" sur le PC

# Vous pouvez ajouter d'autres commandes pour contrôler votre PC ici
#pyadb