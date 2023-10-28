class SuffixArray():
    def __init__(self, instr):
        self.instr = instr
        self.list = []
        for i in range(0, len(self.instr)):
            self.list.append(self.instr[i:])
        self.list = sorted(self.list)

    def find_all(self, begin):
        tem_list = []
        leng = len(begin)
        for item in self.list:
            try:
                if begin == item[:leng]:
                    tem_list.append(item)
            except:
                pass
        return tem_list


    def find_shortest(self, begin):
        tem_list = self.find_all(begin)
        if len(tem_list) < 1:
            print('No substring founded.')
        else:
            shortest_str = tem_list[0]
            shortest = len(shortest_str)
            for i in tem_list:
                if len(i) < shortest:
                    shortest_str = i
            return shortest_str

    def find_longest(self, begin):
        tem_list = self.find_all(begin)
        if len(tem_list) < 1:
            print('No substring founded.')
        else:
            longest_str = tem_list[0]
            longest = len(longest_str)
            for i in tem_list:
                if len(i) > longest:
                    longest_str = i
            return longest_str
    
