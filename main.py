from parse_money_tracker_data import ParseData
from aggregated_money_tracker import AggregatedMoneyTracker
from money_tracker import MoneyTracker
from money_tracker_menu import MoneyTrackerMenu
import sys

def main():
    username = sys.argv[1].lower()
    filename = "money_tracker_{}.txt".format(username)
    parsed_data = ParseData(filename)
    aggregated_object = AggregatedMoneyTracker(parsed_data)
    money_tracker = MoneyTracker(aggregated_object)
    menu = MoneyTrackerMenu(username, money_tracker)

if __name__ == '__main__':
	main()