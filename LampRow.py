# B
# class LampRow:
#     def __init__(self, row_len=8):
#         self.dict = {'0': '-', '1': '*'}
#         self.__row_len = row_len
#         self.__state = "0"*self.__row_len
#
#     def show(self):
#         for i in self.__state:
#             print(self.dict[i], end="")
#         print()
#
#     def __get_state(self):
#         return self.__state
#
#     def __set_state(self, new_state):
#         if len(new_state) != self.__row_len:
#             self.__state = "0"*self.__row_len
#             print('ошибка')
#         else:
#             self.__state = new_state
#
#     state = property(__get_state, __set_state)
#
#
# lamps = LampRow(6)
# lamps.show()
# lamps.state = "101010"
# print(lamps.state)
# lamps.show()
# lamps.state = "10101010"
# print(lamps.state)
# lamps.show()

# C
# class LampRow:
#     def __init__(self, row_len=8):
#         self.dict = {'0': '-', '1': '*', '2': 'o'}
#         self.__row_len = row_len
#         self.__state = "0"*self.__row_len
#
#     def show(self):
#         for i in self.__state:
#             print(self.dict[i], end="")
#         print()
#
#     def __get_state(self):
#         return self.__state
#
#     def __set_state(self, new_state):
#         if len(new_state) != self.__row_len:
#             self.__state = "0"*self.__row_len
#             print('ошибка')
#         else:
#             self.__state = new_state
#
#     state = property(__get_state, __set_state)
#
#
# lamps = LampRow(6)
# lamps.show()
# lamps.state = "102102"
# print(lamps.state)
# lamps.show()
# lamps.state = "10201010"
# print(lamps.state)
# lamps.show()

class LampRow:
    def __init__(self, row_len=8):
        self.dict = {'0': '-', '1': '*', '2': 'o'}
        self.__row_len = row_len
        self.__state = 0

    def show(self):
        for i in '{:0{}}'.format(self.__state, self.__row_len):
            print(self.dict[i], end="")
        print()

    def __get_state(self):
        return '{:0{}}'.format(self.__state, self.__row_len)

    def __set_state(self, new_state):
        if len(new_state) != self.__row_len:
            self.__state = 0
            print('ошибка')
        else:
            self.__state = int(new_state)

    state = property(__get_state, __set_state)


lamps = LampRow(6)
lamps.show()
lamps.state = "102102"
print(lamps.state)
lamps.show()
lamps.state = "10201010"
print(lamps.state)
lamps.show()
