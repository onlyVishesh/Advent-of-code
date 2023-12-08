import fileinput
fields = ["seeds","seedToSoil","soilToFertilizer","fertilizerToWater","waterToLight","lightToTemperature","temperatureToHumidity","humidityToLocation"]
dataArray = []
data = {}
for line in fileinput.input(files ='Advent of code solution/Day 5: If You Give A Seed A Fertilizer/test cases.txt'):
  line = str(line)[:-1]
  dataArray.append(line)

j = 0
arr=[]

for i in dataArray:
  if(i!=""):
    arr.append([i])
  else:
    data[fields[j]] = arr
    j+=1
    arr=[]
seeds=[]
seeds = map(int, data["seeds"][0][0].split()[1:])
seeds = list(seeds)
data.pop("seeds")
for keys in data:
  data[keys] = data[keys][1:]
  
# print(data)

seed_soil = {}
def seedToSoil(soil,seed,num,):
  for i in range(0,num):
    seed_soil[seed+i] = soil+i

soil_fertilizer = {}
def soilToFertilizer(fertilizer,soil,num):
  for i in range(0,num):
    soil_fertilizer[soil+i] = fertilizer+i

fertilizer_water = {}
def fertilizerToWater(water,fertilizer,num):
  for i in range(0,num):
    fertilizer_water[fertilizer+i] = water+i

water_light = {}
def waterToLight(light,water,num,):
  for i in range(0,num):
    water_light[water+i] = light+i

light_temperature = {}
def lightToTemperature(temp,light,num,):
  for i in range(0,num):
    light_temperature[light+i] = temp+i

temperature_humidity = {}
def temperatureToHumidity(humidity,temp,num,):
  for i in range(0,num):
    temperature_humidity[temp+i] = humidity+i

humidity_location = {}
def humidityToLocation(loc,humidity,num,):
  for i in range(0,num):
    humidity_location[humidity+i] = loc+i

for key in data:
  if(key == fields[1]):
    for j in data[key]:
      a,b,c = map(int, j[0].split())
      seedToSoil(a,b,c)
  elif(key == fields[2]):
    for j in data[key]:
      a,b,c = map(int, j[0].split())
      soilToFertilizer(a,b,c)
  elif(key == fields[3]):
    for j in data[key]:
      a,b,c = map(int, j[0].split())
      fertilizerToWater(a,b,c)
  elif(key == fields[4]):
    for j in data[key]:
      a,b,c = map(int, j[0].split())
      waterToLight(a,b,c)
  elif(key == fields[5]):
    for j in data[key]:
      a,b,c = map(int, j[0].split())
      lightToTemperature(a,b,c)
  elif(key == fields[6]):
    for j in data[key]:
      a,b,c = map(int, j[0].split())
      temperatureToHumidity(a,b,c)
  elif(key == fields[7]):
    for j in data[key]:
      a,b,c = map(int, j[0].split())
      humidityToLocation(a,b,c)


def mapping(value,dict):
  if(dict.get(value) != None):
    return dict.get(value)
  else:
    return value 

def chainMapping(value):
  # print(value)
  value=mapping(value,seed_soil)
  # print(value)
  value=mapping(value,soil_fertilizer)
  # print(value)
  value=mapping(value,fertilizer_water)
  # print(value)
  value=mapping(value,water_light)
  # print(value)
  value=mapping(value,light_temperature)
  # print(value)
  value=mapping(value,temperature_humidity)
  # print(value)
  value=mapping(value,humidity_location)
  # print(value)
  return value

# print(seed_soil)
# print(soil_fertilizer)
# print(fertilizer_water)
# print(water_light)
# print(light_temperature)
# print(temperature_humidity)
# print(humidity_location)
# print(seeds)

def main():
  min = chainMapping(seeds[0])
  for i in seeds:
    if(min>chainMapping(i)):
      min = chainMapping(i)
  print(min)

if __name__ == "__main__":
  main()
