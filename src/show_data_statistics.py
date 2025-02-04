import argparse
from collections import Counter
import json
import os
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_path', '-i',
        type=str,
        required=True,
    )
    args = parser.parse_args()

    with open(args.input_path) as f:
        print(f'[Info] Read: {args.input_path}', file=sys.stderr)
        data = json.load(f)

    # data statistics
    counter = Counter()
    key2sets = {'num_mentions': set()}

    for article_id, article in data.items():
        counter['num_articles'] += 1

        if 'sentences' in article:
            counter['num_sentences'] += len(article['sentences'])

            for sen_id, sen in article['sentences'].items():
                sen_text = sen['text']
                counter['num_chars'] += len(sen_text)

                if 'attributes' in sen:
                    for attr in sen['attributes']:
                        key = f'num_attributes:type={attr["type"]}'
                        counter[key] += 1
                        if attr['type'][0] in ('L', 'T', 'V'):
                            print(article_id, sen['text'], attr)

        if 'mentions' in article:
            counter['num_mentions'] += len(article['mentions'])

            for men_id, men in article['mentions'].items():
                key2sets['num_mentions'].add(men['text'])

                if 'entity_type' in men:
                    key = f'num_mentions:entity_type={men["entity_type"]}'
                    counter[key] += 1
                    if not key in key2sets:
                        key2sets[key] = set()
                    key2sets[key].add(men['text'])

    print('\nData statistics -- Total (Unique):')
    main_keys = ['num_articles', 'num_sentences', 'num_chars', 'num_mentions']
    for key in main_keys:
        val = counter[key]
        if key in key2sets:
            val2 = len(key2sets[key])
            print(f'{key}\t{val}\t({val2})')
        else:
            print(f'{key}\t{val}')
        
    for key, val in sorted(counter.items()):
        if not key in main_keys:
            if key in key2sets:
                val2 = len(key2sets[key])
                print(f'{key}\t{val}\t({val2})')
            else:
                print(f'{key}\t{val}')


if __name__ == '__main__':
    main()
