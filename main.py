from log_processing import parse_log_line, load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts, display_log_level
import  sys, pathlib


def main():
    if len(sys.argv) < 2:
        print('Enter the right path to a log file')
        return
    try:
        file_path = sys.argv[1]
        log_level = sys.argv[2] if len(sys.argv) > 2 else None
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        if log_level:
            filtered_logs = filter_logs_by_level(logs, log_level)
            display_log_level(filtered_logs)


    except FileNotFoundError:
        print('File does not exist')



# logfile_path = sys.argv[1]
# print(logfile_path)





if __name__ == '__main__':
        main()
