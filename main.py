from Screen.start_screen import StartScreen
from Screen.main_screen import MainScreen

WIDTH = 800
HEIGHT = 800
APP_NAME = "Chroniq"

if __name__ == "__main__":
    # start_screen = StartScreen(WIDTH, HEIGHT, APP_NAME)
    # start_screen.create_screen()

    main_screen = MainScreen(WIDTH, HEIGHT, APP_NAME)
    main_screen.create_screen()