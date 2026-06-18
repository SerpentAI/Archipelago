import csv
import io


class D2RTable:
    file_name: str
    column_names: tuple[str]

    index_column: str
    rows: list[list[str]]

    row_index_mapping: dict[str, int]
    column_index_mapping: dict[str, int]

    def __init__(self, index_column: str):
        self.index_column = index_column
        self.rows = list()

        self._bootstrap()

        self._determine_column_index_mapping()
        self._determine_row_index_mapping()

    def clear_rows(self):
        self.rows = list()

    def add_row(self, row_data: list[str]):
        self.rows.append(row_data)

    def set_value_by_row_index(self, row_index: str, column: str, value: str):
        self.rows[self.row_index_mapping[row_index]][self.column_index_mapping[column]] = value

    # Dev Only - Should formally live in the mod generator
    def export_txt(self) -> None:
        with open(f"worlds/d2rr/data/mod_generator/mod/{self.file_name}", "w", encoding="cp949", newline="") as f:
            f.write(self.to_txt().read())

    def to_txt(self) -> io.TextIOWrapper:
        txt_buffer: io.BytesIO = io.BytesIO()
        txt_file: io.TextIOWrapper = io.TextIOWrapper(txt_buffer, encoding="cp949", newline="")

        writer = csv.writer(txt_file, dialect="excel-tab", quoting=csv.QUOTE_NONE, quotechar=None)

        writer.writerow(self.column_names)
        writer.writerows(self.rows)

        txt_file.flush()
        txt_buffer.seek(0)

        return txt_file

    def _bootstrap(self):
        pass

    def _determine_column_index_mapping(self):
        self.column_index_mapping = dict()

        for column_index, column_name in enumerate(self.column_names):
            self.column_index_mapping[column_name] = column_index

    def _determine_row_index_mapping(self):
        self.row_index_mapping = dict()

        row: list[str]
        for row_index, row in enumerate(self.rows):
            index_value: str = row[self.column_index_mapping[self.index_column]]
            self.row_index_mapping[index_value] = row_index

