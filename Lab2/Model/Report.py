class Report:
    def __init__(self, number, title, body, date):
        self._number_of_report = number
        self._title = title
        self._body = body
        self._date = date

    @property
    def title(self):
        return self._title

    @property
    def body(self):
        return self._body

    @property
    def date(self):
        return self._date
