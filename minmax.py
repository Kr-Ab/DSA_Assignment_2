from msilib.schema import Class


class MinMax:
    data = []

    #initialising the array 
    def __init__(self, sample):
        self.data = sample.copy()

    

    #function to get the minimum and maximum value and their respective indexes from the array
    def getminmax(self, start, end, min, max):
        min_ndx = max_ndx = 0
        #if only one element exists
        if start == end:
            min = max = self.data[start]
            min_ndx = max_ndx = start
        else:
            mid = start + ((end - start) // 2)
            #recursion by dividing the array  
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

        #returning minimum value , maximum value , minimum value index , maximum value index
        return [min, max, min_ndx, max_ndx]

    #function to write the output on the file
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


#main with input error handling
if __name__ == '__main__':
    try:
        #opening the output file
        f = open("outputPS1.txt", "w")
        #opening the input file
        with open("inputPS1.txt", 'r') as input:
            for line in input:
                try: 
                    sample = list(map(int, line.split()))
                except: #Inputs apart from integer array
                    f.write("Invalid Input \n")
                    continue
                if len(set(sample))==1: # single value input
                    f.write("Only one number found. Cannot distinguish between distributions \n")
                    continue
                if len(sample)==0:# no Value entered
                    f.write("Empty Input Array \n")
                    continue
                minmax = MinMax(sample)

                #writing the output to the file
                f.write(minmax.getoutput(minmax.getminmax(
                    0, len(sample)-1, float('inf'), float('-inf'))))
                f.write("\n")

        # closing the file
        f.close()

    except Exception as e:
        print("Error", e)
