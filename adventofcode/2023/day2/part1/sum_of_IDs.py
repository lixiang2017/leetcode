import os 

path = os.path.join(os.path.dirname(__file__), 'input')
ans = 0
red_limit, green_limit, blue_limit = 12, 13, 14
with open(path) as f:
    for line in f:
        if line.startswith("Game"):
            game_id, records = line.strip().split(":")
            game, _id = game_id.split()
            red = green = blue = 0
            for record in records.split(";"):
                for item in record.split(","):
                    number, color = item.split()
                    if "red" == color:
                        red = max(red, int(number))
                    elif "green" == color:
                        green = max(green, int(number))
                    elif "blue" == color:
                        blue = max(blue, int(number))
                        
            if red <= red_limit and green <= green_limit and blue <= blue_limit:
                ans += int((_id))

print('ans ', ans)  # 2331