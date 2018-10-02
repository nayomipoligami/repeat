def kanal_değiştir(self):
    while True:

        işlem = input("İlerlemek İçin:+\nGerilemek İçin:-\nÇıkmak İçin:X")
        if işlem == "+":
            if self.kanal != self.kanal_listesi[len(self.kanal_listesi) - 1]:
                self.kanal = self.kanal_listesi[self.kanal_listesi.index(self.kanal) + 1]
                print("Kanal:", self.kanal)
        elif işlem == "-":
            if self.kanal_listesi.index(self.kanal) != 0:
                self.kanal = self.kanal_listesi[self.kanal_listesi.index(self.kanal) - 1]
                print("Kanal:", self.kanal)