from datetime import date, datetime
from os import listdir, mkdir
from os.path import isfile, join
from time import sleep


class Logger(object):
    year, month, day = str(date.today()).split('-')
    last_event = ''

    # Singleton
    def __new__(cls, path='./'):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    # Initialization
    def __init__(self, path='./'):
        self.catalog = [name_file for name_file in listdir('./')]
        self.name_dir = ''.join([alpha for alpha in path if alpha.isalpha() or alpha.isdigit() or alpha == '_'])
        if path != './' and self.name_dir not in self.catalog :
            mkdir(path)

        self.path = f'{path}log_{self.day}.{self.month}.{self.year}'
        open(self.path, 'a', encoding='UTF-8').close()

    def write_log(self, evt):
        # write in new file or write in last file - > 'a'
        with open(self.path, 'a', encoding='UTF-8') as f:
            new_event = f'[{self.__get_date()}] {evt}'
            try:
                f.write(new_event + '\n')
                self.last_event = new_event
            except Exception as e:
                print(e)

    def clear_log(self):
        open(self.path, 'w').close()

    def get_logs(self):
        with open(self.path, 'r', encoding='UTF-8') as f:
            return [log[:-1] for log in f]

    def get_last_event(self):
        return self.last_event

    @staticmethod
    def get_all_logs(path='./'):
        return [name_file for name_file in listdir(path)
                if isfile(join(path, name_file)) and name_file[:3] == 'log']

    # Private get date
    @staticmethod
    def __get_date():
        return datetime.now().strftime('%H:%M:%S')


logger = Logger(path='./test4/')

# Create events
events = [
    'Two roads diverged in a yellow wood',
    'And sorry I could not travel both',
    'And be one traveler, long I stood',
    'And looked down one as far as I could',
    'To where it bent in the undergrowth',
    'Then took the other, as just as fair',
    'And having perhaps the better claim',
    'Because it was grassy and wanted wear',
    'Though as for that the passing there',
    'Had worn them really about the same'
]

# Imitation of events
for event in events:
    sleep(.3)
    logger.write_log(event)

print(f'Get logs: \n{logger.get_logs()}\n')
print(f'Last event: \n{logger.get_last_event()}\n')
print(f'All log files: \n{logger.get_all_logs()}\n')

#logger.clear_log()
#print(f'Clear file: {logger.get_logs()}\n')

new_logger = Logger()
print('Singleton:')
print(f'{logger}')
print(f'{new_logger}')
# logger <__main__.Logger object at 0x000001D2FF723C40>
# new_logger <__main__.Logger object at 0x000001D2FF723C40>
