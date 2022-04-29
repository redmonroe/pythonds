from chapter4_basic_ds import Queue
import random
from datetime import datetime


class Printer:
    '''we are trying to get the total print time'''
    '''this might be were the queue should be, are there two?'''
    def __init__(self, quality):
        self.quality = quality
        self.print_time = None
        self.task = None

    def set_task(self, task=None):
        # breakpoint()
        self.task = task
        print(f'printing task: request time: {task.request_time} len: {task.length} timestampt: {task.timestamp}')

    def set_print_time(self):
        '''draft 10 pages per minutes'''
        if self.quality == 'draft':
            self.print_time = self.task.length * 6
            print(f'print time: {self.print_time} seconds')

class Task:
    
    def __init__(self, request_time, other=None):
        self.request_time = request_time 
        self.timestamp = None 
        self.length = None

    def set_length(self):
        self.length = random.randrange(1,21)

    def set_ts(self):
        dt = datetime.now()
        self.timestamp = datetime.timestamp(dt)

    def __repr__(self):
        return f'request time: {self.request_time} timestamp: {self.timestamp} length: {self.length}'

class PrintQueue(Queue):
    pass


qq = PrintQueue()
for currentSecond in range(3600):
    num = random.randrange(1, 181)
    if num == 180:
        task = Task(currentSecond)
        task.set_length()
        task.set_ts()
        qq.enqueue(task)

while qq.is_empty() == False:
    print('start size:', qq.size())
    printer = Printer(quality='draft')
    task = qq.dequeue()
    print('end size:', qq.size())
    # breakpoint()

    printer.set_task(task=task)
    printer.set_print_time()
    '''dequeue into printer'''
    
# breakpoint()

