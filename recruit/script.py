#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import time
import unicodedata
from datetime import datetime
from typing import Optional

PREFIX = "1-"
print(f"uuid = {PREFIX[:-1]}")
ETCFILENAME = "etc.md"

filepaths = [
    os.path.abspath(filename)
    for filename in os.listdir(".")
    if filename.startswith(PREFIX)
]


def util_time_str_format(time_str: str) -> str:
    try:
        date_obj = time.strptime(time_str, "%Y")
        return time.strftime("%Y", date_obj)
    except Exception:
        try:
            date_obj = time.strptime(time_str, "%m.%d")
            return time.strftime("%m.%d", date_obj)
        except Exception:
            assert False, f"{time_str}既不是年份也不是月日"


class Submit:
    def __init__(
        self,
        year: str,  # 投递时年份, 流程不能跨年, 由对事件有序性断言保证
        company: str,  # 公司名
        position: str,  # 岗位
        batch: str,  # 批次
        events: list[tuple[str, str]],  # 事件列表
    ) -> None:
        self.year: str = year
        self.company: str = company
        self.position: str = position
        self.batch: str = batch
        self.events: list[tuple[str, str]] = events

        self.stage_str = "投递"
        self.stage_level = 0

        def stage_update(event_level: int, index: int):
            level2stage_map = {
                0: ["投递"],
                1: ["测评", "笔试"],
                2: ["面试"],
                3: ["OC", "挂", "不匹配"],
            }

            if event_level > self.stage_level:
                self.stage_level = event_level
                self.stage_str = level2stage_map[self.stage_level][index]

        self.eval_num: int = 0
        self.exam_num: int = 0
        self.interview_num: int = 0

        for _, event_name in self.events:
            if "测评" in event_name or "评测" in event_name:
                self.eval_num += 1
                stage_update(1, 0)
            elif "笔" in event_name and "约" not in event_name and "邀请" not in event_name:
                self.exam_num += 1
                stage_update(1, 1)
            elif "面" in event_name and "约" not in event_name and "邀请" not in event_name:
                self.interview_num += 1
                stage_update(2, 0)
            elif "OC" in event_name:
                stage_update(3, 0)
            elif (
                "挂" in event_name
                or "简历挂" in event_name
                or "调剂" in event_name
                or "转岗" in event_name
            ):
                stage_update(3, 1)
            elif "不匹配" in event_name:
                stage_update(3, 2)
            else:
                assert (
                    "投递" in event_name
                    or "联系" in event_name
                    or "约" in event_name
                    or "邀请" in event_name
                ), event_name

        self.ignore: bool = False
        self.progress_link: str = ""

    @staticmethod
    def handle_filename(
        filename: str,
    ) -> tuple[str, str, str, str, list[tuple[str, str]]]:
        submit_time, company, position, *dummy = list(
            map(str.strip, filename[:-3].split("-"))
        )
        year: str = util_time_str_format(submit_time[:4])
        company = company
        position = position
        batch = dummy[0] if len(dummy) != 0 else "正式批"
        events: list[tuple[str, str]] = [(util_time_str_format(submit_time[5:]), "投递")]
        return year, company, position, batch, events

    @staticmethod
    def check_ignore(line: str) -> bool:
        return line == "<!-- ignore -->\n"

    @staticmethod
    def get_progress_link(line: str) -> Optional[str]:
        pattern = r"\[进度\]\((.*?)\)"
        match = re.search(pattern, line)
        if match is None:
            return None
        return match.group(1)

    @classmethod
    def from_filepath(cls, filepath: str):
        filename = os.path.basename(filepath).removeprefix(PREFIX)
        year, company, position, batch, events = Submit.handle_filename(filename)

        ignore = False
        progress_link: Optional[str] = None
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if Submit.check_ignore(line):
                    ignore = True
                if (dummy := Submit.get_progress_link(line)) is not None:
                    progress_link = dummy
                if line.startswith("## "):
                    for event in line[3:].split("|"):
                        event_time, event_name = map(str.strip, event.split("-"))
                        events.append((util_time_str_format(event_time), event_name))

        obj = cls(year, company, position, batch, events)
        obj.ignore = ignore
        if progress_link is not None:
            obj.progress_link = progress_link
        return obj

    def __lt__(self, other: "Submit"):
        self_time_str = self.events[0][0]
        other_time_str = other.events[0][0]
        self_time = datetime.strptime(self_time_str, "%m.%d")
        other_time = datetime.strptime(other_time_str, "%m.%d")
        return self_time < other_time


submits = [Submit.from_filepath(filepath) for filepath in filepaths]

with open(ETCFILENAME, "r", encoding="utf-8") as f:
    submit: Optional[Submit] = None
    for line in f:
        if line.startswith("+ "):
            year, company, position, batch, events = Submit.handle_filename(line[4:])
            if submit is not None:
                submit.ignore = True
                submits.append(submit)
                submit = None
            submit = Submit(year, company, position, batch, events)
        elif line.startswith("  + "):
            for event in line[3:].split("|"):
                event_time, event_name = map(str.strip, event.split("-"))
                assert submit is not None, "Define"
                submit.events.append((util_time_str_format(event_time), event_name))
        else:
            if (
                dummy := Submit.get_progress_link(line)
            ) is not None and submit is not None:
                submit.progress_link = dummy


submits = sorted(submits)


def print_excell_table(table: list[list[str]], pre_seq: list[str]):
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
    ele_width: list[list[int]] = [[] for _ in range(n)]

    for j in range(m):
        for i in range(n):
            if j >= len(table[i]):
                continue
            col_width[j] = max(col_width[j], get_str_width_add(table[i][j]))
        for i in range(n):
            if j >= len(table[i]):
                continue
            ele_width[i].append(col_width[j] - get_str_width_reduce(table[i][j]))

    for i in range(n):
        for j in range(len(table[i])):
            if j == len(table[i]) - 1:
                print(table[i][j], end="")
            else:
                print(table[i][j].ljust(ele_width[i][j]), end="")
                print("," if j >= len(pre_seq) else pre_seq[j], end="")
        print()


def print_all():
    """为未忽略未省略的投递打印总览表格"""
    table = list()
    pre_seq = ["", "", ":"]

    for submit in submits:
        if submit.ignore is True:
            continue
        row = [submit.company, submit.position]
        for event in submit.events:
            event_str = event[0] + "-" + event[1]
            row.append(event_str)
        table.append(row)

    print_excell_table(table, pre_seq)


def print_sum():
    """打印数据统计"""
    submit_num = 0
    quiet_num = 0
    exam_num = 0
    interview_num = 0
    oc_num = 0
    g_num = 0
    unmatch_num = 0
    for submit in submits:
        submit_num += 1
        if submit.stage_level == 0:
            quiet_num += 1
        elif submit.stage_level == 1:
            exam_num += 1
        elif submit.stage_level == 2:
            interview_num += 1
        elif submit.stage_level == 3:
            if submit.stage_str == "OC":
                oc_num += 1
            elif submit.stage_str == "挂":
                g_num += 1
            elif submit.stage_str == "不匹配":
                unmatch_num += 1
            else:
                assert False
        else:
            assert False

    if submit_num == 0:
        print("还未进行投递")
        return

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


def print_click():
    """TODO: 后面流程提示"""
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    table: list[list[str]] = list()
    table.append(["today", "", today.strftime("%m.%d-%A")])

    for submit in submits:
        year_str = submit.year
        row = [submit.company, submit.position]
        for event in submit.events:
            if event[1] == "投递":
                continue
            time_str = year_str + "." + event[0]
            event_data = datetime.strptime(time_str, "%Y.%m.%d")
            if event_data >= today:
                row.append(event[0] + "-" + event_data.strftime("%A") + "-" + event[1])
        if len(row) > 2:
            table.append(row)
    print_excell_table(table, [" ", ":"])


CMDS = {
    "all": print_all,
    "sum": print_sum,
    "click": print_click,
}


try:
    from dryad import Dryad  # type: ignore
except Exception as e:
    print("git clone https://github.com/zweix123/dryad.git")
    print("cd dryad")
    print("pip install .")
    exit(-1)

Dryad(cmd_tree=CMDS)
