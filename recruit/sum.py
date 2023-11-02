#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import time
import unicodedata
from datetime import datetime
from typing import Optional

# get all file's filepath in current folder
# how to check it is recruit file? if it start with "20"[doge]
filepaths = [
    os.path.abspath(filename)
    for filename in os.listdir(".")
    if filename.startswith("20")
]
# [print(filepath) for filepath in filepaths]


def time_str_foramt(time_str) -> str:
    # 时间格式确实确定, 但是不对齐, 用这个真的两种情况对齐下
    try:
        date_obj = time.strptime(time_str, "%Y")
        return time.strftime("%Y", date_obj)
    except Exception:
        try:
            date_obj = time.strptime(time_str, "%m.%d")
            return time.strftime("%m.%d", date_obj)
        except Exception:
            assert False, time_str


class Submit:
    def __init__(self, filepath: str) -> None:
        filename = os.path.basename(filepath)
        submit_time, company, post, *batch_dummy = list(
            map(str.strip, filename[:-3].split("-"))
        )

        self.filepath = filepath
        self.year: str = time_str_foramt(submit_time[:4])
        self.company = company
        self.post = post
        self.batch = batch_dummy[0] if len(batch_dummy) != 0 else "正式批"
        self.events: (str, str) = [(time_str_foramt(submit_time[5:]), "投递")]

        self.ignore = False
        self.sche_link: Optional[str] = None
        with open(filepath, "r") as f:
            for line in f:
                if line == "<!-- ignore -->\n":
                    self.ignore = True
                if True:
                    pattern = r'\[进度\]\((.*?)\)'
                    match = re.search(pattern, line)
                    # assert match is not None
                    if match is not None:
                        self.sche_link = match.group(1)

                if line.startswith("## "):
                    for event in line[3:].split("|"):
                        event_time, event_name = map(
                            str.strip, event.split("-"))
                        self.events.append(
                            (time_str_foramt(event_time), event_name))

        self.stage = "投递"
        self.order = 0
        # 我将流程阶段分成三层
        order2stage = {
            0: ["投递"],
            1: ["测评", "笔试"],
            2: ["面试"],
            3: ["OC", "挂", "不匹配"],
        }

        def update(event_value: int, index: int):
            if event_value > self.order:
                self.order = event_value
                self.stage = order2stage[self.order][index]

        # 这里统计的针对一个流程, 测评、笔试、面试的次数，用于最后每项总次数的统计
        self.eval_num: int = 0
        self.exam_num: int = 0
        self.interview_num: int = 0

        for event_time, event_name in self.events:
            if "占位" in event_name:
                assert False, event_name
            elif "测评" in event_name or "评测" in event_name:
                self.eval_num += 1
                update(1, 0)
            elif "笔" in event_name and "约" not in event_name and "邀请" not in event_name:
                self.exam_num += 1
                update(1, 1)
            elif "面" in event_name and "约" not in event_name and "邀请" not in event_name:
                self.interview_num += 1
                update(2, 0)
            elif "OC" in event_name:
                update(3, 0)
            elif "挂" in event_name or "调剂" in event_name or "转岗" in event_name:
                update(3, 1)
            elif "不匹配" in event_name:
                update(3, 2)
            else:
                assert (
                    "投递" in event_name
                    or "联系" in event_name
                    or "约" in event_name
                    or "邀请" in event_name
                ), event_name

    def __str__(self) -> str:
        event_str = ", ".join(
            [f"{time_str} {event_name}" for time_str, event_name in self.events])
        return f"{self.year}.{self.events[0][0]}投递{self.company}的{self.post}岗位: {event_str}"

    def __repr__(self) -> str:
        return self.company + " " + self.post + " " + self.batch + " " + str(self.order) + " " + self.stage

    def __lt__(self, other: "Submit"):
        self_time_str = self.events[0][0]
        other_time_str = other.events[0][0]
        self_time = datetime.strptime(self_time_str, "%m.%d")
        other_time = datetime.strptime(other_time_str, "%m.%d")
        return self_time < other_time


def print_yellow(msg: str):
    print("\033[33m" + msg + "\033[0m")


def print_excell_table(table: list[list[str]], pre_seq: list[str]):
    # 各列对齐打印表格，每行元素不限，每列只和有元素的行对齐
    n = len(table)
    if n <= 0:
        return
    m = 0
    for i in range(n):
        m = max(m, len(table[i]))
    # had get (n, m)

    def get_str_width_add(s):
        return sum(2 if unicodedata.east_asian_width(c) in ("F", "W") else 1 for c in s)

    def get_str_width_reduce(s):
        return sum(1 if unicodedata.east_asian_width(c) in ("F", "W") else 0 for c in s)

    col_width = [0 for _ in range(m)]
    ele_width = [[] for _ in range(n)]

    for j in range(m):
        for i in range(n):
            if j >= len(table[i]):
                continue
            col_width[j] = max(col_width[j], get_str_width_add(table[i][j]))
        for i in range(n):
            if j >= len(table[i]):
                continue
            ele_width[i].append(
                col_width[j] - get_str_width_reduce(table[i][j]))

    for i in range(n):
        for j in range(len(table[i])):
            if j == len(table[i]) - 1:
                print(table[i][j], end="")
            else:
                print(table[i][j].ljust(ele_width[i][j]), end="")
                print("," if j >= len(pre_seq) else pre_seq[j], end="")
        print()


def print_all(submits: list[Submit]):
    print_yellow("总览表格")

    table = list()
    pre_seq = ["", "", ":"]

    for submit in submits:
        if submit.ignore is True:
            continue
        row = [submit.company, submit.post]
        for event in submit.events:
            event_str = event[0] + '-' + event[1]
            row.append(event_str)
        table.append(row)

    print_excell_table(table, pre_seq)


def print_sum(submits: list[Submit]):
    print_yellow("数据统计")

    submit_num = 0
    quiet_num = 0
    exam_num = 0
    interview_num = 0
    oc_num = 0
    g_num = 0
    unmatch_num = 0
    for submit in submits:
        submit_num += 1
        if submit.order == 0:
            quiet_num += 1
        elif submit.order == 1:
            exam_num += 1
        elif submit.order == 2:
            interview_num += 1
        elif submit.order == 3:
            if submit.stage == "OC":
                oc_num += 1
            elif submit.stage == "挂":
                g_num += 1
            elif submit.stage == "不匹配":
                unmatch_num += 1
            else:
                assert False
        else:
            assert False

    from rich.console import Console
    from rich.table import Table

    console = Console()

    table = Table(title="投递情况")

    table.add_column("类型", justify="center", style="bold")
    table.add_column("数量", justify="center", style="bold")
    table.add_column("占比", justify="center", style="bold")

    table.add_row("投递", str(submit_num), "-")
    table.add_row("简历筛", str(quiet_num), f"{quiet_num/submit_num:.0%}")
    table.add_row("笔试", str(exam_num), f"{exam_num/submit_num:.0%}")
    table.add_row("面试", str(interview_num), f"{interview_num/submit_num:.0%}")
    table.add_row("OC", str(oc_num), f"{oc_num/submit_num:.0%}")
    table.add_row("挂", str(g_num), f"{g_num/submit_num:.0%}")
    table.add_row("不匹配", str(unmatch_num), f"{unmatch_num/submit_num:.0%}")

    console.print(table)

    print("测评次数:", sum(submit.eval_num for submit in submits))
    print("笔试次数:", sum(submit.exam_num for submit in submits))
    print("面试次数:", sum(submit.interview_num for submit in submits))


def print_click(submits: list[Submit]):
    print_yellow("TODO")
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    table: list[list[str]] = list()
    table.append(["today", "", today.strftime("%m.%d-%A")])

    for submit in submits:
        year_str = submit.year
        row = [submit.company, submit.post]
        for event in submit.events:
            if event[1] == "投递":
                continue
            time_str = year_str + "." + event[0]
            event_data = datetime.strptime(time_str, "%Y.%m.%d")
            if event_data >= today:
                row.append(event[0] + "-" +
                           event_data.strftime("%A") + '-' + event[1])
        if len(row) > 2:
            table.append(row)
    print_excell_table(table, [" ", ":"])


def print_sche_link(submits: list[Submit]):
    print_yellow("Sche Link: ")
    table: list[list[str]] = []
    for submit in submits:
        if submit.sche_link is not None:
            table.append([submit.company, submit.sche_link])
    print_excell_table(table, [":"])


if __name__ == "__main__":
    submits = sorted([Submit(filepath) for filepath in filepaths])
    # [print(i ,str(submit) ) for i, submit in enumerate(submits) ]
    # [print(i ,repr(submit) ) for i, submit in enumerate(submits) ]

    print_sche_link(submits)
    print_all(submits)
    print_sum(submits)
    print_click(submits)
