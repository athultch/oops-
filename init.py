class Computer:
    def __init__(self,cpu,ram,storge):
        self.cpu =cpu
        self.ram =ram
        self.storge =storge

    def start(self):
        print(self.cpu , self.ram , self.storge)

lenovo = Computer("i7 ", "16gb" , "1tb")

dell   = Computer("i9 ", "62 ", "2tb ") 
        
lenovo.start()
dell.start()