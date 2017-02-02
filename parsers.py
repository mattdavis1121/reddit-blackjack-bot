import argparse

meta_parser = argparse.ArgumentParser()
meta_parser.add_argument('--test', action="store_true")
meta_args = meta_parser.parse_args()

# Command parser
cmd_parser = argparse.ArgumentParser()
cmd_parser.add_argument('-b', '--bet', type=int, help='specify a bet other than the default. must be used with -d/--deal. example: "--deal --bet 100"')
cmd_parser.add_argument('-d', '--deal', action='store_true', help='deal a new hand')
cmd_parser.add_argument('-s', '--stay', action='store_true', help='issue a stay command and allow dealer to play out hand')
cmd_parser.add_argument('-dd', '--doubledown', '--double', dest='double_down', action='store_true', help='issue a double down command')
cmd_parser.add_argument('-sp', '--split', action='store_true', help='issue a split command - CURRENTLY INOPERABLE')
cmd_parser.add_argument('--history', action='store_true', help='display user hand history - CURRENTLY INOPERABLE')
cmd_parser.add_argument('--highscores', '--leaderboard', dest='high_scores', action='store_true', help='display the highest scoring users')