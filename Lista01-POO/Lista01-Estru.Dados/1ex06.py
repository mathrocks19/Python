class Televisao:
    def __init__(self):
        while True:
            self.canal = int(input("Insira o canal da sua TV (0 a 99): "))
            if self.canal in range(0, 101):
                print("Canal:", self.canal)
                break
            else:
                print("Esse canal não existe.")
        self.volume = 50
        print(" Seu Volume é:", self.volume)

    def aumentar_volume(self):
        if self.volume >= 101:
            print(" Volume máximo da Sua TV.")
        else:
            self.volume += 1
            print("Seu Volume é:", self.volume)

    def diminuir_volume(self):
        if self.volume == 0:
            print("Canal da TV está Mudo.")
        else:
            self.volume -= 1
            print(" Seu Volume é:", self.volume)


tv = Televisao()
for y in range(0, 51):  
    tv.aumentar_volume()
for y in range(0, 101):  
    tv.diminuir_volume()