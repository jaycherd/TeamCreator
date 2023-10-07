from member.utility import fxns as utils
from member.utility import constants as csts
from icecream import ic


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


    # Test with an instance of your class
    # member = YourClass(...)  # Replace `YourClass` with the actual name of your class
    # print_member_attributes(member)


    
        



