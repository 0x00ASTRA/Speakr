from src.gui.controller import Controller
from src.gui.view import View
from src.gui.model import Model


def main():
    view = View()
    model = Model()
    controller = Controller(view=view, model=model)
    view.controller = controller
    view.update_ui()
    controller.run()

if __name__ == "__main__":
    main()