""" Run ESPN Fantasy Data Extractor """
import argparse
from espn_extractor.draft_board import extract_draft_board, extract_draft_positions, \
    extract_draft_position
from espn_extractor.draft_board_excel import extract_draft_cheatsheet
import config

SUPPORTED_FORMATS = 'data and xlsx'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--position',
                        help='Load data for specific position (QB, RB, WR, TE, DST, K)')
    parser.add_argument('-s', '--size', help='How many players per position to load',
                        type=int, default=50)
    parser.add_argument('-f', '--format',
                        help=f'What format file should be exported? ({SUPPORTED_FORMATS}'
                             f' supported)',
                        default='xlsx')
    args = parser.parse_args()
    export_format = args.format.lower()
    if export_format == 'data':
        # CSV and TXT support position flag
        if args.position:
            extract_draft_position(config, args.position.upper(), args.size, False)
        else:
            # if no pisition, load everything
            extract_draft_positions(config, args.size, False)
            extract_draft_board(config, args.size, False)
    elif export_format == 'xlsx':
        # No position flag support for xlsx
        extract_draft_cheatsheet(config, args.size, False)
    else:
        print(f'Invalid Format: {args.format}. Suppoerted formats: {SUPPORTED_FORMATS}.')
