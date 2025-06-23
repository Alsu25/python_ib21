class LightingSystem:
    def __init__(self):
        self.lights_on = False

    def turn_on(self):
        self.lights_on = True
        return "Освещение включено"

    def turn_off(self):
        self.lights_on = False
        return "Освещение выключено"

    def dim(self):
        self.lights_on = True
        return "Освещение приглушено"

    def get_status(self):
        return f"Освещение: {'Включено' if self.lights_on else 'Выключено'}"


class ClimateControlSystem:
    def __init__(self):
        self.temperature = 20

    def set_temperature(self, temp):
        self.temperature = temp
        return f"Температура установлена на {temp} градусов"

    def get_status(self):
        return f"Температура: {self.temperature} градусов"


class SecuritySystem:
    def __init__(self):
        self.alarm_on = False

    def turn_on(self):
        self.alarm_on = True
        return "Сигнализация включена"

    def turn_off(self):
        self.alarm_on = False
        return "Сигнализация выключена"

    def get_status(self):
        return f"Сигнализация: {'Включена' if self.alarm_on else 'Выключена'}"


class MultimediaSystem:
    def __init__(self):
        self.music_on = False

    def turn_on(self):
        self.music_on = True
        return "Музыка включена"

    def turn_off(self):
        self.music_on = False
        return "Музыка выключена"

    def get_status(self):
        return f"Музыка: {'Включена' if self.music_on else 'Выключена'}"


class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.climate = ClimateControlSystem()
        self.security = SecuritySystem()
        self.multimedia = MultimediaSystem()

    def home_mode(self):
        return [
            self.lighting.turn_on(),
            self.climate.set_temperature(22),
            self.security.turn_off(),
        ]

    def away_mode(self):
        return [
            self.lighting.turn_off(),
            self.security.turn_on(),
            self.multimedia.turn_off(),
        ]

    def party_mode(self):
        return [
            self.lighting.dim(),
            self.climate.set_temperature(24),
            self.multimedia.turn_on(),
        ]

    def night_mode(self):
        return [
            self.lighting.turn_off(),
            self.climate.set_temperature(18),
            self.security.turn_on(),
        ]

    def get_all_systems_status(self):
        return [
            self.lighting.get_status(),
            self.climate.get_status(),
            self.security.get_status(),
            self.multimedia.get_status(),
        ]


def main():
    print("=== Тестирование паттерна Фасад для умного дома ===")

    smart_home = SmartHomeFacade()

    print("\n1. Начальное состояние всех систем:")
    print(smart_home.get_all_systems_status())

    print("\n2. Активация режима 'Я дома':")
    home_results = smart_home.home_mode()
    for result in home_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я дома':")
    print(smart_home.get_all_systems_status())

    print("\n3. Активация режима 'Вечеринка':")
    party_results = smart_home.party_mode()
    for result in party_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Вечеринка':")
    print(smart_home.get_all_systems_status())

    print("\n4. Активация режима 'Ночь':")
    night_results = smart_home.night_mode()
    for result in night_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Ночь':")
    print(smart_home.get_all_systems_status())

    print("\n5. Активация режима 'Я ухожу':")
    away_results = smart_home.away_mode()
    for result in away_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я ухожу':")
    print(smart_home.get_all_systems_status())

    print("\n=== Тестирование завершено ===")


if __name__ == "__main__":
    main()
