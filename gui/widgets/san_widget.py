from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QHBoxLayout, QComboBox, QLineEdit, QPushButton, \
    QTableWidgetItem, QMessageBox, QGroupBox, QHeaderView
from dataclasses import dataclass
import ipaddress
import re

@dataclass
class SanEntry:
    type: str
    value: str


class SanWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        SANGroup = QGroupBox("SAN")
        SANLayout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(
            ["Type", "Value"]
        )

        self.table.setColumnWidth(0,100)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        self.table.setColumnWidth(1,300)

        SANLayout.addWidget(self.table)


        input_layout = QHBoxLayout()

        self.type_box = QComboBox()
        self.type_box.addItems([
            "DNS",
            "IP",
        ])

        self.value_edit = QLineEdit()

        add_button = QPushButton("Add")

        add_button.clicked.connect(
            self.add_entry
        )

        input_layout.addWidget(self.type_box)
        input_layout.addWidget(self.value_edit)
        input_layout.addWidget(add_button)


        SANLayout.addLayout(input_layout)
        SANGroup.setLayout(SANLayout)
        layout.addWidget(SANGroup)

    def add_entry(self):
        san_type = self.type_box.currentText()
        value = self.value_edit.text().strip()

        if not self.validate_entry():
            return

        row = self.table.rowCount()

        self.table.insertRow(row)

        self.table.setItem(
            row,
            0,
            QTableWidgetItem(san_type)
        )

        self.table.setItem(
            row,
            1,
            QTableWidgetItem(value)
        )

        self.value_edit.clear()

    def validate_entry(self) -> bool:
        san_type = self.type_box.currentText()
        san_value = self.value_edit.text().strip()

        if san_type == "DNS":
            labels = san_value.split(".")
            for label in labels:
                if not re.fullmatch(r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$', label):
                    QMessageBox.warning(self, " ", "DNS Name not valid")
                    return False
            return True

        if san_type == "IP":
            try:
                ipaddress.ip_address(san_value)
            except ValueError:
                QMessageBox.warning(self, " ", "Not a valid IP address")
                return False
            return True

        QMessageBox.warning(self, " ", "Unkown SAN-Type")
        return False

    def get_entries(self) -> list[SanEntry]:
        entries = []

        for row in range(self.table.rowCount()):
            entries.append(
                SanEntry(
                    type=self.table.item(row, 0).text(),
                    value=self.table.item(row,1).text()
                )
            )

        return entries

    def clear_table(self):
        self.table.setRowCount(0)