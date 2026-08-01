def _create_menu(self):
    menu = self.menuBar()

    file_menu = menu.addMenu("Datei")
    file_menu.addAction("Neu")
    file_menu.addAction("Öffnen")
    file_menu.addAction("Speichern")

    tools_menu = menu.addMenu("Extras")
    help_menu = menu.addMenu("Hilfe")