from vxi11 import vxi11
from HWaccess.USBTMC import USBTMC


class Device:
    def __init__(self):
        self.device = None
        pass

    def init_device(self, mode, port):
        """

        :param mode: 0 - lxi, 1 - rs232, 2 - usbtmc
        :param port: ip, rs232 or usbtmc ports
        :return:
        """
        idn = None
        status = -1
        if mode == 0:
            self.device = lxi(port)
            idn = self.device.ask("*idn?")
            status = 0
        elif mode == 2:
            self.device =USBTMC(port)
            idn = str(self.device.getName())
            status = 0
        elif mode == 1:
            print("not implemented yet!")
            idn = None
            status = -1
            pass
        else:
            idn = None
            status = -1
        return idn, status


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

    def getName(self):
        name = self.device.ask("*idn?")
        return name
        pass

    def sendReset(self):
        self.device.write("*rst")
        pass
