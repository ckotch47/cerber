from progress.bar import IncrementalBar


class ProgressBarBase:
    progress_bar: IncrementalBar

    def __init__(self, max_len: int, name: str = 'progress'):
        self.progress_bar = IncrementalBar(name, max=max_len, color='cyan')

    def __next__(self):
        self.progress_bar.next()

    def __del__(self):
        self.progress_bar.finish()

    def new_max(self, max_len: int):
        self.progress_bar.max = max_len
