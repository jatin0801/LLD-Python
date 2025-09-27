class Logger:
    _instance = None  # private class variable

    def __new__(cls):
        if cls._instance is None:  # create only once
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str):
        print(f"Log: {message}")


class Application:
    def run(self):
        # Fetch the single instance of Logger
        logger = Logger()
        logger.log("Application started.")


# Client code
if __name__ == "__main__":
    app = Application()
    app.run()

    # Prove singleton behavior
    logger1 = Logger()
    logger2 = Logger()
    print("Same instance?", logger1 is logger2)  # True
