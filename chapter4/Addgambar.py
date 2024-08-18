import pygame
pygame.init()

# Memuat gambar
image = pygame.image.load('../chapter3/merah.jpg')
# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Loop utama permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Menggambar gambar
    screen.blit(image, (100, 100))
    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()