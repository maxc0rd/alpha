from argparse import ArgumentParser
import json
import os
import random

args = ArgumentParser()
# default надо?
# help надо?
args.add_argument("operation", type=str)
args.add_argument("amount", type=str, nargs='?')

args = vars(args.parse_args())

print(args)


class GetFromJson:

    def __init__(self, json_path):
        self.json_path = json_path

    def rw_json(self):

        with open(self.json_path, "r") as config_json:
            pre_data = json.load(config_json)
        with open("state.json", "w") as copy_json:
            json.dump(pre_data, copy_json, indent=2)

    def read_state(self):
        with open("state.json", "r") as read_state:
            my_json = read_state.read()
        config_dict = json.loads(my_json)

        return config_dict

    def get_rate(self):

        current_rate = self.read_state()["the_rate"]

        return current_rate

    def get_delta(self):
        current_delta = self.read_state()["delta"]

        return current_delta

    def get_uah(self):
        current_uah_balance = self.read_state()["uah_balance"]

        return current_uah_balance

    def get_usd(self):
        current_usd_balance = self.read_state()["usd_balance"]

        return current_usd_balance

    def randomize_rate(self):

        random_rate = random.uniform(self.get_rate() - self.get_delta(), self.get_rate() + self.get_delta())
        self.write_in_state(round(random_rate, 2), "the_rate")

    def write_in_state(self, write_rate, key_rate):

        with open("state.json", "r") as old_state:
            exp_old = json.load(old_state)
        exp_old[key_rate] = write_rate

        with open("state.json", "w") as new_state:
            json.dump(exp_old, new_state, indent=2)


whats_inside = GetFromJson("config.json")

if args["operation"] == "RATE":
    print(whats_inside.get_rate())

if args["operation"] == "NEXT":
    whats_inside.randomize_rate()
