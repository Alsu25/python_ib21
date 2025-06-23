class GameSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.volume = 50
            cls._instance.difficulty = "Normal"
        return cls._instance


settings1 = GameSettings()
settings2 = GameSettings()

print(settings1 is settings2)

settings1.volume = 70
settings1.difficulty = "Hard"

print(settings2.volume)
print(settings2.difficulty)
