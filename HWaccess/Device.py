from HWaccess.USBTMC import USBTMC
from HWaccess.LXI import lxi


class Device:
    def __init__(self):
        self.device = None
        self.locale = 'utf-8'
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

    def ask(self, cmd:str):
        answer, status = self.device.ask(cmd)
        return answer, status
        pass

    def write(self, cmd:str):
        answer, status = self.device.write(cmd)
        return answer, status



