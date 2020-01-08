class FloridaHurricaneFind:
    def __init__(self):
        #this list containts name, if hurricane made landfall in florida, windspeed and date of landfall,
        #new data is appended to list for each new hurricane
        self.hurList = []

    def analyze(self,data):
        #if current row is a new hurricane, add new entry to hurList and exit
        if len(data) == 4:
            self.hurList.append([data[1].strip(),False,0,0])
            return
    
        #exit if date is < 1900
        elif int(data[0]) < 19000000:
            return
        
        #if program hasn't detected the hurricane in florida yet check lat/lng
        elif not self.hurList[-1][1]:
            self.latitude = float(data[4][:-1].strip())
            self.longitude = float(data[5][:-1].strip())
            self.latHem = data[4][-1].strip()
            self.lngHem = data[5][-1].strip()

            #if hurricane made landfall in Florida set flag in hurList to true
            #also set date of landfall
            if data[2].strip() == "L" and 24.39 <= self.latitude <= 31 and 79.81 <= self.longitude <= 87.63 and self.latHem == "N" and self.lngHem == "W":
                self.hurList[-1][1] = True
                self.hurList[-1][3] = "{}-{}-{}".format(data[0][:4],data[0][4:6],data[0][6:])

        #update max windspeed if it's greater than existing speed
        if int(data[6].strip()) > self.hurList[-1][2]:
            self.hurList[-1][2] = int(data[6].strip())
        return

    def floridaHurricaneFind(self,file):
        #reads in data row by row and analyzes
        with open(file) as hurdat:
            for row in hurdat:
                self.data = row.split(",")
                self.analyze(self.data)
            hurdat.close()
        
        #after data is anaylzed, write output to file
        with open("output.txt","w+") as output: 
            output.write("Name, Windspeed (knots), Date(YYY-MM-DD)\n")
            for row in self.hurList:
                if row[1]:
                    self.line = "{}, {}, {}\n".format(row[0],row[2],row[3])
                    output.write(self.line)
            output.close()
        return