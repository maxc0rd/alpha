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
        self.history = "history.txt"
        # self.update_history()

    def update_history(self, action):
        with open(self.history, "a") as history_file:
            history_file.write(action)

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
        # self.update_history(f"Get CURRENT rate -> {current_rate}\n")

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
        upd_rate = round(random_rate, 2)
        self.write_in_state(upd_rate, "the_rate")
        self.update_history(f"Get NEXT rate -> {upd_rate}\n")

    def write_in_state(self, write_rate, key_rate):

        with open("state.json", "r") as old_state:
            exp_old = json.load(old_state)
        exp_old[key_rate] = write_rate

        with open("state.json", "w") as new_state:
            json.dump(exp_old, new_state, indent=2)

    def buy_usd(self, usd_amount):

        if usd_amount.upper() == "ALL":
            if self.get_uah() == 0:
                self.update_history("Unsuccessful attempt to exchange ALL available UAH to USD -> "
                                    "CURRENT UAH BALANCE 0.00\n")
                return print(":( NOT POSSIBLE. CURRENT UAH BALANCE 0.00")
            else:
                usd_all_in = self.get_uah() / self.get_rate()
                usd_balance_after_all = self.get_usd() + usd_all_in
                self.write_in_state(round(usd_balance_after_all, 2), "usd_balance")
                self.write_in_state(0, "uah_balance")
                self.update_history(f"Successful attempt to exchange ALL available UAH to USD -> "
                                    f"new balance {usd_balance_after_all} USD 0.00 UAH")
        else:
            required_uah_amount = round(self.get_rate() * float(usd_amount), 2)
            if self.get_uah() < required_uah_amount:
                low_uah_balance = f"UNAVAILABLE, REQUIRED BALANCE UAH {required_uah_amount}, AVAILABLE {self.get_uah()}"
                self.update_history(f"Unsuccessful attempt to buy {usd_amount} USD -> {low_uah_balance}\n")
                return print(low_uah_balance)
            else:
                usd_balance_after = self.get_usd() + float(usd_amount)
                uah_balance_after = self.get_uah() - required_uah_amount
                self.write_in_state(round(usd_balance_after, 2), "usd_balance")
                self.write_in_state(round(uah_balance_after, 2), "uah_balance")
                self.update_history(f"Successful attempt to buy {usd_amount} USD -> "
                                    f"new balance {usd_balance_after} USD {uah_balance_after} UAH\n")

    def sell_usd(self, usd_amount):

        if usd_amount.upper() == "ALL":
            if self.get_usd() == 0:
                return print(":( NOT POSSIBLE. CURRENT USD BALANCE 0.00")
            else:
                usd_all_in = self.get_usd() * self.get_rate()
                self.write_in_state(0, "usd_balance")
                self.write_in_state(round(self.get_uah() + usd_all_in, 2), "uah_balance")
        else:
            required_usd_amount = round(self.get_rate() * float(usd_amount), 2)
            if self.get_usd() < float(usd_amount):
                return print(f"UNAVAILABLE, REQUIRED BALANCE USD {usd_amount}, AVAILABLE {self.get_usd()}")
            else:
                self.write_in_state(round(self.get_usd() - float(usd_amount), 2), "usd_balance")
                self.write_in_state(round(self.get_uah() + required_usd_amount, 2), "uah_balance")


whats_inside = GetFromJson("config.json")

if args["operation"].upper() == "RATE":
    online_rate = whats_inside.get_rate()
    whats_inside.update_history(f"Get CURRENT rate -> {online_rate}\n")
    print(online_rate)

if args["operation"].upper() == "NEXT":
    whats_inside.randomize_rate()

if args["operation"].upper() == "AVAILABLE":
    available_balance = f"USD {whats_inside.get_usd()} UAH {whats_inside.get_uah()}"
    whats_inside.update_history(f"Get AVAILABLE balance -> {available_balance}\n")
    print(available_balance)

if args["operation"].upper() == "RESTART":
    whats_inside.rw_json()

if args["operation"].upper() == "BUY":
    whats_inside.buy_usd(args["amount"])

if args["operation"].upper() == "SELL":
    whats_inside.sell_usd(args["amount"])

# Можем покупать не только целые доллары (int -> float?) !!
# Можем покупать не только целые гривны (int -> float?) !!
# Почему в state.json один знак после запятой ?!
# выдать сообщение, если buy all , а денег на счете ноль !
