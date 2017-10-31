class c_file_info:
    chars       = 0
    lines       = 0
    filename    = ""

    def __init__(self):
        self.filename = ""

    def set_filename(self, filename):
        self.filename = filename

    def get_chars(self):
        return self.chars
    
    def get_lines(self):
        return self.lines

    def counter(self):
        chars = 0
        lines = 0
        with open(self.filename) as f:
            for line in f:
                chars += len(f.readline())
                #chars += len(line)
                lines += 1
            #lines = len(f.readlines())
        self.lines = lines
        self.chars = chars
