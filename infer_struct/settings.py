import os

THIS_SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

Settings = {
    "path": {
        "power_grid_simple_examples": os.path.expandvars(
            f"{THIS_SCRIPT_PATH}/../.data/Network_raw_data_Ashkan"
        )
    }
}
