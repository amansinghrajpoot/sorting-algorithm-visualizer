import random
import sys
import pygame

WIDTH = 1000
HEIGHT = 500
RATIO = 2


def generate_data() -> list:
    data = []
    for i in range(0, 500):
        d = random.randint(1, 500)
        data.append(d)
    return data


class visualize:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.fps = pygame.time.Clock()
        self.line_color = "#89A4C3"
        self.swap_color = "#2F3B30"
        self.screen_color = "#CAC2DD"

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.WINDOWMAXIMIZED:
                self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            if event.type == pygame.WINDOWMINIMIZED:
                pass

    def reset_display(self, data: list):
        for i in range(0, int(WIDTH/RATIO)):
            pygame.draw.line(self.screen, self.line_color, [i * RATIO, HEIGHT], [i * RATIO, data[i]], RATIO)
        pygame.display.update()

    def run(self, sorting_map: dict):

        self.screen.fill(self.screen_color)

        pygame.display.update()

        for keys in sorting_map:
            self.screen.fill(self.screen_color)
            pygame.display.set_caption(keys)
            data = generate_data()
            self.reset_display(data)
            sort_algo = sorting_map.get(keys)
            sort_algo.algorithm(data, self)
            pygame.time.wait(5)

        while True:
            pygame.display.update()
            self.check_event()

    def update_display(self, data, i, j, w):
        self.check_event()
        pygame.draw.line(self.screen, self.swap_color, [i * RATIO, HEIGHT], [i * RATIO, data[i]], RATIO)
        pygame.draw.line(self.screen, self.swap_color, [j * RATIO, HEIGHT], [j * RATIO, data[j]], RATIO)
        pygame.display.update()
        pygame.time.wait(w)

        pygame.draw.line(self.screen, self.screen_color, [i * RATIO, HEIGHT], [i * RATIO, data[i]], RATIO)
        pygame.draw.line(self.screen, self.screen_color, [j * RATIO, HEIGHT], [j * RATIO, data[j]], RATIO)
        pygame.display.update()
        pygame.time.wait(w)

    def swap_display(self, data, i, j, w):
        self.check_event()
        pygame.draw.line(self.screen, self.swap_color, [i * RATIO, HEIGHT], [i * RATIO, data[i]], RATIO)
        pygame.draw.line(self.screen, self.swap_color, [j * RATIO, HEIGHT], [j * RATIO, data[j]], RATIO)
        pygame.display.update()
        pygame.time.wait(w)

        pygame.draw.line(self.screen, self.line_color, [i * RATIO, HEIGHT], [i * RATIO, data[i]], RATIO)
        pygame.draw.line(self.screen, self.line_color, [j * RATIO, HEIGHT], [j * RATIO, data[j]], RATIO)
        pygame.display.update()
        pygame.time.wait(w)
