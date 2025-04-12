import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
)

class ProveedoresManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Proveedores")
        self.data = []
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.inputs = {}

        fields = ["nombre", "telefono"]
        form_group = QGroupBox("Formulario de Proveedores")
        form_layout = QGridLayout()

        for idx, field in enumerate(fields):
            label = QLabel(field.capitalize() + ":")
            input_field = QLineEdit()
            form_layout.addWidget(label, idx, 0)
            form_layout.addWidget(input_field, idx, 1)
            self.inputs[field] = input_field

        form_group.setLayout(form_layout)
        layout.addWidget(form_group)

        button_layout = QHBoxLayout()
        self.btn_add = QPushButton("Agregar")
        self.btn_add.clicked.connect(self.add_data)
        button_layout.addWidget(self.btn_add)

        self.btn_delete = QPushButton("Eliminar")
        self.btn_delete.clicked.connect(self.delete_data)
        button_layout.addWidget(self.btn_delete)

        self.btn_refresh = QPushButton("Ver Registros")
        self.btn_refresh.clicked.connect(self.refresh_table)
        button_layout.addWidget(self.btn_refresh)

        layout.addLayout(button_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(len(fields) + 1)
        self.table.setHorizontalHeaderLabels(["ID"] + fields)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def add_data(self):
        new_entry = [len(self.data) + 1]
        for field in self.inputs:
            value = self.inputs[field].text()
            if not value:
                QMessageBox.warning(self, "Error", f"El campo {field} no puede estar vacío.")
                return
            new_entry.append(value)

        self.data.append(new_entry)
        self.refresh_table()
        for input_field in self.inputs.values():
            input_field.clear()

    def delete_data(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            del self.data[selected_row]
            self.refresh_table()
        else:
            QMessageBox.warning(self, "Error", "Seleccione un registro para eliminar.")

    def refresh_table(self):
        self.table.setRowCount(len(self.data))
        for row_idx, row_data in enumerate(self.data):
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProveedoresManager()
    window.show()
    sys.exit(app.exec())
