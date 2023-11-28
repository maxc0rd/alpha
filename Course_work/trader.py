from argparse import ArgumentParser
import json
import random

args = ArgumentParser()

args.add_argument("operation", type=str)
args.add_argument("amount", type=str, nargs='?')

args = vars(args.parse_args())


class GetFromJson:

    def __init__(self, json_path):
        self.json_path = json_path
        self.history = "history.txt"

    def update_history(self, action):
        with open(self.history, "a") as history_file:
            history_file.write(action)

    def rw_json(self):

        with open(self.json_path, "r") as config_json:
            pre_data = json.load(config_json)
        with open("state.json", "w") as copy_json:
            json.dump(pre_data, copy_json, indent=2)
        restart_session = open(self.history, "w")
        restart_session.write("Currency trader powered by Max Lekontsev\n\n"
                              "> User has started a new trading session\n\n")
        restart_session.close()

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
                usd_all_in = round(self.get_uah() / self.get_rate(), 2)
                usd_balance_after_all = self.get_usd() + usd_all_in
                self.write_in_state(usd_balance_after_all, "usd_balance")
                self.write_in_state(0, "uah_balance")
                self.update_history(f"Successful attempt to exchange ALL available UAH to USD -> "
                                    f"new balance {usd_balance_after_all} USD 0.00 UAH\n")
        else:
            required_uah_amount = round(self.get_rate() * float(usd_amount), 2)
            if float(usd_amount) == 0:
                self.update_history(f"Unsuccessful attempt to buy {usd_amount} USD -> "
                                    f"Amount should be bigger than 0\n")
                return print("You can't buy 0 USD !")
            elif self.get_uah() < required_uah_amount:
                low_uah_balance = f"UNAVAILABLE, REQUIRED BALANCE UAH {required_uah_amount}, AVAILABLE {self.get_uah()}"
                self.update_history(f"Unsuccessful attempt to buy {usd_amount} USD -> {low_uah_balance}\n")
                return print(low_uah_balance)
            else:
                usd_balance_after = round(self.get_usd() + float(usd_amount), 2)
                uah_balance_after = round(self.get_uah() - required_uah_amount, 2)
                self.write_in_state(usd_balance_after, "usd_balance")
                self.write_in_state(uah_balance_after, "uah_balance")
                self.update_history(f"Successful attempt to buy {usd_amount} USD -> "
                                    f"new balance {usd_balance_after} USD {uah_balance_after} UAH\n")

    def sell_usd(self, usd_amount):

        if usd_amount.upper() == "ALL":
            if self.get_usd() == 0:
                self.update_history("Unsuccessful attempt to exchange ALL available USD to UAH -> "
                                    "CURRENT USD BALANCE 0.00\n")
                return print(":( NOT POSSIBLE. CURRENT USD BALANCE 0.00")
            else:
                usd_all_in = self.get_usd() * self.get_rate()
                uah_balance_after_all = round(self.get_uah() + usd_all_in, 2)
                self.write_in_state(0, "usd_balance")
                self.write_in_state(uah_balance_after_all, "uah_balance")
                self.update_history(f"Successful attempt to exchange ALL available USD to UAH -> "
                                    f"new balance {uah_balance_after_all} UAH 0.00 USD\n")
        else:
            required_usd_amount = round(self.get_rate() * float(usd_amount), 2)
            if float(usd_amount) == 0:
                self.update_history(f"Unsuccessful attempt to sell {usd_amount} USD -> "
                                    f"Amount should be bigger than 0\n")
                return print("You can't sell 0 USD !")
            elif self.get_usd() < float(usd_amount):
                low_usd_balance = f"UNAVAILABLE, REQUIRED BALANCE USD {usd_amount}, AVAILABLE {self.get_usd()}"
                self.update_history(f"Unsuccessful attempt to sell {usd_amount} USD -> {low_usd_balance}\n")
                return print(low_usd_balance)
            else:
                usd_balance_after = round(self.get_usd() - float(usd_amount), 2)
                uah_balance_after = self.get_uah() + required_usd_amount
                self.write_in_state(usd_balance_after, "usd_balance")
                self.write_in_state(round(uah_balance_after, 2), "uah_balance")
                self.update_history(f"Successful attempt to sell {usd_amount} USD -> "
                                    f"new balance {usd_balance_after} USD {uah_balance_after} UAH\n")


whats_inside = GetFromJson("config.json")

if args["operation"].upper() == "RATE":
    online_rate = whats_inside.get_rate()
    whats_inside.update_history(f"Get CURRENT rate -> {online_rate}\n")
    print(online_rate)
elif args["operation"].upper() == "NEXT":
    whats_inside.randomize_rate()
elif args["operation"].upper() == "AVAILABLE":
    available_balance = f"USD {whats_inside.get_usd()} UAH {whats_inside.get_uah()}"
    whats_inside.update_history(f"Get AVAILABLE balance -> {available_balance}\n")
    print(available_balance)
elif args["operation"].upper() == "RESTART":
    whats_inside.rw_json()
elif args["operation"].upper() == "BUY":
    whats_inside.buy_usd(args["amount"])
elif args["operation"].upper() == "SELL":
    whats_inside.sell_usd(args["amount"])
else:
    print(":( Not supported\nChoose one of the following arguments:\n"
          "RATE\nNEXT\nAVAILABLE\nRESTART\nBUY XXX\nBUY ALL\nSELL XXX\nSELL ALL")

