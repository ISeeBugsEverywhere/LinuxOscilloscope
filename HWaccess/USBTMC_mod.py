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

