import sys
import pygame as pg
import window_class


def main():
    window = window_class.Window((1080, 720), "No Best Game", [540, 490])
    pg.init()
    pg.mixer.music.load('music.mp3')
    pg.mixer.music.play()
    window.run()


if __name__ == "__main__":

    sys.exit(main())
