from datetime import datetime,timedelta

from member.utility import fxns as utils
from member.utility import constants as csts


class Member:
    _id_counter = 0
    def __init__(self,name,avail_matrix,priority):
        self._member_id = Member._id_counter
        Member._id_counter += 1
        # Set name directly since there's no validation for it in your provided code
        self._name = name
        # Validate and set priority
        if not csts.MIN_PRI <= priority <= csts.MAX_PRI:
            raise ValueError(f"Members priority must be between {csts.MIN_PRI} and {csts.MAX_PRI}")
        self._priority = priority
        # Validate and set avail_matrix
        if not utils.check_avail_matrix(avail_matrix):  # Assuming check_avail_matrix is a function that takes avail_matrix as an argument
            raise ValueError("Availabilities contains invalid times, " +
                             "make sure all times are 24Hr format" +
                             "(\"HH:MM\") and between 00:00 to 23:59, also ensure if" +
                             "person has no avail to leave it blank or put N/A")
        self._avail_matrix = avail_matrix
        self._available_minutes = self.generate_available_minutes()

    @property
    def available_minutes(self):
        return self._available_minutes

    #below is a getter, used whenever try to access private attributes
    @property
    def priority(self):
        return self._priority

    @property
    def avail_matrix(self):
        return self._avail_matrix

    @property
    def name(self):
        return self._name
    
    @property
    def member_id(self):
        return self._member_id
    
    # @priority.setter
    # def priority(self,value):
    #     if not csts.MIN_PRI <= value <= csts.MAX_PRI:
    #         raise ValueError(f"Members priority must be between {csts.MIN_PRI} and {csts.MAX_PRI}")
    #     self._priority = value
    
    # @avail_matrix.setter
    # def avail_matrix(self,value):
    #     #error checking to go here
    #     if not utils.check_avail_matrix:
    #         raise ValueError(f"Availabilities contains invalid times")
    #     self._avail_matrix = value
    
    # @name.setter
    # def name(self,value):
    #     self._name = value

    # def print_member_attributes(self):
    #     for attr_name in dir(self):
    #         # Skip special methods and attributes (those starting with '__')
    #         if not attr_name.startswith('__'):
    #             # Skip private attributes that start with a single underscore, since they have a corresponding public property
    #             if not attr_name.startswith('_'):
    #                 value = getattr(self, attr_name)
    #                 if not callable(value):  # Skip methods, only consider attributes
    #                     print(f"{attr_name}: {value}")

    def print_member_attributes(self):
        for attr_name in dir(self):
            # Check if the attribute is a property
            if isinstance(getattr(type(self), attr_name, None), property):
                value = getattr(self, attr_name)
                print(f"{attr_name}: {value}")

    def generate_available_minutes(self):
        avail_minutes_set = set()
        matrix = self._avail_matrix.copy()
        for row in range(len(matrix)):
            for col in range(0,len(matrix[row]),2):
                start_time = datetime.strptime(matrix[row][col],'%H:%M')
                end_time = datetime.strptime(matrix[row][col + 1],'%H:%M')
                for single_date in self.daterange(start_time,end_time):
                    datestr = single_date.strftime("%H:%M")
                    datestr += f"-{row}" #this to track the current day
                    avail_minutes_set.add(datestr)
        # ic(len(avail_minutes_set))
        return avail_minutes_set

    def daterange(self,start_date: datetime,end_date: datetime) -> datetime:
        delta = timedelta(minutes=1)
        current_date = start_date
        while current_date < end_date:
            yield current_date
            current_date += delta

