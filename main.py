import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx
from math import sin, cos, sqrt
from PIL import Image


def draw_menu(path):
    image = Image.open(path)
    size = image.size
    pix = image.load()
    sp = []
    for i in range(size[0]):
        for j in range(size[1]):
            sp.append([[i, j], pix[i, j]])
    return sp


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

    def draw_menu(self):
        matrix = draw_menu('Menu.png')
        for i in matrix:
            Window.d1_point(self, i[0][0], i[0][1], self.window.get_surface(), i[1][:-1])

    def d_point(self, x, y, color):
        r, g, b = color
        renderer = sdl2.ext.Renderer(self.window)
        renderer.draw_point([x, y], sdl2.ext.Color(r, g, b))
        renderer.present()
        processor = sdl2.ext.TestEventProcessor()
        processor.run(self.window)

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

    def hexagon(self, x, y, length, new_image, color=(0, 0, 0)):
        bside = round(length * sin(60 / 180 * 3.14))
        cside = round(length * sin(30 / 180 * 3.14))
        drawDDA(self, x, y, x + length, y, color)
        drawDDA(self, x, y - bside * 2, x + length, y - bside * 2, color)
        y1, x1 = y - bside, x - cside
        y2, x2 = y - bside, x + length + cside
        drawDDA(self, x, y, x1, y1, color)
        drawDDA(self, x1, y1, x, y - bside * 2, color)
        drawDDA(self, x + length, y, x2, y2, color)
        drawDDA(self, x + length, y - bside * 2, x2, y2, color)
        Window.d1_point(self, x2, y2, self.window.get_surface(), color)

    def pentagon(self, x, y, length, new_image, color=(0, 0, 0)):
        draw = ImageDraw.Draw(new_image)
        bside = round(length * sin(54 / 180 * 3.14)) * 2
        cside = round(length * sin(36 / 180 * 3.14))
        heigth1 = round(sqrt(pow(bside, 2) - pow(length / 2, 2)))
        drawDDA(self, x, y, x + length, y, color)
        y1, x1 = y - heigth1 + cside, x + length / 2 - bside / 2
        y2, x2 = y1, x + length / 2 + bside / 2
        drawDDA(self, x + length / 2, y - heigth1, x1, y1, color)
        drawDDA(self, x + length / 2, y - heigth1, x2, y2, color)
        drawDDA(self, x1, y1, x, y, color)
        drawDDA(self, x2, y2, x + length, y, color)



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
    window = Window((1081, 721), "No Best Game")

    window.run()
    # window.fill_Window((240, 0, 0))
    # fill_Window(window, 240, 0, 0)


if __name__ == "__main__":
    # window = Window((1080, 720), (240, 40, 40), "No Best Game")
    sys.exit(main())