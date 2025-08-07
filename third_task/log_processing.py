
'''
Function  which takes a line from the log as an input parameter and returns a dictionary with parsed components:
date, time, level, message. 
'''

def parse_log_line(line: str) -> dict:
    log_dict = {}
    line = line.split()
    log_dict['date'] = line[0]
    log_dict['time'] = line[1]
    log_dict['level'] = line[2]
    log_dict['message'] = ' '.join(line[3:])
    return log_dict


'''
Function which opens the file, reads each line and applies the parse_log_line function to it,
storing the results in a list. 
'''

def load_logs(file_path: str, log_level=None) -> list:
    # try:
    with open(file_path, 'r', encoding='utf-8') as file:
        logs = file.readlines()
        log_list = [parse_log_line(log) for log in logs]
        return log_list


'''
Function which filters by logging level and returns all log entries for a specific logging level
'''

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = [log for log in logs if log['level'].lower() == level.lower()]
    if not filtered_logs:
        print(f" No records with level '{level.upper()}' found in the logs.")
    return filtered_logs


'''
Function which counts the number of records for each logging level
'''

def count_logs_by_level(logs: list) -> dict:
    counted_levels = {}
    for log in logs:
        if not log['level'] in counted_levels:
            counted_levels[log['level']] = 1
        else:
            counted_levels[log['level']] += 1
    return counted_levels


'''
Function which formats and outputs calculation results in a readable form
'''

def display_log_counts(counts: dict):
    print(f'\n {"LEVEL":<10} | {"COUNT":<10}')
    print('-' * 20)
    for level, count in counts.items():
        print(f'{level:<10} | {count:<10}')


'''
Function which formats and outputs calculation results in a readable form
'''

def display_log_level(filtered_logs: dict):
    print(f'\n{"DATE":<12} | {"TIME":<8} | {"LEVEL":<7} | MESSAGE ')
    print('-' * 70)
    for filtered_log in filtered_logs:
        print(
            f"{filtered_log['date']:<12} | {filtered_log['time']:<8} | {filtered_log['level']:<7} | {filtered_log['message']}")




