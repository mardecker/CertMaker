from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QScrollArea

from gui.pages.home_page import HomePage
from gui.pages.certificate_page import CertificatePage
from gui.pages.csr_page import CsrPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(640, 480)
        self.setWindowTitle("CertMaker")

        self.stack = QStackedWidget()

        self.home_page = HomePage()
        self.certificate_page = CertificatePage()
        self.csr_page = CsrPage()

        # make CertificatePage scrollable
        self.scroll_certificate = QScrollArea()
        self.scroll_certificate.setWidgetResizable(True)
        self.scroll_certificate.setWidget(self.certificate_page)
        self.scroll_csr = QScrollArea()
        self.scroll_csr.setWidgetResizable(True)
        self.scroll_csr.setWidget(self.csr_page)

        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.scroll_certificate)
        self.stack.addWidget(self.scroll_csr)

        self.setCentralWidget(self.stack)

        self.home_page.create_certificate_requested.connect(
            self.show_certificate_page
        )

        self.home_page.create_csr_requested.connect(
            self.show_csr_page
        )

        self.certificate_page.action_aborted.connect(
            self.show_home_page
        )

        self.csr_page.action_aborted.connect(
            self.show_home_page
        )

    def show_certificate_page(self):
        self.stack.setCurrentWidget(self.scroll_certificate)

    def show_csr_page(self):
        self.stack.setCurrentWidget(self.scroll_csr)

    def show_home_page(self):
        self.stack.setCurrentWidget(self.home_page)