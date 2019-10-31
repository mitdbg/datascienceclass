import argparse
import csv
import HTMLParser
import multiprocessing
import pandas as pd
import Queue
import requests
import sys

#from threading import Thread
from lxml import html


def log(msg):
    print(sys.stderr, multiprocessing.current_process().name, msg)


def get_urls(csv_file):
    df = pd.read_csv(csv_file)
    urls = df['url']
    assert urls[0]
    return df


# Scrapes list of <category,regex> entries from URL content, and enqueues them
# for later processing.
def scrape_url(out_queue, url_entry):
    if url_entry is not None:
        url = url_entry['url']
        category = url_entry['category']

        page = requests.get(url)
        tree = html.fromstring(page.content)

        # Valid as of Oct 2019.
        scraped_regexes = tree.xpath('.//tr[@class="expression"]/*[2]')
        html_parser = HTMLParser.HTMLParser()
        csv_rows = []
        for regex in scraped_regexes:
            csv_row = to_csv_row(category, regex)
            if csv_row is not None:
                csv_rows.append(csv_row)

        # YOUR CODE GOES HERE.
        # Add rows to out queue.


# Cleans scraped regex for saving onto output csv file.
def to_csv_row(category, scraped_regex):
    row = {'category': category}
    try:
        regex_text = scraped_regex[0].text.encode('utf-8')
        html_parser = HTMLParser.HTMLParser()
        unescaped_regex = html_parser.unescape(regex_text)

        # Data quality check: skip regexes that contain new lines.
        if "\n" in unescaped_regex:
            return None

        clean_regex = unescaped_regex.replace(" ", "")
        # More cleaning: remove optional double quotes surrouding regex.
        if clean_regex.startswith('"') and clean_regex.endswith('"'):
            clean_regex = clean_regex[1:-1]
        row['regex'] = clean_regex
    except:
        return None

    return row


# Each worker will scrape URLs in parallel.
def worker(task_queue, out_queue):
    try:
      # YOUR CODE GOES HERE.
      # Dequeue URLs from the task queue, and scrape them.
    except Queue.Empty:
        log('Done scraping!')


def main_task(urls_df, output_file, n_workers):
    # YOUR CODE GOES HERE.
    # 1. Create two Queues, one for adding URLs for processing,
    #    and another to store the scraped regexes.
    # 2. Enqueue URLs onto the task queue you created.
    # 3. Create your workers using Process and start them up.

    csv_rows = []
    try:
        while True:
            # https://bugs.python.org/issue20147
            csv_rows += out_queue.get(block=True, timeout=1)
    except Queue.Empty:
        log('Done!')

    with open(output_file, 'w') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=['category', 'regex'],
            quotechar='"',
            quoting=csv.QUOTE_ALL)
        writer.writeheader()
        #writer.writerows(csv_rows)  # use utf-8 encoding in python3
        for row in csv_rows:
            try:
                writer.writerow(row)
            except UnicodeEncodeError:
                pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Scrapes regexes from http://regexlib.com.')
    parser.add_argument(
        '-i',
        '--input_csv',
        help='Relative path of input CSV file containing regex '
        'category and URLs to scrape.',
        required='True')
    parser.add_argument(
        '-o',
        '--output_csv',
        help='Relative path of output CSV file containing '
        'scraped regexes for each category.',
        required='True')
    parser.add_argument(
        '-n',
        '--num_workers',
        help='Number of workers to use.',
        type=int,
        choices=xrange(1, 64),
        required='True')
    args = parser.parse_args()

    log('Scraping regexes...')

    urls_df = get_urls(args.input_csv)
    main_task(urls_df, args.output_csv, args.num_workers)

    log('Regexes saved at "%s".' % args.output_csv)
