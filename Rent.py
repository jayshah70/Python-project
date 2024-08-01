class Rent_Calculation:
    def __init__(self, rent, food, electricity_spend, charge_unit, person):
        self.rent = rent
        self.food = food
        self.electricity_spend = electricity_spend
        self.charge_unit = charge_unit
        self.person = person

    def calculate_rate(self):
        electricity_bill = (self.electricity_spend * self.charge_unit)
        total_rent = int((self.rent + self.food + electricity_bill) / self.person)
        return f"Each Person will pay {total_rent}"

rc = Rent_Calculation(5000, 2500, 100, 8, 3)
rent = rc.calculate_rate()
print(rent)

