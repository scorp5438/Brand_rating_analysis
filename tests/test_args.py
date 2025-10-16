import sys

import pytest

from main import parse_args


class TestArgParse:
    def test_valid_args(self, monkeypatch):
        """Тест корректных аргументов"""
        test_args = ['--files', 'data.csv', '--report', 'output.csv']
        monkeypatch.setattr(sys, 'argv', ['main.py'] + test_args)

        args = parse_args()
        assert args.files == ['data.csv']
        assert args.report == 'output.csv'

    def test_missing_files_flag(self, monkeypatch):
        """Тест отсутствия обязательного флага --files"""
        test_args = ['--report', 'output.csv']
        monkeypatch.setattr(sys, 'argv', ['main.py'] + test_args)

        with pytest.raises(SystemExit):
            parse_args()

    def test_multiple_files(self, monkeypatch):
        """Тест нескольких файлов"""
        test_args = ['--files', 'file1.csv', 'file2.csv', 'file3.csv']
        monkeypatch.setattr(sys, 'argv', ['main.py'] + test_args)

        args = parse_args()
        assert args.files == ['file1.csv', 'file2.csv', 'file3.csv']
        assert len(args.files) == 3