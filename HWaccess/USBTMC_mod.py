import usbtmc
class USBTMC:
    def __init__(self, device):
        self.device = usbtmc.Instrument(device)
        pass

    @staticmethod
    def get_devices(self):
        """
        returns alist with usbtmc devices
        (Windows only version)

        :return:
        """
        return usbtmc.list_devices()

    def write(self, command):
        try:
            self.device.write(command)
            return None, 0
        except Exception as ex:
            return str(ex), -1
            pass

    def read(self, length=4000):
        '''

        :param length: length of data to read
        :return:
        '''
        return self.device.read_raw(length)

    def close(self):
        self.device.close()

    def ask(self, cmd, sleep=0, length=4000):
        """
        Imitates vxi11 ask command, therefore returns a string
        :param cmd:
        :return:
        """
        a = self.device.ask_raw(cmd, length)
        return str(a.decode('utf-8'))

