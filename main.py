import argparse
import sys

from tabulate import tabulate

from core import (
    get_full_path,
    read_file,
    create_product_list,
    get_avg_rating
)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Создание отчета',
        add_help=False
    )

    parser.add_argument('--files', nargs='*', help='name files')
    parser.add_argument('--report', help='name report')
    parser.add_argument('--path', help='path to file')

    valid_flags = ('--files', '--report', '--path')

    for arg in sys.argv:
        if arg.startswith('--') and arg not in valid_flags:
            print(f'Ошибка: Неизвестный флаг {arg}!')
            print(f'Допустимые флаги: --files, --report, --path')
            sys.exit(1)

    # args = parser.parse_args()

    if '--files' in sys.argv:
        files_index = sys.argv.index('--files')
        if files_index + 1 >= len(sys.argv) or sys.argv[files_index + 1].startswith('--'):
            parser.error('Флаг --files указан, но не указаны имена файлов! Пример: --files file1.csv file2.csv')
    else:
        parser.error('Не указан обязательный флаг --files! Пример: --files file1.csv file2.csv')

    if '--report' in sys.argv:
        report_index = sys.argv.index('--report')
        if report_index + 1 >= len(sys.argv):
            parser.error('Флаг --report указан, но не указано имя отчета! Пример report')
    return parser.parse_args()


def execute_from_command_line():
    args = parse_args()
    report_name = 'report_default'
    if args.report:
        report_name = args.report
    print(report_name)

    if args.path:
        files = get_full_path(args.files, args.path)
        row_data = read_file(files)
        products = create_product_list(row_data)
    else:
        row_data = read_file(args.files)
        products = create_product_list(row_data)

    avg_report = get_avg_rating(products)
    table_data = [{'Brand': brand, 'Rating': rating} for brand, rating in avg_report.items()]
    if table_data:
        print(tabulate(table_data, headers='keys', tablefmt='grid'))
    else:
        print('Файлы не найдены или пустые')


def main():
    execute_from_command_line()


if __name__ == '__main__':
    main()
