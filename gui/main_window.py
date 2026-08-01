from PyQt6.QtWidgets import QMainWindow, QStackedWidget

from gui.pages.home_page import HomePage
#from gui.pages.certificate_page import CertificatePage
#from gui.pages.csr_page import CsrPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()

        self.home_page = HomePage()
        self.certificate_page = CertificatePage()
        self.csr_page = CsrPage()

        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.certificate_page)
        self.stack.addWidget(self.csr_page)

        self.setCentralWidget(self.stack)

        self.home_page.create_certificate_requested.connect(
            self.show_certificate_page
        )

        self.home_page.create_csr_requested.connect(
            self.show_csr_page
        )

    def show_certificate_page(self):
        self.stack.setCurrentWidget(self.certificate_page)

    def show_csr_page(self):
        self.stack.setCurrentWidget(self.csr_page)