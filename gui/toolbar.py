def _create_toolbar(self):
    toolbar = self.addToolBar("Haupt")

    toolbar.addAction("Neu CSR")
    toolbar.addAction("Self-Signed")
    toolbar.addSeparator()
    toolbar.addAction("Öffnen")
    toolbar.addAction("Speichern")