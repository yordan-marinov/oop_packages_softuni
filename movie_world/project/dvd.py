from datetime import datetime


class DVD:
    def __init__(
        self,
        name: str,
        id: int,
        creation_year: int,
        creation_month: str,
        age_restriction: int,
    ):
        self.name: str = name
        self.id: int = id
        self.creation_year: int = creation_year
        self.creation_month: str = creation_month
        self.age_restriction: int = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        date_object = datetime.strptime(date, "%d.%m.%Y").date()
        date_str = datetime.strftime(date_object, "%d %B %Y")
        _ , month, year = date_str.split()
        return cls(name, id, int(year), month, age_restriction)

    def is_rented_dvd_repr(self):
        if self.is_rented:
            return "rented"
        return "not rented"

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {self.is_rented_dvd_repr()}"
     