class DecryptageTexte:
    def __init__(self, cle):
        self.cle_secrete = cle

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

   