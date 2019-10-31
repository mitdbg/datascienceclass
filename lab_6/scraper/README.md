# Objective

Implement the missing parts of the script below, using [`multiprocessing`](https://docs.python.org/2/library/multiprocessing.html)
to scrape content from a list of URLs. Specifically, the script takes as
input URLS from the http://regexlib.com website, and scrapes tuples of
"category" and "regex", storing the results on a CSV file.

# Requirements
* Python 2.X
* Python pip

To install all requirements, run the following from your Docker container:

```
# Python 2.X
$ apt update && apt install -y python python-pip

# Pip packages
$ pip2 install -r requirements.txt
```

# Usage

```
$ python scraper.py -h
usage: scraper.py [-h] -i INPUT_CSV -o OUTPUT_CSV

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
```

# Example

```
$ python scraper.py -i input_regexlib_urls.csv -o /tmp/scraped_regexes.csv -n 8
```

We provide most of the code for you, including parsing HTML content, as well as
the actual scraping and cleaning of scraped regexes. You only have to implement
the missing `multiprocessing` functionality using `Process` and `Queue`. This is
similar to the sample code we saw in [Lecture 15](http://dsg.csail.mit.edu/6.S080/lectures/lec15-code.zip).
