import pygame as py


# boucle de la partie
def main(window):
    run = True
    while run:
        for event in py.event.get():
            if event.type == py.QUIT:
                print("Quit")
                run = False
