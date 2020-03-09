#This is a loom simulator to help me design different patterns for my traditional 4-pulley European upright loom. The pedals are labeled A 1 2 3 4 B

class Loom:

    def __init__(self, thread_count, under=' -', over='- '):
        self._thread_count = thread_count
        self.weaving = self.weave()
        self._over = over
        self._under = under

    @property
    def thread_count(self):
        return self._thread_count

    @thread_count.setter
    def thread_count(self, new_num):
        if type(new_num) is not int:
            raise ValueError("You must enter a number")
        self._thread_count = new_num

    # @property
    # def over(self):
    #     return self._over
    #
    # @over.setter
    # def over(self, new_over):
    #     self._over = new_over
    #
    # @property
    # def under(self):
    #     return self._under
    #
    # @under.setter
    # def under(self, under):
    #     self._under = under

    def A(self):
        a = '- '
        # a = self.over + self.under
        return a*self.thread_count + '\n'

    def B(self):
        # b = self.under + self.over
        b = ' -'
        return b*self.thread_count + '\n'

    def one(self):
        one = '-   '
        return one*(int(self.thread_count/2)) + '\n'

    def two(self):
        two = ' -  '
        return two*(int(self.thread_count/2)) + '\n'

    def three(self):
        three = '  - '
        return three*(int(self.thread_count/2)) + '\n'

    def four(self):
        four = '   -'
        return four*(int(self.thread_count/2)) + '\n'

    def reverse(self):
        return_str = ""
        for i in self.weaving:
            if i == '-':
                return_str += ' '
            if i == ' ':
                return_str += '-'
            if i == '\n':
                return_str += '\n'
        return return_str

    def weave(self):
        usr = ''
        return_str = ""
        print("Type A B 1 2 3 4 to press pedals of your virtual loom; press any other key to stop and see what you've made")
        while usr == "" or usr == "A" or usr == "B" or usr == '1' or usr == '2' or usr == '3' or \
            usr == '4':
            usr = input("what pedal would you like to push? \n")
            if usr == 'A':
                return_str += self.A()
            if usr == 'B':
                return_str += self.B()
            if usr == '1':
                return_str += self.one()
            if usr == '2':
                return_str += self.two()
            if usr == '3':
                return_str += self.three()
            if usr == '4':
                return_str += self.four()
        return return_str

    def __str__(self):
        return self.weaving

if __name__ == "__main__":

    # l = Loom(10)
    # print(l)
    # print(l.reverse())
    l0 = Loom(100)
    print(l0)
    print(l0.reverse())
