import pygame
from phonemizer import phonemize

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

# Load mouth shape images (replace these paths with your actual file paths)
mouth_shapes = {
    'phoneme1': pygame.image.load('open.png'),
    'phoneme2': pygame.image.load('close.png'),
    # Add more phoneme images as needed
}

# Text to be spoken
raw_text = "Hello, how are you today?"

# Convert text to phonemes
recognized_phonemes = phonemize(raw_text, language="en-us", backend="espeak")

# Split phonemes into individual phonemes
recognized_phonemes = recognized_phonemes.strip().split()
print(recognized_phonemes)

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
    window.blit(mouth_shapes.get(current_phoneme, mouth_shapes['default']), (window_width // 2, window_height // 2))

    # Update the display
    pygame.display.flip()

    # Delay between frames (adjust as needed)
    pygame.time.delay(500)

    # Move to the next phoneme
    index = (index + 1) % len(recognized_phonemes)

# Clean up
pygame.quit()




# from phonemizer import phonemize
# import pygame

# # Initialize Pygame
# pygame.init()

# # Set the window dimensions
# window_width, window_height = 800, 600
# window = pygame.display.set_mode((window_width, window_height))

# # Load mouth shape images (assuming you have loaded them into mouth_shapes dictionary)

# # Text to be spoken
# raw_text = "Hello, how are you today?"

# # Convert text to phonemes
# recognized_phonemes = phonemize(raw_text, language="en-us", backend="espeak")

# # Split phonemes into individual phonemes
# recognized_phonemes = recognized_phonemes.strip().split()
# print(recognized_phonemes)
# # Main loop (similar to the previous code snippet)
# running = True
# index = 0

# while running:
#     # Handle events and display mouth shapes (similar to the previous code snippet)
#     # ...
#     # Move to the next phoneme
#     index = (index + 1) % len(recognized_phonemes)
