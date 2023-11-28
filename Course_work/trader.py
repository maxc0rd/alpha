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

    def buy_usd(self, usd_amount):

        if usd_amount == "ALL":
            usd_all_in = self.get_uah() / self.get_rate()
            self.write_in_state(round(self.get_usd() + usd_all_in, 2), "usd_balance")
            self.write_in_state(0, "uah_balance")
        else:
            required_uah_amount = self.get_rate() * int(usd_amount)
            if self.get_uah() < required_uah_amount:
                return print(f"UNAVAILABLE, REQUIRED BALANCE UAH {required_uah_amount}, AVAILABLE {self.get_uah()}")
            else:
                self.write_in_state(round(self.get_usd() + int(usd_amount), 2), "usd_balance")
                self.write_in_state(round(self.get_uah() - required_uah_amount, 2), "uah_balance")

    def sell_usd(self, usd_amount):

        if usd_amount == "ALL":
            usd_all_in = self.get_usd() * self.get_rate()
            self.write_in_state(0, "usd_balance")
            self.write_in_state(round(self.get_uah() + usd_all_in, 2), "uah_balance")
        else:
            required_usd_amount = self.get_rate() * int(usd_amount)
            if self.get_usd() < int(usd_amount):
                return print(f"UNAVAILABLE, REQUIRED BALANCE USD {usd_amount}, AVAILABLE {self.get_usd()}")
            else:
                self.write_in_state(round(self.get_usd() - int(usd_amount), 2), "usd_balance")
                self.write_in_state(round(self.get_uah() + required_usd_amount, 2), "uah_balance")


whats_inside = GetFromJson("config.json")

if args["operation"] == "RATE":
    print(whats_inside.get_rate())

if args["operation"] == "NEXT":
    whats_inside.randomize_rate()

if args["operation"] == "AVAILABLE":
    print(f"USD {whats_inside.get_usd()} UAH {whats_inside.get_uah()}")

if args["operation"] == "RESTART":
    whats_inside.rw_json()

if args["operation"] == "BUY":
    whats_inside.buy_usd(args["amount"])

# Можем покупать не только целые доллары (int -> float?) !!
# Можем покупать не только целые гривны (int -> float?) !!
if args["operation"] == "SELL":
    whats_inside.sell_usd(args["amount"])
