from print_color import print


class FileBase:
    def __init__(self, filename):
        self.wordlist = self.open(filename)
        self.index = 0
        self.max = len(self.wordlist)

    def open(self, filename):
        try:
            with open(filename) as filehandle:
                return [line.strip('\n') for line in filehandle.readlines()]
        except Exception as e:
            print(e, color='red')
            exit(1)

    def __iter__(self):
        self.index = 0
        return self

    def __len__(self):
        return self.max

    def __next__(self):
        if self.index >= self.max:
            raise StopIteration
        else:
            word = self.wordlist[self.index]
            self.index += 1
            return word
