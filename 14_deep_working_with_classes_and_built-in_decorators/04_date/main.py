class Date:
    def __init__(self, day: int = None, month: int = None, year: int = None) -> None:
        self._day = day
        self._month = month
        self._year = year

    def __str__(self) -> str:
        return f'День: {self._day}\tМесяц: {self._month}\tГод: {self._year}'

    @classmethod
    def from_string(cls, str_of_date: str) -> 'Date':
        day = int(str_of_date[:2])
        month = int(str_of_date[3:5])
        year = int(str_of_date[6:])

        return Date(day, month, year)

    @classmethod
    def is_date_valid(cls, str_of_date: str) -> bool:
        date = cls.from_string(str_of_date)

        return 1 <= date._day <= 31 and 1 <= date._month <= 12 and 1 <= date._year


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
