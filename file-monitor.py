import os
import schedule
import time
from datetime import datetime
from utility import FileMonitor


class FileMonitorTask(FileMonitor):
    def __init__(self, path='./file-store', log_path="./logs"):
        super().__init__(path, log_path)

    @staticmethod
    def get_files(path):
        files = os.listdir(path)
        return files

    @staticmethod
    def get_count_of_match(word='CDS', line=''):
        if len(line) > 1:
            str_lst = line.split()
            return str_lst.count(word)
        return 0

    def generate_log_file(self, file_count=1, data_dict=dict()):
        for i in range(file_count):
            file_name = '{}/{}.log'.format(self._FILE_LOG_PATH,'search_result')
            with open(file_name, 'a') as f:
                f.write('{}\n'.format(datetime.now()))
                for file_name, count in data_dict.items():
                    lin_str = '{} : {}\n'.format(file_name, count)
                    f.write(lin_str)
                f.write('-' * 35 + "\n")
                f.close()

    def read_files(self):
        files = self.get_files(path=self._FILE_STORE_PATH)
        data_dict = dict()
        for file in files:
            f_path = '{}/{}'.format(self._FILE_STORE_PATH, file)
            with open(f_path, 'r') as f:
                lines = f.readlines()
                cds_count = 0
                for line in lines:
                    cds_count += self.get_count_of_match(line=line)
                data_dict[file] = cds_count
                f.close()
        self.generate_log_file(data_dict=data_dict)
        print('Created Logs...')

    @staticmethod
    def run_every_day(fun):
        schedule.every(10).seconds.do(fun)
        schedule.every().day.at("11:30").do(fun)
        while 1:
            n = schedule.idle_seconds()
            if n is None:
                break
            elif n > 0:
                time.sleep(n)
            schedule.run_pending()

    @staticmethod
    def run_on(fun, second=None, minutes=1, hour=None):
        if second:
            schedule.every(second).seconds.do(fun)
        elif minutes:
            schedule.every(minutes).minutes.do(fun)
        elif hour:
            schedule.every(hour).hour.do(fun)

        while 1:
            n = schedule.idle_seconds()
            if n is None:
                break
            elif n > 0:
                time.sleep(n)
            schedule.run_pending()


if __name__ == '__main__':
    task = FileMonitorTask()
    task.run_on(task.read_files, minutes=1)
    task.run_every_day(task.read_files)


