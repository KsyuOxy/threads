from threading import Thread
from time import sleep
from tkinter import Label


class NumsThread(Thread):  # -> поток вставляет обноввлённый список чисел в лейбл в течении выполнения и записыв в файл
    def __init__(self, list_nums: list, duration: float, lbl: Label, path: str):
        super().__init__()
        self.__list_nums = list_nums
        self._duration = duration
        self._label = lbl
        self._path = path
        self._result_nums = []

    def run(self):
        for n in self.__list_nums:
            self._result_nums.append(n)
            self._label.config(text=self._result_nums)
            sleep(self._duration)
        with open(self._path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self._result_nums))  # ->

