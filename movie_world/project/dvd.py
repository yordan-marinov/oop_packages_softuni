class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name: str = name
        self.id: int = id
        self.creation_year: int = creation_year
        self.creation_month: str = creation_month
        self.age_restriction: int = age_restriction
        self.is_rented: bool = False

    def is_rented_dvd_repr(self):
        if self.is_rented:
            return "rented"
        return "not rented"

    def __repr__(self):
        return f"{self.id}: {self.name} " \
               f"({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. " \
               f"Status: {self.is_rented_dvd_repr()}"

    @staticmethod
    def string_repr_of_month(month) -> str:
        months = {
            "1": "January",
            "2": "February",
            "3": "March",
            "4": "April",
            "5": "May",
            "6": "June",
            "7": "July",
            "8": "August",
            "9": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }
        return months[month]

    @staticmethod
    def split_date(date: str):
        date = date.split(".")
        creation_year_from_split = int(date[2])
        creation_month_from_split = DVD.string_repr_of_month(date[1])
        return creation_year_from_split, creation_month_from_split

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        creation_year, creation_moth = cls.split_date(date)
        return cls(name, id, creation_year, creation_moth, age_restriction)
