""" Convert data files from CSV to JSON """
import csv
import json
import inquirer

DATA_PATH = 'espn_extractor/data'
QUESTIONS = [
    inquirer.List(
        'file',
        message='Which file do you want to convert from CSV to JSON?',
        choices=['league_history', 'DST', 'K', 'QB', 'RB', 'TE', 'WR']
    )
]


def csv_to_json():
    """ Primary function, only one to be called externally """
    answer = inquirer.prompt(QUESTIONS)
    user_input = answer['file']
    call_method(user_input)


def call_method(file_name):
    """ Ensure valid file has been selected and a function to convert the file exists """
    global_vars = globals()
    if file_name in global_vars:
        return global_vars[file_name]()
    return print(f'{file_name} function not found')


def league_history():
    """ Convert league_history.csv into league_history.json"""
    data = {}

    with open(f'{DATA_PATH}/league_history.csv', encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)

        for row in csv_reader:
            year = row['year']
            owner = row['owner']

            if year not in data:
                data[year] = {}

            if owner not in data[year]:
                data[year][owner] = {
                        'team_name': row['team_name'],
                        'win': row['win'],
                        'loss': row['loss'],
                        'draws': row['draws'],
                        'final_standing': row['final_standing'],
                        'points_for': row['points_for'],
                        'points_against': row['points_against'],
                        'acquisitions': row['acquisitions'],
                        'trades': row['trades'],
                        'drops': row['drops'],
                        'streak_length': row['streak_length'],
                        'streak_type': row['streak_type'],
                        'playoff_seed': row['playoff_seed']
                    }

    with open(f'{DATA_PATH}/league_history.json', 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data, indent=4))
