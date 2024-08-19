
try:
    with open("ups.log", 'r') as log_file:
        lines_count = len(log_file.readlines())
except FileNotFoundError:
    print("File Not Fount")


if lines_count >= 3600:
    with open("ups.log", 'r') as log_file:
        with open("history.log", "w") as history_file:
            history_file.writelines(log_file)

    with open("ups.log", 'w') as log_file:
        log_file.write('')



