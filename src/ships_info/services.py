from .models import ShipData, ShipTypes, PiancShips, DimensionsCorrelation

def find_ships_parameters():
    # function looks for the min, average and max parameters of the khown ships in the database
    list_of_ship_types = ShipTypes.objects.all()
    result_data = {}
    for ship_type in list_of_ship_types:
        ship_data = list(ShipData.objects.filter(ship_type=ship_type))
        if len(ship_data) > 0:
            ship_zero = ship_data[0]
            result_data[ship_type.name] = {
                "deadweight" : [ship_zero.deadweight, ship_zero.deadweight],
                "length" : [ship_zero.length, ship_zero.length],
                "width" : [ship_zero.width, ship_zero.width],
                "depth" : [ship_zero.depth, ship_zero.depth],
            }
            for i in range(1, len(ship_data)):
                if ship_data[i].deadweight < result_data[ship_type.name]["deadweight"][0]:
                    result_data[ship_type.name]["deadweight"][0] = round(ship_data[i].deadweight, 1)
                if ship_data[i].deadweight > result_data[ship_type.name]["deadweight"][1]:
                    result_data[ship_type.name]["deadweight"][1] = round(ship_data[i].deadweight, 1)

                if ship_data[i].length < result_data[ship_type.name]["length"][0]:
                    result_data[ship_type.name]["length"][0] = round(ship_data[i].length, 1)
                if ship_data[i].length > result_data[ship_type.name]["length"][1]:
                    result_data[ship_type.name]["length"][1] = round(ship_data[i].length, 1)

                if ship_data[i].width < result_data[ship_type.name]["width"][0]:
                    result_data[ship_type.name]["width"][0] = round(ship_data[i].width, 1)
                if ship_data[i].width > result_data[ship_type.name]["width"][1]:
                    result_data[ship_type.name]["width"][1] = round(ship_data[i].width, 1)

                if ship_data[i].depth < result_data[ship_type.name]["depth"][0]:
                    result_data[ship_type.name]["depth"][0] = round(ship_data[i].depth, 1)
                if ship_data[i].depth > result_data[ship_type.name]["depth"][1]:
                    result_data[ship_type.name]["depth"][1] = round(ship_data[i].depth, 1)
    return result_data

def sort_by_distance(datalist):
    # function sorts list of data according to the distance from the searched data
    n = len(datalist)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if datalist[j][0] > datalist[j + 1][0]:
                datalist[j], datalist[j + 1] = datalist[j + 1], datalist[j]
                already_sorted = False
        if already_sorted:
            break
    return datalist

def find_closest_pianc_ship(ships_type, parameter, value):
    # function looks for the parameters of the ships according to PIANC spreadsheet
    pianc_ships = list(PiancShips.objects.filter(ship_type=ships_type))
    final_list_of_ships = []
    for ship in pianc_ships:
        if parameter == "deadweight":
            var_distance = abs(ship.deadweight - value)
        elif parameter == "length":
            var_distance = abs(ship.length - value)
        elif parameter == "width":
            var_distance = abs(ship.width - value)
        elif parameter == "depth":
            var_distance = abs(ship.depth - value)
        final_list_of_ships.append([var_distance, ship])
    sorted_final_list = sort_by_distance(final_list_of_ships)
    result = {
        "deadweight" : sorted_final_list[0][1].deadweight,
        "ship_class" : sorted_final_list[0][1].ship_class_name,
        "length" : sorted_final_list[0][1].length,
        "width" : sorted_final_list[0][1].width,
        "depth" : sorted_final_list[0][1].depth,
    }
    return result

def find_ships_parameters_according_to_stat(ships_type, dwt):
    length_koef = DimensionsCorrelation.objects.get(ship_type=ships_type, parameter="length").a_value
    width_koef = DimensionsCorrelation.objects.get(ship_type=ships_type, parameter="width").a_value
    depth_koef = DimensionsCorrelation.objects.get(ship_type=ships_type, parameter="depth").a_value
    result = {
        "deadweight" : dwt,
        "length" : round(length_koef * dwt ** (1/3),1),
        "width" : round(width_koef * dwt ** (1/3),1),
        "depth" : round(depth_koef * dwt ** (1/3),1),
    }
    return result

def create_linear_chart(ships_type):
    length_koef = DimensionsCorrelation.objects.get(ship_type=ships_type, parameter="length").a_value
    width_koef = DimensionsCorrelation.objects.get(ship_type=ships_type, parameter="width").a_value
    depth_koef = DimensionsCorrelation.objects.get(ship_type=ships_type, parameter="depth").a_value
    result = []
    for i in range(1,500):
        dwt = i * 1000
        length = round(length_koef * dwt ** (1/3),1)
        width = round(width_koef * dwt ** (1/3),1)
        depth = round(depth_koef * dwt ** (1/3),1)
        result.append([dwt, length, width, depth])
    return result

def find_closest_ships(ships_type, parameter, value, spread):
    # function looks for the list of ships with closest parameters
    initial_list_of_ships = ShipData.objects.filter(ship_type=ships_type)
    final_list_of_ships = []
    found_ships = []
    for ship in initial_list_of_ships:
        if parameter == "deadweight":
            var_distance = abs(ship.deadweight - value)
        elif parameter == "length":
            var_distance = abs(ship.length - value)
        elif parameter == "width":
            var_distance = abs(ship.width - value)
        elif parameter == "depth":
            var_distance = abs(ship.depth - value)
        if var_distance / value <= spread / 100 and ship.imo not in found_ships:
            final_list_of_ships.append([var_distance, ship])
            found_ships.append(ship.imo)
    sorted_final_list = sort_by_distance(final_list_of_ships)
    return sorted_final_list