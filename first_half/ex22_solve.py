class SuffixArray():
    def __init__(self, instr):
        self.instr = instr
        lst = []
        for i in range(0, len(instr)):
            lst.append((instr[i:], i))
        self.sarray = sorted(lst)

    def search(self, what):
        low = 0
        high = len(self.sarray) - 1
        while low <= high:
            mid = (low+high) // 2
            val, i = self.sarray[mid]
            if val == what:
                return mid, i
            elif what > val:
                low = mid + 1
            elif what < val:
                high = mid - 1

        return -1, -1

    def find_shortest(self, match):
        sarray_i, instr_i = self.search(match)
        return instr_i

    def find_longest(self, match):
        sarray_i, instr_i = self.search(match)
        if sarray_i == -1:
            return -1, -1
        test, instr_i = self.array[sarray_i]
        longest, longest_i = test, instr_i
        while test.startswith(match):
            if len(longest) < test:
                longest, longest_i = test, instr_i
            try:
                sarray_i += 1
                test, instr_i = self.array[sarray_i]
            except IndexError:
                break

        return longest, longest_i

    def find_all(self, match):
        sarray_i, inst_i = self.search(match)
        if sarray_i == -1: return -1, -1

        test, instr_i = self.sarray[sarray_i]
        results = []

        while test.startswith(match):
            results.append((test, instr_i))
            sarray_i += 1

            try:
                test, instr_i = self.sarray[sarray_i]
            except IndexError:
                break

        return results
























