
import sys

from PySide6 import QtGui, QtWidgets

import params as par
from ui.ui_aade_connect import Ui_Dialog
from ui.ui_main import Ui_MainWindow
from validate_data import validate


class EmployeeDlg(QtWidgets.QDialog):
    """Employee dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.load_combo_values()

        self.fill_combo_values()

        self.make_connections()

        # self.table_details_new_line()

    def make_connections(self):
        self.bnew_line.clicked.connect(self.table_details_new_line)
        self.bpost.clicked.connect(self.post_data)
        self.partype.currentIndexChanged.connect(self.update_l1)

    def update_l1(self):
        pass

    def fill_Combo(self, items, combobox):
        for item in items:
            combobox.addItem(item)

    def load_combo_values(self):
        self.ca_combo_op = [i[1] for i in par.icat]
        self.e3_combo_op = [i[1] for i in par.ie3]
        self.fp_combo_op = [i[1] for i in par.fpa]
        self.branch_op = [i[1] for i in par.branch]
        self.partyp_op = [i[1] for i in par.itype]
        self.series_op = par.series

    def post_data(self):
        dlg = EmployeeDlg(self)
        dlg.ui.afm.setText('123456789')
        dlg.exec()

        print(dlg.ui.afm.text())
        print(dlg.ui.user.text())
        print(dlg.ui.key.text())

        data = self.collect_data()
        val, errors = validate(data)
        if not val:
            QtWidgets.QMessageBox.critical(self, 'Λάθος', errors)
            return
        self.results.setText(str(data))

    def collect_data(self):
        data = {
            'date': self.date.date().toString("yyyy-MM-dd"),
            'branch': par.branch[self.branch.currentIndex()][0],
            'type': par.itype[self.partype.currentIndex()][0],
            'series': self.series.currentText(),
            'aa': self.aa.text(),
            'cafm': self.cafm.text(),
            'lines': self.collect_data_from_table()
        }
        return data

    def collect_data_from_table(self):
        rowno = self.tlines.rowCount()
        tit = ['aa', 'cat', 'e3', 'fpa', 'val']
        data = []
        for row in range(rowno):
            coldata = {
                'aa': self.tlines.item(row, 0).text(),
                'cat': par.icat[self.tlines.cellWidget(row, 1).currentIndex()][0],
                'e3': par.ie3[self.tlines.cellWidget(row, 2).currentIndex()][0],
                'fpa': par.fpa[self.tlines.cellWidget(row, 3).currentIndex()][0],
                'val': self.tlines.cellWidget(row, 4).value()
            }
            data.append(coldata)
        return data

    def fill_combo_values(self):
        self.fill_Combo(self.branch_op, self.branch)
        self.fill_Combo(self.partyp_op, self.partype)
        self.fill_Combo(self.series_op, self.series)

    def table_details_new_line(self):
        index = self.tlines.rowCount()
        lines = index + 1
        self.tlines.setRowCount(lines)

        item1 = QtWidgets.QTableWidgetItem(str(lines))
        self.tlines.setItem(index, 0, item1)

        ca_combo = QtWidgets.QComboBox()
        self.fill_Combo(self.ca_combo_op, ca_combo)
        self.tlines.setCellWidget(index, 1, ca_combo)

        e3_combo = QtWidgets.QComboBox()
        self.fill_Combo(self.e3_combo_op, e3_combo)
        self.tlines.setCellWidget(index, 2, e3_combo)

        fp_combo = QtWidgets.QComboBox()
        self.fill_Combo(self.fp_combo_op, fp_combo)
        self.tlines.setCellWidget(index, 3, fp_combo)

        val = QtWidgets.QDoubleSpinBox()
        self.tlines.setCellWidget(index, 4, val)
        val.setMaximum(99999)  # Να το βάλουμε στις παραμέτρους
        val.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        val.setAlignment(QtGui.Qt.AlignRight)

        self.tlines.resizeColumnsToContents()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
