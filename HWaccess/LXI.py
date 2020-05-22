from vxi11 import vxi11


class lxi:
    def __init__(self, ip: str):
        self.device = vxi11.Instrument(ip)
        self.device.open()
        pass

    def ask(self, cmd:str):
        """

        :param cmd: cmd in string
        :return: answer, 0 if OK, else exception, -1
        """
        try:
            answer = self.device.ask(cmd)
            return answer, 0
        except Exception as ex:
            return str(ex), -1
        pass

    def write(self, cmd:str):
        """

        :param cmd: cmd string
        :return: None, 0, if ok, else - None, -1
        """
        try:
            self.device.write(cmd)
            return None, 0
        except Exception as ex:
            return str(ex), -1
        pass