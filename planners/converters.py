import datetime as dt


class DateConverter:
    regex = "\d{4}-\d{1,2}-\d{1,2}"
    format = "%Y-%m-%d"

    def to_python(self, value):
        return dt.datetime.strptime(value, self.format).date()

    def to_url(self, value):
        if isinstance(value, str):
            return value

        return value.strftime(self.format)