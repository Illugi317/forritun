class Employee:
    
    def __init__(self, name) -> None:
        self.__name = name

    def weekly_pay(self):
        return 0

    def get_name(self):
        return self.__name

class HourlyEmployee(Employee):

    def __init__(self, name, hourly_pay) -> None:
        super().__init__(name)
        self.__hourly_rate = hourly_pay

    def weekly_pay(self, hours):
        normal_hours = min(hours, 40)
        bonus_hours = max(0, hours - 40)

        return normal_hours * self.__hourly_rate + bonus_hours * self.__hourly_rate * 1.5

class SalariedEmployee(Employee):

    def __init__(self, name, annual_salary) -> None:
        super().__init__(name)
        self.__annual_salary = annual_salary

    def weekly_pay(self, hours):
        return self.__annual_salary / 52

class Manager(Employee):

    def __init__(self, name, annual_salary, weekly_bonus) -> None:
        super().__init__(name)
        self.__annual_salary = annual_salary
        self.__weekly_bonus = weekly_bonus
    
    def weekly_pay(self, hours):
        return (self.__annual_salary / 52) + self.__weekly_bonus
        