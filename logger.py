class logger:
    def __init__(self):
        self.logfile = open("GamePack.log", "w")  # open logfile for writing

    def log(self, error):
        try:
            # add error to log file
            self.logfile.write(f"error in {self.game}:\n{error}\n")
        except Exception as e:
            # add error to log file
            self.logfile.write(
                f"error in logger (ironic!): Failed to add log to logfile, exception:\n{e}\n")

    def exit(self):
        self.logfile.close()  # save and close file
