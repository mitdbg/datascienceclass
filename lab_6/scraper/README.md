# Objective

Implement the missing parts of the script below, using [`multiprocessing`](https://docs.python.org/2/library/multiprocessing.html)
to scrape content from a list of URLs. Specifically, the script takes as
input URLS from the http://regexlib.com website, and scrapes tuples of
"category" and "regex", storing the results on a CSV file.

**UPDATE (Nov 7th 2019): We now use Python3 instead of Python2 below.**

# Requirements
* Python 3.X
* Python pip3

To install all requirements, run the following from your Docker container:
```
# Pip packages
$ pip3 install -r requirements.txt
```

# Usage

```
$ python3 scraper.py -h
usage: scraper.py [-h] -i INPUT_CSV -o OUTPUT_CSV -n N_WORKERS [--redownload_html]

Scrapes regexes from http://regexlib.com.

arguments:
  -h, --help            show this help message and exit
  -i INPUT_CSV, --input_csv INPUT_CSV
                        Relative path of input CSV file containing regex
                        category and URLs to scrape.
  -o OUTPUT_CSV, --output_csv OUTPUT_CSV
                        Relative path of output CSV file containing scraped
                        regexes for each category.
  -n N_WORKERS, --num_workers N_WORKERS
                        Number of workers to use.
  --redownload_html     Redownloads HTML data from regexlib.com
```

# Example

```
$ python3 scraper.py -i input_regexlib_urls.csv -o /tmp/scraped_regexes.csv -n 8
```

We provide most of the code for you, including parsing HTML content, as well as
the actual scraping and cleaning of scraped regexes. You only have to implement
the missing `multiprocessing` functionality using `Process` and `Queue`. This is
similar to the sample code we saw in [Lecture 15](http://dsg.csail.mit.edu/6.S080/lectures/lec15-code.zip).

**UPDATE (Nov 7th 2019):**
We've noticed that downloading html content from regexlib.com is
non-deterministic, as the website can at times choose to reorder the listed
regex entries for a given category (you can confirm this by reloading one of
the provided regexlib URLs in [`input_regexlib_urls.csv`](`input_regexlib_urls.csv`)).

Therefore, we've updated this assignment to include code for scraping from
local html files included in the [`downloaded_html`](downloaded_html/) directory.

A correct solution should output **the same number of regexes** (i.e., number of
lines in [`/tmp/scraped_regexes.csv`] should be the same regardless of how many
workers you use. The order in which regexes are written to the file need not be
the same across multiple runs.
