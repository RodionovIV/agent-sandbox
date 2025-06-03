# Ð ÐµÐ°Ð»Ð¸Ð·Ð°ÑÐ¸Ñ Ð¿Ð°Ð¼ÑÑÐ¸ Ð´Ð»Ñ Ð°Ð³ÐµÐ½ÑÐ°
class Memory:
    def __init__(self):
        self.history = []

    def add(self, message):
        self.history.append(message)

    def get_history(self):
        return self.history
