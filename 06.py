from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def read_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        try:
            with open(self.file_path, 'r') as file_obj:  # Изменено f на file_obj
                return file_obj.read()
        except FileNotFoundError:
            return "Файл не найден."


class DatabaseDataSource:

    def __init__(self, connection_string):
        self.connection_string = connection_string

    def fetch_data(self):
        return f"Данные из базы данных с подключением: {self.connection_string}"


class DatabaseAdapter(DataSource):
    def __init__(self, database_source):
        self.database_source = database_source

    def read_data(self):
        return self.database_source.fetch_data()


def main():
    with open("data.txt", "w") as file_obj:  # Изменено f на file_obj
        file_obj.write("Это данные из текстового файла.")

    file_source = FileDataSource("data.txt")
    print(file_source.read_data())

    database_source = DatabaseDataSource("database_connection_string")
    database_adapter = DatabaseAdapter(database_source)
    print(database_adapter.read_data())


if __name__ == "__main__":
    main()
