import ezdxf
import os
import datetime

def draw_ship(ship_type, deadweight, length, width, depth, lang):
    # function creates drawing of a ship
    doc = ezdxf.new("R2004")
    msp = doc.modelspace()
    # create edge lines
    basicX = 0
    basicY = 0
    ships_points = [
        (basicX, basicY, 0, 0, -0.1),
        (basicX + length * 0.2, basicY + width/2, 0, 0, 0),
        (basicX + length * 0.9, basicY + width/2, 0, 0, -0.1),
        (basicX + length, basicY + width * 0.25, 0, 0, 0),
        (basicX + length, basicY - width * 0.25, 0, 0, -0.1),
        (basicX + length * 0.9, basicY - width/2, 0, 0, 0),
        (basicX + length * 0.2, basicY - width/2, 0, 0, -0.1),
        (basicY, basicX, 0, 0, 0),
    ]
    msp.add_lwpolyline(ships_points)
    # add hatch
    hatch = msp.add_hatch(color=131)
    hatch.transparency = 0.4
    ships_hatch_points = []
    for p in ships_points:
        ships_hatch_points.append([p[0], p[1], p[-1]])
    hatch.paths.add_polyline_path(ships_hatch_points)
    # add text
    if lang == "ru":
        text = "DWT=" + str(deadweight) + " т, L = " + str(length) + " м, W = " + str(width) + " м, T = " + str(depth) + " м"
        ship_name = ship_type.name
    else:
        text = "DWT=" + str(deadweight) + " t, L = " + str(length) + " m, W = " + str(width) + " m, T = " + str(depth) + " m"
        ship_name = ship_type.eng_name
    msp.add_text(text, height=2.5).set_placement((length / 2 - 2 * len(text)/2, 0))
    msp.add_text(ship_name, height=2.5).set_placement((length / 2 - 2 * len(ship_name) / 2, 3.5))
    # save file
    temporal_file_name = ship_type.eng_name + "_" + str(datetime.datetime.now())
    doc.saveas(os.getcwd() + "/media/" + temporal_file_name + ".dxf")
    return doc, temporal_file_name

if __name__ == "__main__":
    ship_type = "Танкер"
    deadweight = 100000
    length = 250
    width = 59
    depth = 20
    draw_ship(ship_type, deadweight, length, width, depth)