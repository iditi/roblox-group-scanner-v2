from scanner.controllers import Controller
from scanner.arguments import get_arguments
import multiprocessing

if __name__ == "__main__":
    multiprocessing.freeze_support()
    arguments = get_arguments()
    controller = Controller(
        arguments=arguments
    )
    print("All workers are running!")