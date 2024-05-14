# nefunguje - dle MJ Slack

class User:
    jmeno = ""
    prijmeni = ""
    vek = 0

    def zkontroluj_vek(self):
        if self.vek > 65:
            print("Jsi duchodce.")
        else:
            print("Nejsi duchodce.")

    def __str__(self):
        print(f"{self.jmeno}, {self.prijmeni}, {self.vek}")


if __name__ == "__main__":
    user1 = User()
    user1.jmeno = "Pepa"
    user1.prijmeni = "Novak"
    user1.vek = 70
    # print(user1)
    user1.zkontroluj_vek()





