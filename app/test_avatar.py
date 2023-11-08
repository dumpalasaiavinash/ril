import cv2
import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

# Load mouth shape images
mouth_shapes = {
    'phoneme1': pygame.image.load('open.png'),
    'phoneme2': pygame.image.load('close.png'),
    # Add more phoneme images as needed
}

# Recognized phonemes (example, replace with actual recognized phonemes)
recognized_phonemes = ['phoneme1', 'phoneme2', 'phoneme1']

# Main loop
running = True
index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill((255, 255, 255))

    # Display the current mouth shape
    current_phoneme = recognized_phonemes[index]
    window.blit(mouth_shapes[current_phoneme], (window_width // 2, window_height // 2))

    # Update the display
    pygame.display.flip()

    # Delay between frames (adjust as needed)
    pygame.time.delay(500)

    # Move to the next phoneme
    index = (index + 1) % len(recognized_phonemes)

# Clean up
pygame.quit()
cv2.destroyAllWindows()
