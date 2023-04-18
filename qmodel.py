# from PySide6.QtCore import QAbstractTableModel, Qt
from PyQt6 import QtCore as qtc
from PyQt6.QtCore import QAbstractTableModel, Qt


class TableModel(QAbstractTableModel):
    def __init__(self, data, combo_index: int = 1):
        super().__init__()
        self._data = data
        self._combo_index = combo_index

    def key(self, idx, idy):
        try:
            return self._data[idx][idy]
        except IndexError:
            return 0

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return qtc.QVariant()

        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data[index.row()][self._combo_index])

        return qtc.QVariant()

    def new_data(self, new_data: list):
        self._data = new_data
        self.dataChanged.emit(0, 0)
