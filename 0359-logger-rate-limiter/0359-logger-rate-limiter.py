class Logger:

    def __init__(self):
        self.hash_map = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hash_map:
            self.hash_map[message] = timestamp + 10
            return True
        elif message in self.hash_map and timestamp >= self.hash_map[message]:
            self.hash_map[message] = timestamp + 10
            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)