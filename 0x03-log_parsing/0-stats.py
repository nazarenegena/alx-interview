#!/usr/bin/python3
'''parsing HTTP request logs script
'''
import re


def extract_input(input_line):
    '''extracting sections of a line.
    '''
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    infoData = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(pattern[0], pattern[1], pattern[2], pattern[3], pattern[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        infoData['status_code'] = status_code
        infoData['file_size'] = file_size
    return infoData


def print_statistics(total_file_size, status_codes_stats):
    '''printing accumulated statistics of HTTP request log.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        number = status_codes_stats.get(status_code, 0)
        if number > 0:
            print('{:s}: {:d}'.format(status_code, number), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updating  metrics from a given HTTP request log.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Starting the log parser.
    '''
    line_number = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_number += 1
            if line_number % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
