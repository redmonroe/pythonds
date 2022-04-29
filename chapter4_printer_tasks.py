from chapter4_basic_ds import Queue
import random
from datetime import datetime


class Printer:
    '''we are trying to get the total print time'''
    '''this might be were the queue should be, are there two?'''
    def __init__(self, ppm):
        self.quality = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.quality

class Task:
    
    def __init__(self, time, other=None):
        self.timestamp = time 
        self.pages = random.randrange(1,21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp
        
def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

def simulation(num_secs, pages_per_minute):
    
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_secs):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            nexttask = print_queue.dequeue()
            waiting_times.append(nexttask.wait_time(current_second))
            lab_printer.start_next(nexttask)

        lab_printer.tick()

    average_wait = sum(waiting_times)/len(waiting_times)
    print(f'average wait {average_wait}, tasks remaining {print_queue.size()}')


for i in range(10):
    simulation(3600, 5)


        


# qq = PrintQueue()
# for currentSecond in range(3600):
#     num = random.randrange(1, 181)
#     if num == 180:
#         task = Task(currentSecond)
#         task.set_length()
#         task.set_ts()
#         qq.enqueue(task)

# while qq.is_empty() == False:
#     print('start size:', qq.size())
#     printer = Printer(quality='draft')
#     task = qq.dequeue()
#     print('end size:', qq.size())
#     # breakpoint()

#     printer.set_task(task=task)
#     printer.set_print_time()
#     '''dequeue into printer'''
    
# breakpoint()

