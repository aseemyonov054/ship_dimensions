import os
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from .models import ShipTypes, ShipData
from .services import find_closest_ships, find_ships_parameters, find_closest_pianc_ship,find_ships_parameters_according_to_stat
from .services import create_linear_chart
from .generate_ship_drawing import draw_ship
from django.utils.translation import get_language

def find_ships_dimensions(request):
    # function gets looks for ships, close to certain dimensions
    if request.method == "GET":
        list_of_ships_type = list(ShipTypes.objects.all())
        parameter_limits_values = find_ships_parameters()
        default_parameters = []
        for ship in list_of_ships_type:
            if ship.name in parameter_limits_values.keys():
                default_parameters = [parameter_limits_values[ship.name]['deadweight'][0],
                                      parameter_limits_values[ship.name]['deadweight'][1]]
                break
        return render(request, "ships_info/find_ships_dim.html", {"list_of_ships_type" : list_of_ships_type,
                                                                  "parameter_limits" : parameter_limits_values,
                                                                  'default_parameters' : default_parameters})
    elif request.method == "POST":
        ships_type_id = request.POST['ships_type']
        ships_type = ShipTypes.objects.get(name=ships_type_id)
        ships_parameter = request.POST['ships_parameter']
        ships_parameter_value = float(request.POST['ships_parameter_value'])
        allowed_spread = float(request.POST['allowed_spread'])
        pianc_ship = find_closest_pianc_ship(ships_type, ships_parameter, ships_parameter_value)
        if ships_parameter == "deadweight":
            stat_ship = find_ships_parameters_according_to_stat(ships_type, ships_parameter_value)
        else:
            stat_ship = None
        linear_data = create_linear_chart(ships_type)
        list_of_ships = find_closest_ships(ships_type, ships_parameter, ships_parameter_value, allowed_spread)
        return render(request, "ships_info/closest_ships_dim.html", {"ships_type" : ships_type,
                                                                     "ships_parameter" : ships_parameter,
                                                                     "ships_parameter_value" : ships_parameter_value,
                                                                    "list_of_ships" : list_of_ships,
                                                                     "pianc_ship" : pianc_ship,
                                                                     "stat_ship" : stat_ship,
                                                                     "linear_data" : linear_data})
    
def generate_drawing(request):
    # function returns technocal drawing of a certain ship
    if request.method == "POST":
        ship_id = int(request.POST['ships_id'])
        ship = ShipData.objects.get(id=ship_id)
        current_language = get_language()
        new_drawing, temp_file = draw_ship(ship.ship_type, ship.deadweight, ship.length, ship.width, ship.depth, current_language)
        response = FileResponse(open(os.getcwd() + "/media/" + temp_file + ".dxf", "rb"))
        os.remove(os.getcwd() + "/media/" + temp_file + ".dxf")
        return response

def generate_drawing_with_numbers(request):
    # function generates drawing according to certain ships' dimensions
    if request.method == "POST":
        ship_name = request.POST['ship_name']
        ship_type = int(request.POST['ship_type'])
        ship_type = ShipTypes.objects.get(id=ship_type)
        ship_deadweight = float(request.POST['ship_deadweight'])
        ship_length = float(request.POST['ship_length'])
        ship_width = float(request.POST['ship_width'])
        ship_depth = float(request.POST['ship_depth'])
        current_language = get_language()
        new_drawing, temp_file = draw_ship(ship_type, ship_deadweight, ship_length, ship_width, ship_depth, current_language)
        response = FileResponse(open(os.getcwd() + "/media/" + temp_file + ".dxf", "rb"))
        os.remove(os.getcwd() + "/media/" + temp_file + ".dxf")
        return response