from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("operation", type=str)
args.add_argument("amount", type=float, nargs='?')

args = vars(args.parse_args())

print(args)