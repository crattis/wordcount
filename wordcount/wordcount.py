# Count the occurrences of the words in local files
import os


def main():
    word_count = {}
    # TODO: For loop for local files
    for html_file in os.scan('.'):
        if html_file.is_file():
            with open(html_file, 'r') as file:
                content = ' '.join(line for line in file.read().splitlines())
                content = content.split(' ')
                for word in content:
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1


if __name__ == '__main__':
    main()
