from Screen.start_screen import StartScreen

WIDTH = 10024
HEIGHT = 1024
APP_NAME = "Chroniq"

if __name__ == "__main__":
    start_screen = StartScreen(WIDTH, HEIGHT, APP_NAME)
    start_screen.create_screen()