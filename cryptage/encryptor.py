
class cryptageTexte:
    def __init__(self):
        self.cle_secrete = self.saisir_cle()
    def saisir_cle(self):
        compt=3
        while compt>0:
            cle_secrete=input("Entrer la cle secrete:")
            if cle_secrete=='Ferda@11':
                return cle_secrete
            else:
                compt-=1
                print(f"cle incorrecte, il vous reste {compt} {'essais'if compt==1 else 'essais'}")
            if compt==0:
                print("vous ne pouvez pas essayer a nouveau")
                exit()
        

    def cryptage(self,text):
        cryptage_text = ""
        long_cle = len(self.cle_secrete)
        for i, mot in enumerate(text):
            if mot.isalpha():
                depart_alpha = ord('a') if mot.islower() else ord('A')
                key_char = self.cle_secrete[i % long_cle]
                decalage = ord(key_char.lower()) - ord('a')
                cryptage_text += chr((ord(mot) - depart_alpha + decalage) % 26 +depart_alpha)
            else:
                cryptage_text += mot
        return cryptage_text

    
    def decryptage(self, cryptage_text):
        texte_decrypte = ""
        long_cle = len(self.cle_secrete)
        for i, char in enumerate(cryptage_text):
            if char.isalpha():
                depart = ord('a') if char.islower() else ord('A')
                char_cle = self.cle_secrete[i % long_cle]
                decalage_cle = ord(char_cle.lower()) - ord('a')
                texte_decrypte += chr((ord(char) - depart - decalage_cle) % 26 + depart)
            else:
                texte_decrypte += char
        return texte_decrypte

    
    