from ping3 import ping
#from func import find_median
import func


def ping_cheking(hosts, count_ping_req):

    result_pass_ping = {}
    result_pass_ping_no = []

    for ip in hosts:
        print(f"IP: {ip}")

        count_error = 0
        temp_lst_for_med = []

        for attempt in range(1, count_ping_req + 1):
            # Параметры проверки
            response = ping(ip, timeout=1, unit='ms')

            if response is False or response is None:
                count_error += 1
                if count_error == 3:
                    break
            else:
                temp_lst_for_med.append(response)

        if temp_lst_for_med and count_error < 3:
            result_pass_ping[ip] = func.find_median(temp_lst_for_med)
        else:
            result_pass_ping_no.append(ip)

        result_pass_ping = dict(sorted(result_pass_ping.items(), key=lambda x: x[1]))

    return result_pass_ping, result_pass_ping_no


def test():
    print("")
    print(f"{ip_list[0]} : {ip_country_dict[ip_list[0]]}")
    os.system(f"mtr -r -c 50 {list(sorted_dict_desc.keys())[0]}")
    time.sleep(50)

    print("")
    print(f"{ip_list[1]} : {ip_country_dict[ip_list[1]]}")
    os.system(f"mtr -w -c 50 {list(sorted_dict_desc.keys())[1]}")
    time.sleep(50)

    print("")
    print(f"{ip_list[2]} : {ip_country_dict[ip_list[2]]}")
    os.system(f"mtr -w -c 50 {list(sorted_dict_desc.keys())[2]}")