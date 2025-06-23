from abc import ABC, abstractmethod


class Device(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass


class SonyTV(Device):

    def turn_on(self):
        print("Sony TV: Turning on")

    def turn_off(self):
        print("Sony TV: Turning off")

    def set_state(self, channel):
        print(f"Sony TV: Setting channel to {channel}")


class SamsungTV(Device):

    def turn_on(self):
        print("Samsung TV: Turning on")

    def turn_off(self):
        print("Samsung TV: Turning off")

    def set_state(self, channel):
        print(f"Samsung TV: Setting channel to {channel}")


class PhilipsLight(Device):

    def turn_on(self):
        print("Philips Light: Turning on")

    def turn_off(self):
        print("Philips Light: Turning off")

    def set_state(self, brightness):
        print(f"Philips Light: Setting brightness to {brightness}")


class IKEALight(Device):

    def turn_on(self):
        print("IKEA Light: Turning on")

    def turn_off(self):
        print("IKEA Light: Turning off")

    def set_state(self, brightness):
        print(f"IKEA Light: Setting brightness to {brightness}")


class RemoteControl:

    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_state(self, state):
        self.device.set_state(state)


def main():
    sony_tv = SonyTV()
    samsung_tv = SamsungTV()
    philips_light = PhilipsLight()
    ikea_light = IKEALight()

    remote_for_sony = RemoteControl(sony_tv)
    remote_for_samsung = RemoteControl(samsung_tv)
    remote_for_philips = RemoteControl(philips_light)
    remote_for_ikea = RemoteControl(ikea_light)

    remote_for_sony.turn_on()
    remote_for_sony.set_state("HBO")
    remote_for_sony.turn_off()

    remote_for_samsung.turn_on()
    remote_for_samsung.set_state("CNN")
    remote_for_samsung.turn_off()

    remote_for_philips.turn_on()
    remote_for_philips.set_state("75%")
    remote_for_philips.turn_off()

    remote_for_ikea.turn_on()
    remote_for_ikea.set_state("50%")
    remote_for_ikea.turn_off()


if __name__ == "__main__":
    main()
