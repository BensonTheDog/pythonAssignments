# manual list of pairs:  (name = string, rgb values = 3-tuple)
RGB_COLORS = [
    ("white", (1., 1., 1.)),
    ("silver", (.75, .75, .75)),
    ("gray", (.5, .5, .5)),
    ("black", (0., 0., 0.)),
    ("red", (1., 0., 0.)),
    ("maroon", (.5, 0., 0.)),
    ("yellow", (1., 1., 0.)),
    ("olive", (1., 0., 0.)),
    ("lime", (0., 1., 0.)),
    ("green", (0., .5, 0.)),
    ("aqua", (0., 1., 0.)),
    ("teal", (1., .5, .5)),
    ("sky blue", (0.529, 0.808, 0.922)),
    ("blue", (0., 0., 1.)),
    ("navy", (0., 0., 0.5)),
    ("fuchsia", (1., 0., 1.)),
    ("purple", (.5, 0., .5)),
    ("pink", (1., 0.753, 0.796)),
    ("hot pink", (1., 0.412, 0.706)),
    ("lime green", (0.196, 0.804, 0.196)),
    ("pale green", (0.596, 0.984, 0.596)),
    ("blue violet", (0.541, 0.169, 0.886)),
    ("turquoise", (0.251, 0.878, 0.816)),
    ("sea green", (0.180, 0.545, 0.341)),
    ("slate blue", (0.415, 0.353, 0.205)),
    ("aquamarine", (0.498, 1., 0.831)),
    ("peach puff", (1., 0.855, 0.725)),
    ("khaki", (0.941, 0.901, 0.549)),
    ("tan", (0.824, 0.706, 0.549))
]


def get_rgb_value():
    """ ask use for three values between 0.0 and 1.0 and return as a 3-tuple
        keep in loop until obey """
    accepted = False
    while (not accepted):
        user_color = input("\nenter red, green and blue values of your color, "
                           "separated by a space. "
                           "\nlegal values run from 0.0 (min) to 1.0 (max): ")
        try:
            rgb_list = user_color.split()
            r, g, b = rgb_list
            r, g, b = float(r), float(g), float(b)
            if (not (0 <= r <= 1 and 0 <= g <= 1 and 0 <= b <= 1)):
                print(" *ERROR*  Values must be between 0.0 and 1.0 (inclusive).")
                continue
            accepted = True
        except ValueError:
            print(" *ERROR*  Please enter 3 numbers separated by spaces.")

    return (r, g, b)


def color_dist(rgb_1, rgb_2):
    if (type(rgb_1) != tuple
            or
            type(rgb_2) != tuple
            or
            len(rgb_1) != 3
            or
            len(rgb_2) != 3
    ):
        return None

    dist = 0
    for k in range(3):
        dist += (rgb_2[k] - rgb_1[k]) ** 2

    return dist


def find_closest_match(rgb_val, color_list):
    # establish initial "best" values
    best_color_so_far = None
    # whatever the definition of dist() is, the following is larger:
    smallest_dist_so_far = 1 + color_dist((0, 0, 0), (1, 1, 1))

    for color in color_list:
        current_distance = color_dist(rgb_val, color[1])
        if current_distance < smallest_dist_so_far:
            smallest_dist_so_far = current_distance
            best_color_so_far = color

    return best_color_so_far


print("\nThese are our packaged colors --------------\n")
for k in range(len(RGB_COLORS)):
    print("tuple #{:3}: {:13} = {}".
          format(k, RGB_COLORS[k][0], str(RGB_COLORS[k][1])))

print("\nNow, you can provide the RGB values of your own custom color.\n")
user_rgb_tuple = get_rgb_value()
winner = find_closest_match(user_rgb_tuple, RGB_COLORS)

print (("\nThe pre-packaged color that most closely matches your custom "
        "design is \n'{}',\n "
        "whose rgb values are\n"
        "red = {}, green = {}, blue = {}\n").
       format(winner[0], winner[1][0], winner[1][1], winner[1][2]))