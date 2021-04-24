import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx
from math import sin, cos, sqrt
from PIL import Image



class Window:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.window = sdl2.ext.Window(self.name, size=self.size)

    def fill_Window(self, color):
        r, g, b = color
        COLOR = sdl2.ext.Color(r, g, b)
        sdl2.ext.fill(self.window.get_surface(), COLOR)

    def d1_point(self, x, y, surface, color):
        r, g, b = color
        WHITE = sdl2.ext.Color(r, g, b)
        pixelview = sdl2.ext.PixelView(surface)
        pixelview[y][x] = WHITE

    def line_vert(self, x, y, l, color=(0, 0, 0)):
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        if l < 0:
            for i in range(l * -1):
                Window.d1_point(self, x - 1, y - 1, self.window.get_surface(), color)
                y = y - 1
        else:
            for i in range(l):
                Window.d1_point(self, x, y + 1, self.window.get_surface(), color)
                y = y + 1

    def line_goriz(self, x, y, l, color=(0, 0, 0)):
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        if l < 0:
            for i in range(l * -1):
                Window.d1_point(self, x-1, y, self.window.get_surface(), color)
                x = x - 1
        else:
            for i in range(l):
                Window.d1_point(self, x, y, self.window.get_surface(), color)
                x = x + 1

    def rectangle(self,  x, y, w, h, color=(0, 0, 0)):
        xyw = [x + w, y]
        xyh = [x, y + h]
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        Window.line_goriz(self, x, y, w, color)
        Window.line_vert(self, x, y, h, color)
        Window.line_goriz(self, xyh[0], xyh[1], w, color)
        Window.line_vert(self, xyw[0], xyw[1], h, color)


    def rectangle1(self,  x, y, w, h, color=(0, 0, 0)):
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        for i in range(x, x + w + 1):
            for j in range(y, y + h + 1):
                Window.d1_point(self, i, j, self.window.get_surface(), color)


    def drawDDA(self, x1, y1, x2, y2, color=(0, 0, 0)):
        x, y = x1, y1
        length = abs((x2 - x1) if abs(x2 - x1) > abs(y2 - y1) else (y2 - y1))
        dx = (x2 - x1) / float(length)
        dy = (y2 - y1) / float(length)
        Window.d1_point(self, round(x), round(y), self.window.get_surface(), color)
        for i in range(int(length)):
            x += dx
            y += dy
            Window.d1_point(self, round(x), round(y), self.window.get_surface(), color)
            
    def draw_bomb(self, x, y, color1, color2):
        Window.rectangle1(self, x, y, 7, 7, color1)
        Window.rectangle1(self, x + 7, y + 7, 35, 35, color1)
        Window.rectangle1(self, x + 21, y, 7, 7, color1)
        Window.rectangle1(self, x + 21, y - 7, 7, 7, color1)
        Window.rectangle1(self, x + 21 + 21, y, 7, 7, color1)
        Window.rectangle1(self, x, y + 21, 7, 7, color1)
        Window.rectangle1(self, x- 7, y + 21, 7, 7, color1)
        Window.rectangle1(self, x, y + 42, 7, 7, color1)
        Window.rectangle1(self, x, y + 42, 7, 7, color1)

        Window.rectangle1(self, x + 21, y + 42, 7, 7, color1)
        Window.rectangle1(self, x +21, y + 42, 7, 7, color1)
        Window.rectangle1(self, x + 21, y + 49, 7, 7, color1)

        Window.rectangle1(self, x + 42, y + 42, 7, 7, color1)
        Window.rectangle1(self, x + 42, y + 21, 7, 7, color1)
        Window.rectangle1(self, x + 49, y + 21, 7, 7, color1)
        
        Window.rectangle1(self, x + 25, y + 15, 5, 5, color2)
        Window.rectangle1(self, x + 30, y + 15, 5, 5, color2)
        Window.rectangle1(self, x + 30, y + 20, 5, 5, color2)

    def run(self):
        sdl2.ext.init()
        # window = sdl2.ext.Window(self.name, size=self.size)
        self.window.show()
        running = True
        Window.fill_Window(self, (43, 122, 168))
        #Window.draw_menu(self)
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                elif event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_SPACE:
                        x, y = 0, 700
                        Window.rectangle1(self, 0, 700, 20, 20)
                    elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                        try:
                            Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                            Window.rectangle1(self, x + 10, y, 20, 20)
                            x = x + 10
                        except:
                            Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                            Window.rectangle1(self, x, y, 20, 20)
                    elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                        try:
                            Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                            Window.rectangle1(self, x - 10, y, 20, 20)
                            x = x - 10
                        except:
                            Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                            Window.rectangle1(self, x, y, 20, 20)
                    elif event.key.keysym.sym == sdl2.SDLK_UP:
                        try:
                            Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                            Window.rectangle1(self, x, y - 10, 20, 20)
                            y = y - 10
                        except:
                            Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                            Window.rectangle1(self, x, y, 20, 20)
                    elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                        try:
                            Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                            Window.rectangle1(self, x, y + 10, 20, 20)
                            y = y + 10
                        except:
                            Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                            Window.rectangle1(self, x, y, 20, 20)
                    elif event.key.keysym.sym == sdl2.SDLK_r:
                        Window.fill_Window(self, (100, 90, 7))
                        x, y = 0, 700
                        #try:
                        #    Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                        #    Window.rectangle1(self, x, y + 10, 20, 20)
                        #    y = y + 10
                        #except:
                        #    Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                        #    Window.rectangle1(self, x, y, 20, 20)
                        #for i in range(10, 100):
                        #    for j in range(10, 20):
                        #        Window.d1_point(self, i, j, self.window.get_surface(), (100, 100, 100))
                        # Window.d1_point(self, 11, 20, self.window.get_surface(), (0, 0, 0))
                        # Window.d1_point(self, 12, 20, self.window.get_surface(), (0, 0, 0))
                        # Window.d1_point(self, 13, 20, self.window.get_surface(), (0, 0, 0))
                        # Window.d1_point(self, 14, 20, self.window.get_surface(), (0, 0, 0))
                elif event.type == sdl2.SDL_CONTROLLER_BUTTON_X:
                    Window.d_point(self, 10, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 11, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 12, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 13, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 14, 20, self.window.get_surface(), (0, 0, 0))
                    # Window.d_point(self, 10, 20, (0, 0, 0))
                    # Window.d_point(self, 11, 20, (0, 0, 0))
                    # Window.d_point(self, 12, 20, (0, 0, 0))
                    # Window.d_point(self, 13, 20, (0, 0, 0))
                    # Window.d_point(self, 14, 20, (0, 0, 0))
                    # Window.d_point(self, 15, 20, (0, 0, 0))
            self.window.refresh()
        return 0


def main():
    window = Window((1081, 721), "XXI")

    window.run()
    # window.fill_Window((240, 0, 0))
    # fill_Window(window, 240, 0, 0)


if __name__ == "__main__":
    # window = Window((1080, 720), (240, 40, 40), "No Best Game")
    sys.exit(main())
