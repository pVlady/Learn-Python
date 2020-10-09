import datetime as dt


class Month:
    """ Class Month : a calendar month of year.
    """

    #---------------------------------------------------------------------------
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.value = 100 * year + month

    #---------------------------------------------------------------------------
    @classmethod
    def Create(cls, month_value):
        """ Create Month using month value.
        """
        year = month_value // 100
        month = month_value - 100 * year
        return cls(year, month)

    #---------------------------------------------------------------------------
    @classmethod
    def month_current(cls):
        return cls(dt.datetime.today().year, dt.datetime.today().month)

    #---------------------------------------------------------------------------
    def is_equal(self, month_other):
        return self.value == month_other.value

    #---------------------------------------------------------------------------
    def add_month(self, month_count=1):
        """ Add mount_count monthes.
        """
        next_year = self.year + (self.month + month_count - 1) // 12
        next_month = (self.month + month_count) % 12
        return Month(next_year, 12 if next_month == 0 else next_month)

    #---------------------------------------------------------------------------
    def add_year(self, year_count=1):
        """ Add year_count years.
        """
        return Month(year_count + self.year, self.month)

    #---------------------------------------------------------------------------
    def diff_months(self, month):
        """ Return month's difference between self and argument.
        """
        return 12 * (self.year - month.year) + self.month - month.month

    #---------------------------------------------------------------------------
    def diff_years(self, month):
        """ Return full years count between self and argument.
        """
        return self.diff_months(month) // 12

    #---------------------------------------------------------------------------
    def as_str(self):
        """ Return string represrntation of self as yyyy-mm format.
        """
        return str(self.year) + '-' + ('0' + str(self.month))[-2:]


# TESTs #
if __name__ == '__main__':
    print('Run tests of class Month\n========================\n')

    m = Month(2020, 8)
    print('self.as_str() ...', ('OK' if m.as_str() == '2020-08' else 'Failed!'))
