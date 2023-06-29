import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Caminho do arquivo MP3
mp3_file = "caminho/do/seu/arquivo.mp3"

# Chamando a função para reproduzir o MP3
play_mp3(mp3_file)
