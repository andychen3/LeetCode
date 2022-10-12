class Logger:

    def __init__(self):
        self.hash = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hash:
            self.hash[message] = timestamp
            return True
        if timestamp - self.hash[message] >= 10:
            self.hash[message] = timestamp
            return True
        else:
            return False

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)