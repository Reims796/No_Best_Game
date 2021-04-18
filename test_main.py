import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx
from math import sin, cos, sqrt
from PIL import Image


class Window:
    def __init__(self, size, name, pos_b):
        self.size = size
        self.name = name
        self.window = sdl2.ext.Window(self.name, size=self.size)
        self.pos_b = pos_b

    def fill_Window(self, color):
        r, g, b = color
        COLOR = sdl2.ext.Color(r, g, b)
        sdl2.ext.fill(self.window.get_surface(), COLOR)

    def d1_point(self, x, y, surface, color):
        r, g, b = color
        WHITE = sdl2.ext.Color(r, g, b)
        pixelview = sdl2.ext.PixelView(surface)
        pixelview[y][x] = WHITE

    def rectangle(self, x, y, w, h, color):
        for i in range(x, x + w):
            for j in range(y, y + h):
                Window.d1_point(self, i, j, self.window.get_surface(), color)

    def draw_bomb(self, x, y, color1, color2):
        Window.rectangle(self, x, y, 7, 7, color1)
        Window.rectangle(self, x + 7, y + 7, 35, 35, color1)
        Window.rectangle(self, x + 21, y, 7, 7, color1)
        Window.rectangle(self, x + 21, y - 7, 7, 7, color1)
        Window.rectangle(self, x + 21 + 21, y, 7, 7, color1)
        Window.rectangle(self, x, y + 21, 7, 7, color1)
        Window.rectangle(self, x - 7, y + 21, 7, 7, color1)
        Window.rectangle(self, x, y + 42, 7, 7, color1)
        Window.rectangle(self, x, y + 42, 7, 7, color1)

        Window.rectangle(self, x + 21, y + 42, 7, 7, color1)
        Window.rectangle(self, x + 21, y + 42, 7, 7, color1)
        Window.rectangle(self, x + 21, y + 49, 7, 7, color1)

        Window.rectangle(self, x + 42, y + 42, 7, 7, color1)
        Window.rectangle(self, x + 42, y + 21, 7, 7, color1)
        Window.rectangle(self, x + 49, y + 21, 7, 7, color1)

        Window.rectangle(self, x + 25, y + 15, 5, 5, color2)
        Window.rectangle(self, x + 30, y + 15, 5, 5, color2)
        Window.rectangle(self, x + 30, y + 20, 5, 5, color2)
 # sp = [(0, 0, 0), (255, 255, 255), (245, 3, 18), (150, 0, 18), (99, 2, 17), (8, 198, 245), (245, 129, 5)]
    def boat_contour(self, x, y, sp):
        Window.rectangle(self, x, y, 8, 8, sp[0])
        Window.rectangle(self, x - 8, y + 8, 8, 16, sp[0])
        Window.rectangle(self, x + 8, y + 8, 8, 16, sp[0])
        Window.rectangle(self, x - 16, y + 24, 8, 8, sp[0])
        Window.rectangle(self, x + 16, y + 24, 8, 8, sp[0])
        Window.rectangle(self, x - 24, y + 32, 8, 8, sp[0])
        Window.rectangle(self, x + 24, y + 32, 8, 8, sp[0])
        Window.rectangle(self, x - 32, y + 40, 8, 16, sp[0])
        Window.rectangle(self, x + 32, y + 40, 8, 16, sp[0])
        Window.rectangle(self, x - 40, y + 56, 8, 104, sp[0])
        Window.rectangle(self, x + 40, y + 56, 8, 104, sp[0])
        Window.rectangle(self, x - 40, y + 160, 88, 8, sp[0])
        Window.rectangle(self, x - 8, y + 32, 24, 24, sp[0])
        Window.rectangle(self, x - 8, y + 64, 24, 8, sp[0])
        Window.rectangle(self, x - 24, y + 72, 56, 80, sp[0])

        Window.rectangle(self, x, y + 40, 8, 8, sp[1])
        Window.rectangle(self, x, y + 72, 8, 8, sp[1])
        Window.rectangle(self, x - 8, y + 80, 8, 8, sp[1])

    def boat_red(self, x, y, sp):
        Window.rectangle(self, x - 8, y + 24, 8, 8, sp[2])
        Window.rectangle(self, x - 16, y + 32, 8, 40, sp[2])
        Window.rectangle(self, x - 24, y + 40, 8, 32, sp[2])
        Window.rectangle(self, x - 32, y + 56, 8, 8 * 13, sp[2])
        Window.rectangle(self, x - 32, y + 152, 24, 8, sp[2])

        Window.rectangle(self, x, y + 8, 8, 24, sp[3])
        Window.rectangle(self, x + 8, y + 24, 8, 8, sp[3])
        Window.rectangle(self, x - 8, y + 56, 24, 8,sp[3])
        Window.rectangle(self, x + 16, y + 32, 8, 40, sp[3])
        Window.rectangle(self, x + 24, y + 40, 8, 32, sp[3])
        Window.rectangle(self, x + 32, y + 56, 8, 16, sp[3])
        Window.rectangle(self, x - 8, y + 152, 40, 8, sp[3])

        Window.rectangle(self, x + 32, y + 72, 8, 88, sp[4])

    def boat_color(self, x, y, sp):
        Window.rectangle(self, x - 8, y + 72, 8, 8, sp[5])
        Window.rectangle(self, x + 8, y + 72, 8, 24, sp[5])
        Window.rectangle(self, x - 16, y + 80, 8, 24, sp[5])
        Window.rectangle(self, x, y + 80, 8, 16, sp[5])
        Window.rectangle(self, x + 16, y + 80, 8, 24, sp[5])
        Window.rectangle(self, x - 8, y + 88, 8, 8, sp[5])

        Window.rectangle(self, x - 8, y + 96, 24, 8, sp[-1])
        Window.rectangle(self, x, y + 104, 8, 16, sp[-1])
        Window.rectangle(self, x - 16, y + 104, 8, 16, sp[-1])
        Window.rectangle(self, x + 16, y + 104, 8, 16, sp[-1])

        Window.rectangle(self, x, y + 128, 8, 16, sp[-1])
        Window.rectangle(self, x - 16, y + 128, 8, 16, sp[-1])
        Window.rectangle(self, x + 16, y + 128, 8, 16, sp[-1])


    def draw_boat(self, x, y, sp):
        Window.boat_contour(self, x, y, sp)
        Window.boat_red(self, x, y, sp)
        Window.boat_color(self, x, y, sp)



    def run(self):
        sdl2.ext.init()
        # window = sdl2.ext.Window(self.name, size=self.size)
        self.window.show()
        running = True
        Window.fill_Window(self, (43, 122, 168))
        # Window.draw_menu(self)
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                elif event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_SPACE:
                        Window.draw_bomb(self, 100, 100, (166, 166, 166), (255, 255, 255))
                        Window.draw_boat(self, self.pos_b[0], self.pos_b[1], [(0, 0, 0), (255, 255, 255), (245, 3, 18), (150, 0, 18), (99, 2, 17), (8, 198, 245), (245, 129, 5)])
                    elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                        Window.draw_boat(self, self.pos_b[0], self.pos_b[1], [(43, 122, 168) for _ in range(8)])
                        self.pos_b = [self.pos_b[0] - 50, self.pos_b[1]]
                        Window.draw_boat(self, self.pos_b[0], self.pos_b[1], [(0, 0, 0), (255, 255, 255), (245, 3, 18), (150, 0, 18), (99, 2, 17), (8, 198, 245), (245, 129, 5)])
            self.window.refresh()
        return 0


def main():
    window = Window((1081, 721), "No Best Game", [540, 500])

    window.run()
    # window.fill_Window((240, 0, 0))
    # fill_Window(window, 240, 0, 0)


if __name__ == "__main__":
    # window = Window((1080, 720), (240, 40, 40), "No Best Game")
    sys.exit(main())
