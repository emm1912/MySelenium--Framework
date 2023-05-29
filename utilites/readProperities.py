import configparser
config = configparser.RawConfigParser()
config.read("./configurations/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationUrl(section, value):
        url= config.get(section, value)
        return url

    @staticmethod
    def getUserEmail(section, value):
        username = config.get(section, value)
        return username

    @staticmethod
    def getUserPassword(section, value):
        password = config.get(section, value)
        return password
