import pygame

class Alarm:
    def __init__(self, sound_path):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(sound_path)

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()

    def set_volume(self, volume):
        self.sound.set_volume(volume)