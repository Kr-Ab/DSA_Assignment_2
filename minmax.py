from msilib.schema import Class


class MinMax:
    data = []

    def __init__(self, sample):
        self.data = sample.copy()

    def getminmax(self, start, end, min, max):
        min_ndx = max_ndx = 0
        if start == end:
            min = max = self.data[start]
            min_ndx = max_ndx = start
        else:
            mid = start + ((end - start) // 2)
            first_half = self.getminmax(start, mid, min, max)
            second_half = self.getminmax(mid + 1, end, min, max)

            if first_half[0] < second_half[0]:
                min = first_half[0]
                min_ndx = first_half[2]
            else:
                min = second_half[0]
                min_ndx = second_half[2]

            if first_half[1] > second_half[1]:
                max = first_half[1]
                max_ndx = first_half[3]
            else:
                max = second_half[1]
                max_ndx = second_half[3]

        return [min, max, min_ndx, max_ndx]

    def getoutput(self, result):
        min = result[0]
        max = result[1]
        min_ndx = result[2]
        max_ndx = result[3]

        if min_ndx not in [0, len(self.data)-1]:
            return "minima " + str(min)

        if max_ndx not in [0, len(self.data)-1]:
            return "maxima " + str(max)

        if min_ndx < max_ndx:
            return "increasing " + str(min)

        if min_ndx > max_ndx:
            return "decreasing " + str(min)


if __name__ == '__main__':
    try:
        f = open("outputPS1.txt", "w")

        with open("inputPS1.txt", 'r') as input:
            for line in input:
                try: 
                    sample = list(map(int, line.split()))
                except:
                    f.write("Invalid Input \n")
                    continue
                if len(set(sample))==1:
                    f.write("Only one number found. Cannot distinguish between distributions \n")
                    continue
                if len(sample)==0:
                    f.write("Invalid Input \n")
                    continue
                minmax = MinMax(sample)

                f.write(minmax.getoutput(minmax.getminmax(
                    0, len(sample)-1, float('inf'), float('-inf'))))
                f.write("\n")

        # closing the file
        f.close()

    except Exception as e:
        print("Error", e)
