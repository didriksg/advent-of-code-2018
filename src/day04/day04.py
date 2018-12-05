from src.utils import Inputstr
import time
from collections import defaultdict, Counter
import re
import operator
import numpy as np

class DateInfo:  # Contains information about a specific date
    def __init__(self, date, info, guard_id = None):
        # Datestamps for this specific date
        self.date = date
        self.info = info
        self.guard_id = guard_id if guard_id is not None else None
        self.extract_info(info)

    def extract_info(self, info):
        self.sleep = [0] * 60
        first_val = info[0][1]
        if "Guard" in first_val:
            self.guard_id = int(re.findall("\d+", first_val)[0])

        for i in info:
            time, string = i
            hour, minute = [int(j) for j in time.split(':')]

            if hour == 23:
                continue
            if "falls asleep" in string:
                self.sleep[minute] = 1
            elif "wakes up" in string:
                self.sleep[minute] = -1

        self.sleep = self.fill_empty(self.sleep)

    def fill_empty(self, minutes):
        prev_fill = bool(minutes[0])
        minutes_filled = [0] * 60
        for j, i in enumerate(minutes[1:], start=1):
            if i == 1:
                prev_fill = not prev_fill
            elif i == -1:
                prev_fill = not prev_fill
            minutes_filled[j] = int(prev_fill)
        return minutes_filled


def get_info(day, test=False):
    return Inputstr(day, test).split("\n")


def part_1(input):
    dates = defaultdict()
    date_info = defaultdict()

    for i in input:
        timestamp, info = i.split("]")
        date, time = timestamp.split(" ")
        _, month, day = date.split("-")

        if month + "-" + day not in dates:
            dates[month + "-" + day] = [(time, info)]
        else:
            dates[month + "-" + day].append((time, info))
    guard = None
    for date in sorted(dates.keys()):
        sorted_values = sorted(dates[date], key=lambda x: (x[0]))
        date_info[date] = DateInfo(date, sorted_values, guard)
        for val in sorted_values:
            if "23" in val[0].split(":")[0]:
                guard = int(re.findall("\d+", val[1])[0])
            else:
                guard = None
    ls = 0
    lsid = None
    lsmin = None

    guard_sleep = {date_info[ds].guard_id: (0,[]) for ds in date_info}

    for d in date_info:
        ds_obj = date_info[d]
        count, sleep_times = guard_sleep[ds_obj.guard_id]
        count += sum(ds_obj.sleep)
        sleep_times.append(ds_obj.sleep)

        guard_sleep[ds_obj.guard_id] = (count,sleep_times)
    max_sleep_id = max(guard_sleep.items(), key=operator.itemgetter(1))[0]
    freq_sleep = defaultdict()
    for gs in guard_sleep:
        np_sleep = np.array(guard_sleep[gs][1])
        if gs not in freq_sleep:
            freq_sleep[gs] = np_sleep.sum(axis=0)
        else:
            freq_sleep[gs].add(np_sleep.sum(axis=0))

    np_sleep = np.array(guard_sleep[max_sleep_id][1])
    tot_sleep = np_sleep.sum(axis=0)
    print(tot_sleep.argmax(), max_sleep_id, tot_sleep.argmax()*max_sleep_id)

    MS = 0
    msid = 0
    msmin = 0
    for fs in freq_sleep:
        ms = max(freq_sleep[fs])
        if ms > MS:
            MS = ms
            msmin = freq_sleep[fs].argmax()
            msid = fs

    print(msmin, msid, msmin * msid)




def part_2(input):
    # print(MS, msid, MS * msid)
    pass

def main():
    start_time_total = time.time()
    input = get_info("04", test=False)

    start_time_part_1 = time.time()
    p1 = part_1(input)
    end_time_part_1 = time.time()
    print(p1)
    print("Part 1 time: {0:.2f}ms".format((end_time_part_1 - start_time_part_1) * 1000))

    start_time_part_2 = time.time()
    part_2(input)
    end_time_part_2 = time.time()
    print("Part 2 time: {0:.2f}ms".format((end_time_part_2 - start_time_part_2) * 1000))

    print("Total time: {0:.2f}ms".format((time.time() - start_time_total) * 1000))


if __name__ == "__main__":
    main()
