from slider import Slider


def get_sliders():
    screen_width = 1600
    screen_padding = 50
    slider_width = 300
    slider_height = 5
    vertical_spacing = 100
    left_x = screen_padding
    right_x = screen_width - screen_padding - slider_width
    sliders = [
        Slider(
            left_x, 100, slider_width, slider_height, 0, 1, 0.01, "Reproduction Chance"
        ),
        Slider(
            right_x, 100, slider_width, slider_height, 0, 1000, 500, "Live Constant"
        ),
        Slider(
            left_x,
            100 + vertical_spacing,
            slider_width,
            slider_height,
            0,
            5,
            1,
            "Mutation Rate",
        ),
        Slider(
            right_x,
            100 + vertical_spacing,
            slider_width,
            slider_height,
            1,
            10,
            2,
            "Birth Amount",
            type="int",
        ),
        Slider(
            left_x,
            100 + 2 * vertical_spacing,
            slider_width,
            slider_height,
            0,
            1,
            1,
            "Mutation Chance",
        ),
        Slider(
            right_x,
            100 + 2 * vertical_spacing,
            slider_width,
            slider_height,
            0,
            10000,
            1000,
            "Limit",
            type="int"
        ),
        Slider(
            left_x,
            100 + 3 * vertical_spacing,
            slider_width,
            slider_height,
            0,
            1,
            0.2,
            "Fitness Split",
        ),
        Slider(
            right_x,
            100 + 3 * vertical_spacing,
            slider_width,
            slider_height,
            0,
            1,
            0.02,
            "Fitness Cleaning Prob",
        ),
    ]
    return sliders
