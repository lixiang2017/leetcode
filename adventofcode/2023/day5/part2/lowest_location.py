import os

path = os.path.join(os.path.dirname(__file__), "input1")

# range pairs
seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []


def get_map_data(f):
    data = []
    while True:
        line = f.readline().strip()
        if line and line[0].isdigit():
            # three numbers: the destination range start, the source range start, and the range length.
            destination, source, length = list(map(int, line.split()))
            data.append([destination, source, length])
        else:
            break 
    return data 

with open(path) as f:
    line = f.readline()
    if line.startswith('seeds:'):
        seeds = list(map(int, line.split(":")[1].split()))
    
    while line and not line.startswith("seed-to-soil map:"):
        line = f.readline()
    seed_to_soil = get_map_data(f)
    
    while line and not line.startswith("soil-to-fertilizer map:"):
        line = f.readline()
    soil_to_fertilizer = get_map_data(f)
    
    while line and not line.startswith("fertilizer-to-water map:"):
        line = f.readline()
    fertilizer_to_water = get_map_data(f)

    while line and not line.startswith("water-to-light map:"):
        line = f.readline()
    water_to_light = get_map_data(f)
    
    while line and not line.startswith("light-to-temperature map:"):
        line = f.readline()
    light_to_temperature = get_map_data(f)
    
    while line and not line.startswith("temperature-to-humidity map:"):
        line = f.readline()
    temperature_to_humidity = get_map_data(f)
    
    while line and not line.startswith("humidity-to-location map:"):
        line = f.readline()
    humidity_to_location = get_map_data(f)

print(seed_to_soil)
print(soil_to_fertilizer)
print(fertilizer_to_water)
print(water_to_light)
print(light_to_temperature)
print(temperature_to_humidity)
print(humidity_to_location)

def mapping(seeds, m):
    new_seeds = set()
    for s in seeds:
        found = False
        for destination, source, length in m:
            if source <= s < source + length:
                delta = s - source 
                new_seeds.add(destination + delta)
                found = True 
                break
        if not found:
            new_seeds.add(s)
    return new_seeds

print('seeds ', seeds)
range_pairs = seeds[:]
seeds = []
for i in range(0, len(range_pairs), 2):
    start, length = range_pairs[i], range_pairs[i + 1]
    seeds.extend(range(start, start + length))

for m in [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]:
    seeds = mapping(seeds, m)

print('ans ', min(seeds)) # 46