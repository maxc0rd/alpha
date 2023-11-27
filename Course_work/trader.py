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

    def read_json(self):

        with open(self.json_path, "r") as config_json:
            my_json = config_json.read()
        config_dict = json.loads(my_json)

        return config_dict

    def get_rate(self):

        current_rate = self.read_json()["the_rate"]

        return current_rate

    def get_delta(self):
        current_delta = self.read_json()["delta"]

        return current_delta

    def get_uah(self):
        current_uah_balance = self.read_json()["uah_balance"]

        return current_uah_balance

    def get_usd(self):
        current_usd_balance = self.read_json()["usd_balance"]

        return current_usd_balance

    def randomize_rate(self):

        random_rate = random.uniform(self.get_rate() - self.get_delta(), self.get_rate() + self.get_delta())

        return round(random_rate, 2)


whats_inside = GetFromJson("alpha/Course_work/config.json")

if args["operation"] == "RATE":
    print(whats_inside.get_rate())

if args["operation"] == "NEXT":
    print(whats_inside.randomize_rate())
