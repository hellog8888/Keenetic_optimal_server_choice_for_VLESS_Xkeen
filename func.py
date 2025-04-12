import datetime


def current_date_and_time():
    cur_time = datetime.datetime.now()
    return f'{cur_time.day}-{cur_time.month:02}-{cur_time.year}_{cur_time.hour:02}_{cur_time.minute:02}_{cur_time.second:02}'


def find_median(lst):
    if not lst:
        return None
    sorted_list = sorted(lst)
    mid_idx = (len(sorted_list) - 1) // 2

    if len(sorted_list) % 2 == 0:
        return (sorted_list[mid_idx] + sorted_list[mid_idx + 1]) / 2.0
    else:
        return sorted_list[mid_idx]


def get_lst_from_file(file_txt):
    with open(file_txt, 'r') as file_txt_r:
        return [line.rstrip('\n') for line in file_txt_r]
