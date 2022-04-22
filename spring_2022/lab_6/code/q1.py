import argparse
import csv
import glob
import html
import multiprocessing
import os
import pandas as pd
import queue
import requests
import sys
import time

from lxml import html as h
from multiprocessing import Queue

#VERBOSE = False
VERBOSE = True

# Useful for debugging concurrency issues.
def log(msg):
    if not VERBOSE:
        return
    print(multiprocessing.current_process().name, msg, sys.stderr)


def get_urls(csv_file):
    df = pd.read_csv(csv_file)
    urls = df['url']
    assert urls[0]
    return df


# Fetches html content for a given url, saving content onto out_filename if GET
# is successful (i.e., HTTP GET returns status code 200).
def download_html(url, out_filename):
    response = requests.get(url, timeout=1)
    http_status = response.status_code
    if (http_status != 200):
        print('ERROR: request failed with HTTP status code ', http_status)
        return

    os.makedirs(os.path.dirname(out_filename), exist_ok=True)
    with open(out_filename, 'wb') as f:
        f.write(response.content)
        print('HTML contents saved under %s' % out_filename)


# Scrapes list of <category,regex> entries from previously downloaded HTML
# content, and enqueues them for later processing.
def scrape_html(out_queue, category, html_filename):
    with open(html_filename, 'r', encoding='utf-8') as f:
        contents = f.read()
        tree = h.fromstring(contents)

        # Valid as of Apr 2022.
        scraped_regexes = tree.xpath('.//tr[@class="expression"]/*[2]')

        csv_rows = []
        for regex in scraped_regexes:
            csv_row = to_csv_row(category, regex)
            if csv_row:
                csv_rows.append(csv_row)

        # YOUR CODE GOES HERE.
        # Add rows to out queue.


# Cleans scraped regex for saving onto output csv file.
def to_csv_row(category, scraped_regex):
    row = {'category': category}

    try:
        regex_bytes = bytes(scraped_regex[0].text, encoding='utf-8')
        regex_text = str(regex_bytes, encoding='utf-8')
        unescaped_regex = html.unescape(regex_text)

        # Data quality check: skip regexes that contain new lines.
        if "\n" in unescaped_regex:
            return None

        clean_regex = unescaped_regex.replace(" ", "")
        # More cleaning: remove optional double quotes surrouding regex.
        if clean_regex.startswith('"') and clean_regex.endswith('"'):
            clean_regex = clean_regex[1:-1]
        row['regex'] = clean_regex
    except Exception as e:
        # Escaping won't throw exceptions for the included html files.
        template = 'Exception while escaping regex: type: {0}, args:\n{1!r}'
        msg = template.format(type(e).__name__, e.args)
        print(msg)
        return None

    return row


# Each worker will scrape regexes from local HTML files in parallel.
def worker(task_queue, out_queue):
    # YOUR CODE GOES HERE.
    # Dequeue tuples of (category,html_filename) from the task queue,
    # and use these as input for scrape_html. Exit when the task queue 
    # is empty.
    return



def main_task(urls_df, output_file, n_workers, redownload_html):
    # YOUR CODE GOES HERE.
    # 1. Create two Queues, one for adding tuples of (category, html_filename)
    #    for processing, and another to store the scraped regexes.

    # NOTE: You need not enable this flag. This is here just so that you see
    # how the HTML files included under downloaded_html/ were originally
    # downloaded.
    if (redownload_html):
        print('Deleting existing html data...')
        os.system('rm -rf downloaded_html/')

        # Group urls by category, use index within same category for saving html.
        for category, group in urls_df.groupby('category'):
            i = 0
            for _, row in group.iterrows():
                html_filename = 'downloaded_html/%s/%02d.html' % (category, i)
                i += 1

                # Save local copy of downloaded html content.
                print('downloading:\n%s\nsaving: %s' % (row['url'],
                                                        html_filename))
                download_html(row['url'], html_filename)

    # Enqueue all tuples of <category, html_filename> for workers to scrape.
    html_filenames = glob.glob(os.path.join('', '../data/downloaded_html/*/*.html'))
    for f in html_filenames:
        category = f.split('/')[3]
        # YOUR CODE GOES HERE
        # 2. Enqueue tuples of (category, html filename) onto the task queue.

    # YOUR CODE GOES HERE
    # 3. Start up the workers.

    csv_rows = []
    try:
        while True:
            # https://bugs.python.org/issue20147
            csv_rows += out_queue.get(block=True, timeout=5)
    except queue.Empty:
        log('Done!')

    with open(output_file, 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=['category', 'regex'],
            quotechar='"',
            quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(csv_rows)


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
        choices=range(1, 64),
        required='True')
    parser.add_argument(
        '--redownload_html',
        help='Redownloads HTML data from regexlib.com',
        dest='redownload_html',
        action='store_true')
    parser.set_defaults(redownload_html=False)
    args = parser.parse_args()

    print('Scraping regexes...')

    urls_df = get_urls(args.input_csv)
    main_task(urls_df, args.output_csv, args.num_workers, args.redownload_html)

    print('Regexes saved at "%s".' % args.output_csv)
