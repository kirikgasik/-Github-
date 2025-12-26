class DatabaseConfig:
    _instance = None  
    def __new__(cls, db_name=None, user=None, password=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db_name = db_name
            cls._instance.user = user
            cls._instance.password = password
        return cls._instance
conf1 = DatabaseConfig("shop_db", "admin", "123")
conf2 = DatabaseConfig("users_db", "root", "000")
print(conf1 is conf2)      
print(conf2.db_name)       
class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_history = []
        return cls._instance
    def log(self, message):
        self.log_history.append(message)
logger1 = Logger()
logger2 = Logger()
logger1.log("Система запущена")
logger2.log("Пользователь вошел")
print(logger1.log_history) 
print(logger1 is logger2)  
