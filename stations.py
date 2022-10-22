class Station:

    def __init__(self, line, zone):
        self.line = line
        self.zone = zone

#create an instance of the class Station for each station
pizarra = Station(1, 4)
alora = Station(1, 3)
alamo = Station(1, 3)
lomas = Station(1, 2)
torrox = Station(1, 1)
centro = Station(1, 0)
col = Station(2, 1)
david = Station(2, 2)
plaza_mayor = Station(2, 3)
lima = Station(2, 3)
prados = Station(2, 4)
fuengirola = Station(2, 4)

#all stations in alphabetical order
stations = [alamo, alora, centro, col, david, fuengirola, lima, lomas, pizarra, plaza_mayor, prados, torrox]

def generateFares(stations):
    #create empty fares matrix with all values initialized to 0
    fares = [[0 for i in range(11)] for k in range(11)]

    #loop through each station
    for i in range(0, len(stations)-1):
        
        #for every other station, check whether it is on the same line and
        #calculate the fares using the zones accordingly
        for k in range(i+1, len(stations)-1):
            if stations[i].line == stations[k].line:
                fares[i][k] = 1 + abs(stations[i].zone - stations[k].zone)
            else:
                fares[i][k] = 1 + stations[i].zone + stations[k].zone               

            #fare will be the same both ways between stations
            fares[k][i] = fares[i][k]

    return fares

        
fares = generateFares(stations)
for row in fares:
    print(row)
