from datetime import datetime

class DateConverter:
    regex = '[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'

    format ="%Y-%m-%d"

    def to_python(self, value:str) -> datetime.date:
        # print(3333333333, datetime.strptime(value, self.format)).date()
        return datetime.strptime(value, self.format).date()

    def to_url(self, value:datetime.date) -> str:
        print(222222222222, value, type(value))
        return value.strftime(self.format)