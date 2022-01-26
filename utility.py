import os


class FileMonitor(object):
    def __init__(self, store_path, log_path):
        self._FILE_STORE_PATH = store_path
        self._FILE_LOG_PATH = log_path
        self.create_folders()

    def create_folders(self):
        if not os.path.exists(self._FILE_STORE_PATH):
            os.makedirs(self._FILE_STORE_PATH)
        if not os.path.exists(self._FILE_LOG_PATH):
            os.makedirs(self._FILE_LOG_PATH)
