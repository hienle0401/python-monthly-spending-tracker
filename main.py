import pandas as pd
import camelot as cm


def extract_tables_from_pdf(file_path):
    tables = cm.read_pdf(file_path, pages='all', flavor='stream')
    return tables

