# Teleport Clicker

A Python terminal tool that lets you save screen positions and assign a key to each one. Press the key to instantly teleport the cursor and click. Supports a "press-and-go" mode to automatically return to the previous position after clicking.

## Requirements

Install dependencies with:

pip install pyautogui keyboard colorama

## How to use

1. Run the script
2. Choose a key to save positions
3. Move the cursor and press the key to save a position, Z to undo, ESC to confirm
4. Assign a keyboard shortcut to each saved position
5. Optionally enable "press-and-go" on any position
6. Press ESC at any time to stop

## Notes

- Tested on Windows
- Run as administrator if the script doesn't detect keypresses correctly
