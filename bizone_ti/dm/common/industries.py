import enum


class Industries(enum.Enum):
    other = "Other"
    construction = "Construction"
    agriculture = "Agriculture"
    energy = "Energy"
    culture = "Culture"
    education = "Education"
    engineering = "Engineering"
    entertainment = "Entertainment"
    e_commerce = "E-commerce"
    finance = "Finance"
    government = "Government"
    healthcare = "Healthcare"
    it = "IT"
    insurance = "Insurance"
    manufacturing = "Manufacturing"
    media = "Media"
    public_services = "Public+Services"
    resources = "Resources"
    retail = "Retail"
    science = "Science"
    sport = "Sport"
    telecommunications = "Telecommunications"
    tourism = "Tourism"
    transport = "Transport"

    @classmethod
    def _missing_(cls, value: str) -> str:
        # Note. This method is used to find lowercase name of enum.Enum
        # instances

        value = value.lower()
        value = value.replace('-', '_').replace('+', '_').replace(' ', '_')

        if value in cls._member_map_.keys():
            return cls._member_map_[value]
        return super()._missing_(value)
