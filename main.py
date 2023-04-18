import sys
from datetime import date

from PyQt6 import QtCore, QtWidgets

import params as par
from qmodel import TableModel

# from ui.ui_aade_connect import Ui_Dialog
from ui.main_ui import Ui_MainWindow
from validate_data import validate


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.counter = 0

        self.date.setDate(date.today())

        self.connect_combos_to_models()
        self.reset_wheel_for_combos()
        self.make_connections()

        self.create_actions()

    def connect_combos_to_models(self):
        self.partype.setModel(TableModel(par.itype))
        self.branch.setModel(TableModel(par.branch))
        self.series.setModel(TableModel(par.series, 0))

    def reset_wheel_for_combos(self):
        self.reset_wheel(self.partype)
        self.reset_wheel(self.branch)
        self.reset_wheel(self.series)

    def create_actions(self):
        self.actionopen.triggered.connect(self.openf)
        self.actionexit.triggered.connect(self.close)

    def openf(self):
        pass
        # dlg = EmployeeDlg(self)
        # dlg.ui.afm.setText("123456789")
        # dlg.exec()

    def make_connections(self):
        self.bnew_line.clicked.connect(self.table_details_new_line)
        self.bpost.clicked.connect(self.post_data)
        self.partype.currentIndexChanged.connect(self.partype_changed)

    def reset_wheel(self, combobox):
        # ακυρώνουμε και την ροδέλα του ποντικιού
        combobox.wheelEvent = lambda event: None

    def post_data(self):
        data = self.collect_data()
        errors = validate(data)
        if errors:
            QtWidgets.QMessageBox.critical(self, "Λάθος", "\n".join(errors))
            return
        self.results.setText(str(data))

    def collect_data(self):
        data = {
            "date": self.date.date().toString("yyyy-MM-dd"),
            "branch": self.branch_value,
            "type": self.typos_parastatikou,
            "series": self.series.currentText(),
            "aa": self.aa.text(),
            "cafm": self.cafm.text(),
            "lines": self.collect_data_from_table(),
        }

        return data

    def collect_data_from_table(self):
        rowno = self.tlines.rowCount()
        data = []
        for row in range(rowno):
            val = self.tlines.cellWidget(row, 4).value()
            if val <= 0:
                continue
            cbo_cat = self.tlines.cellWidget(row, 1)
            cbo_val = cbo_cat.model().key(cbo_cat.currentIndex(), 0)

            cbo_e3 = self.tlines.cellWidget(row, 2)
            e3_index = cbo_e3.currentIndex()
            e3_model = cbo_e3.model()
            e3_val = e3_model.key(e3_index, 0)
            coldata = {
                "aa": self.tlines.item(row, 0).text(),
                "cat": cbo_val,
                "e3": e3_val,
                "fpa": par.fpa[self.tlines.cellWidget(row, 3).currentIndex()][0],
                "val": val,
            }
            data.append(coldata)
        return data

    @property
    def typos_parastatikou(self):
        return self.partype.model().key(self.partype.currentIndex(), 0)

    @property
    def branch_value(self):
        return self.branch.model().key(self.partype.currentIndex(), 0)

    @property
    def category_list(self):
        return par.category_frompartype(self.typos_parastatikou)

    def line_models_connections(self, row, first=False):
        combo_cat = self.tlines.cellWidget(row, 1)
        combo_e3 = self.tlines.cellWidget(row, 2)

        self.reset_wheel(combo_cat)
        self.reset_wheel(combo_e3)

        combo_cat.setModel(TableModel(self.category_list))

        def combo_cat_changed():
            new_cat = combo_cat.model().key(combo_cat.currentIndex(), 0)
            fresh_e3 = par.e3_from_partyp_category(self.typos_parastatikou, new_cat)
            combo_e3.setModel(TableModel(fresh_e3, 1))

        if first:
            combo_cat.currentIndexChanged.connect(combo_cat_changed)

        combo_cat_changed()

    def partype_changed(self):
        for row in range(self.tlines.rowCount()):
            self.line_models_connections(row)

    def table_details_new_line(self):
        index = self.tlines.rowCount()
        lines = index + 1
        self.tlines.setRowCount(lines)

        self.tlines.setItem(index, 0, QtWidgets.QTableWidgetItem(str(lines)))
        self.tlines.setCellWidget(index, 1, QtWidgets.QComboBox())
        self.tlines.setCellWidget(index, 2, QtWidgets.QComboBox())

        fpa_combo = QtWidgets.QComboBox()
        self.reset_wheel(fpa_combo)
        fpa_combo.setModel(TableModel(par.fpa))
        self.tlines.setCellWidget(index, 3, fpa_combo)

        val = QtWidgets.QDoubleSpinBox()
        self.tlines.setCellWidget(index, 4, val)

        val.setMaximum(99999)  # Να το βάλουμε στις παραμέτρους
        val.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        val.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        self.line_models_connections(index, True)
        self.tlines.resizeColumnsToContents()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
