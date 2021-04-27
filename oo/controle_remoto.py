
'''
Exemplo:
    >>> # Testando canal
    >>> canal = Canal()
    >>> canal.mostrar_canal
    1
    >>> canal.aumentar_canal()
    >>> canal.mostrar_canal
    2
    >>> canal.aumentar_canal()
    >>> canal.mostrar_canal
    3
    >>> canal.aumentar_canal()
    >>> canal.mostrar_canal
    4
    >>> canal.diminuir_canal()
    >>> canal.mostrar_canal
    3
    >>> canal.diminuir_canal()
    >>> canal.mostrar_canal
    2
    >>> canal.diminuir_canal()
    >>> canal.mostrar_canal
    1
    >>> canal.diminuir_canal()
    >>> canal.mostrar_canal
    1
    >>> # Testando volume
    >>> volume = Volume()
    >>> volume.mostrar_volume
    0
    >>> volume.aumentar_volume()
    >>> volume.mostrar_volume
    1
    >>> volume.aumentar_volume()
    >>> volume.mostrar_volume
    2
    >>> volume.aumentar_volume()
    >>> volume.mostrar_volume
    3
    >>> volume.aumentar_volume()
    >>> volume.mostrar_volume
    4
    >>> volume.diminuir_volume()
    >>> volume.mostrar_volume
    3
    >>> volume.diminuir_volume()
    >>> volume.mostrar_volume
    2
    >>> volume.aumentar_volume()
    >>> volume.mostrar_volume
    3
    >>> volume.mudo()
    >>> volume.mostrar_volume
    0
    >>> controle = Controle(volume, canal)
    >>> controle.mostrar_canal()
    1
    >>> controle.aumentar_canal()
    >>> controle.mostrar_canal()
    2
    >>> controle.aumentar_canal()
    >>> controle.mostrar_canal()
    3
    >>> controle.diminuir_canal()
    >>> controle.mostrar_canal()
    2
    >>> controle.aumentar_volume()
    >>> controle.mostrar_volume()
    1
    >>> controle.aumentar_volume()
    >>> controle.mostrar_volume()
    2
    >>> controle.diminuir_volume()
    >>> controle.mostrar_volume()
    1
    >>> controle.mudo()
    >>> controle.mostrar_volume()
    0

'''


class Canal:

    def __init__(self, mostrar_canal=1):
        self.mostrar_canal = mostrar_canal

    def aumentar_canal(self):
        self.mostrar_canal += 1

    def diminuir_canal(self):
        self.mostrar_canal -= 1
        if self.mostrar_canal < 1:
            self.mostrar_canal = 1

class Volume:

    def __init__(self, mostrar_volume=0):
        self.mostrar_volume = mostrar_volume

    def aumentar_volume(self):
        self.mostrar_volume += 1

    def diminuir_volume(self):
        self.mostrar_volume -= 1
        if self.mostrar_volume < 0:
            self.mostrar_volume = 0

    def mudo(self):
        self.mostrar_volume = 0

class Controle:

    def __init__(self, volume, canal):
        self.canal = canal
        self.volume = volume

    def mostrar_canal(self):
        return self.canal.mostrar_canal

    def aumentar_canal(self):
        self.canal.aumentar_canal()

    def diminuir_canal(self):
        self.canal.diminuir_canal()

    def mostrar_volume(self):
        return self.volume.mostrar_volume

    def aumentar_volume(self):
        self.volume.aumentar_volume()

    def diminuir_volume(self):
        self.volume.diminuir_volume()

    def mudo(self):
        self.volume.mudo()
