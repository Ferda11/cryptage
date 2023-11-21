from cryptage import *
cryptage_instance=cryptageTexte()
text=input("Entrer un mot:")
texte_chiffre = cryptage_instance.cryptage(text)
print(f"Le texte chiffré est : {texte_chiffre}")
print(f"Le texte chiffré est : {texte_decrypte}")
