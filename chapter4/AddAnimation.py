import pygame
pygame.init()

# Memuat gambar
image = pygame.image.load('../chapter3/merah.jpg')
# Memuat suara
sound = pygame.mixer.Sound('../result.wav')
# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Loop utama permainan
x=0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Memutar suara
    sound.play()
    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))
    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()