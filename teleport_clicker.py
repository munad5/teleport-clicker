import pyautogui as tp
import keyboard as kb
import time 
from colorama import Fore as color


def typing_text(text, speed):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

def print_points(arr=[]):
    for i in range(len(arr)):
        print(f"{i + 1}: {arr[i]}")

def print_assignments(positions=[], assignments=[]):
    for i in range(len(positions)):
        print(f"{i + 1}: {positions[i]} = {assignments[i]}")

def error_msg(message):
    typing_text(color.RED + f"\nWARNING! {message}" + color.WHITE, 0.02)


points = []
num_points = 0
press_and_go = True
press_and_go_arr = []

print(color.CYAN + "╔═══════════════════════════════════════════════════════════════╗")
print(color.CYAN + "║          TELEPORT CLICKER - Quick Setup                       ║")
print(color.CYAN + "╠═══════════════════════════════════════════════════════════════╣")
print(color.CYAN + "║ • Save multiple positions on screen                           ║")
print(color.CYAN + "║ • Assign a key to each position                               ║")
print(color.CYAN + "║ • Press the key to teleport and click                         ║")
print(color.CYAN + "╚═══════════════════════════════════════════════════════════════╝" + color.WHITE)
print("\nSelect the key to save positions (cannot be ESC or Z)\n")


time.sleep(0.2)
while True:

    key = kb.read_key()
    time.sleep(0.2)

    if key == "esc":
        typing_text(color.RED + "\n\nESC is not a valid key, please try another one" + color.WHITE, 0.04)
    
    elif key == "z":
        typing_text(color.RED + "\n\nZ is not a valid key, please try another one" + color.WHITE, 0.04)

    else:
        break


print(f"\n\nPerfect! Move your cursor on screen and press {key} to save a position.\nPress ESC to confirm, Z to undo the last point.\n")


while True:

    if kb.is_pressed(key) and tp.position() in points:
        typing_text(color.RED + "\n\nThis point has already been saved.\n\n" + color.WHITE, 0.04)

    if kb.is_pressed(key):
        points.append(tp.position())
        time.sleep(0.3)
        num_points += 1
        print_points(points)
        print("\n\n\n")

    elif kb.is_pressed("z") and num_points > 0:
        points.pop()
        num_points -= 1
        time.sleep(0.1)
        print_points(points)
        print("\n\n\n")

    elif kb.is_pressed("esc") and num_points > 0:
        break

    elif kb.is_pressed("esc") or kb.is_pressed("z") and num_points <= 0:
        print("Please insert at least one point.")
        time.sleep(0.2)


print("\n\nAll saved points:\n")
print_points(points)

print("\nAssign keys to each point: enter the number, then press the key.\n")

assigned_keys = [None] * len(points)
press_and_go_arr = [False] * len(points)

i = 0

while i < num_points:

    try:
        kb.press("backspace")
        choice = int(input("\n>"))

        if choice <= 0:
            error_msg("The value is too small, please enter a valid point number.\n\n")

        elif assigned_keys[choice - 1] is None:
            time.sleep(0.1)
            assigned_keys[choice - 1] = kb.read_key()
            i += 1

        else:
            error_msg(f"This will overwrite key {assigned_keys[choice - 1]}.\n")
            time.sleep(0.5)
            assigned_keys[choice - 1] = kb.read_key()

    except ValueError:
        error_msg("Invalid input, please enter a number.\n\n")

    except IndexError:
        error_msg("The value is too large, please enter a valid point number.\n\n")

    print_assignments(assigned_keys, points)

kb.press("backspace")

choice = input("\nDo you want any key to click a point and then return to the previous position? (y/n)\nType 'all' to enable this for all points.\n\n>")
flag_for_click_text = False

while True:

    if flag_for_click_text is False:
        flag_for_click_text = True

    else:
        choice = input("Do you want to add another key? (y/n)\nType 'all' to enable for all remaining points.\n\n>")

    if choice == "y":

        press_and_go = True
        print_assignments(press_and_go_arr, points)

        try:
            choice = int(input("\n>"))

            if choice <= 0:
                error_msg("The value is too small, please enter a valid point number.\n\n")

            else:
                if press_and_go_arr[choice - 1] is True:
                    print(f"Point {choice}: {points[choice - 1]} will be removed from press-and-go.\n")
                    press_and_go_arr[choice - 1] = False
                else:
                    press_and_go_arr[choice - 1] = True

        except ValueError:
            error_msg("Invalid input, please enter a number.\n\n")

        except IndexError:
            error_msg("The value is too large, please enter a valid point number.\n\n")

    elif choice == "n":
        break

    elif choice == "all":
        press_and_go_arr = [True] * len(points)

kb.press("backspace")


while True:

    choice_3 = input("\nAre these the final settings? (y/n)\n")
    print_assignments(assigned_keys, points)

    if choice_3 == "n":

        try:
            choice = int(input("\n>"))

            if choice <= 0:
                error_msg("The value is too small, please enter a valid point number.\n\n")

            else:
                print(color.RED + f"\nThis will overwrite key {assigned_keys[choice - 1]}.\n" + color.WHITE)
                time.sleep(0.5)
                assigned_keys[choice - 1] = kb.read_key()

        except ValueError:
            error_msg("Invalid input, please enter a number.\n\n")

        except IndexError:
            error_msg("The value is too large, please enter a valid point number.\n\n")

    elif choice_3 == "y":

        if press_and_go is False:
            while True:

                if kb.is_pressed("esc"):
                    break

                else:
                    for i, assigned_key in enumerate(assigned_keys):
                        if assigned_key and kb.is_pressed(assigned_key):
                            x, y = points[i]
                            time.sleep(0.05)
                            tp.click(x, y)

                            while kb.is_pressed(assigned_key):
                                time.sleep(0.01)

                        time.sleep(0.01)

        else:
            while True:

                if kb.is_pressed("esc"):
                    break

                else:
                    for i, assigned_key in enumerate(assigned_keys):
                        if assigned_key and kb.is_pressed(assigned_key):
                            x1, y1 = tp.position()
                            x, y = points[i]
                            time.sleep(0.01)
                            tp.click(x, y)

                            if press_and_go_arr[i] is True:
                                time.sleep(0.01)
                                tp.moveTo(x1, y1)

                            while kb.is_pressed(assigned_key):
                                time.sleep(0.01)

                        time.sleep(0.01)
