# Count the occurrences of the words in local files.
import os


def main():
    word_count = {}
    # Find HTML files in the current directory for Frequency Analysis.
    for html_file in os.listdir('.'):
        if html_file.endswith(".html"):
            with open(html_file, 'r') as file:
                # Get count the words used in the HTML file to a shared
                # dictionary.
                content = ' '.join(line for line in file.read().splitlines())
                content = content.split(' ')
                for word in content:
                    if word.lower() not in word_count:
                        word_count[word.lower()] = 1
                    else:
                        word_count[word.lower()] += 1
    # sort dictionary by value.
    word_list = sorted(word_count.items(),
                       key=lambda item: item[1], reverse=True)
    for counted in word_list:
        print(counted)


if __name__ == '__main__':
    main()
