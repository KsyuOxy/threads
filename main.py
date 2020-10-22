from models import *
from driver import TXTDriver
from gui import *

if __name__ == '__main__':

    t = TXTDriver('numbers.txt')
    n = t.get_negative()  # -> получ список положит чисел из файла
    p = t.get_positive()  # -> получ список отриц чисел из файла
    nums = t.get_nums()  # -> получ список всех чисел из файла

    lbl_nums.config(text=nums)  # ->  список всех чисел  в лейбл

    thread_positive = NumsThread(p, 0.5, lbl_positive, 'positive_nums.txt')  # -> поток позотивн чисел
    thread_positive.daemon = True  # -> вторичный
    thread_positive.start()

    thread_positive = NumsThread(n, 0.5, lbl_negative, 'negative_nums.txt')  # -> поток негативн чисел
    thread_positive.daemon = True  # -> вторичный
    thread_positive.start()

    root.mainloop()



