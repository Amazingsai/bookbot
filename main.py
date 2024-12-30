def main():
    with open("books/frankenstein.txt") as f:
        #...
        file_contents = f.read()
        report(file_contents)
def count_words(text):
    words = text.split()
    return len(words)
def count_char(text):
    d = {}
    lowercase = text.lower()
    for char in lowercase:
        if(char not in d):
            d[char] = 1
        else:
            d[char] += 1
    return d
def report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document\n")
    d = count_char(text)
    for char in d:  
        if(char.isalpha()):
             print(f"The {char} character was found {d[char]} times")
    print("\n--- End report ---")
main()