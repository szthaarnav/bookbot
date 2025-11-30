# BookBot: A Python Text Analyzer 

BookBot is a lightweight command-line utility built in Python for analyzing text files, such as digital books. It reads the contents of a file and generates a statistical report in the console, providing key insights into the text's composition.

The project is structured modularly, separating file handling (`main.py`) from statistical functions (`stats.py`).

## ✨ Features

* **Total Word Count:** Calculates and prints the total number of words in the input text file.
* **Character Frequency:** Counts the occurrences of every letter (case-insensitive) in the text.
* **Whitespace and Non-Alphabetic Exclusion:** Ignores spaces and other characters during the character counting process, focusing only on letters.
* **Sorted Report:** Prints the character counts in **descending order** (most frequent first), making it easy to identify the most commonly used letters.
* **Command Line Usage:** Designed to accept the file path directly as a command-line argument.

## 🛠️ Technology Used

* **Language:** Python 3
* **Modules:** Standard Python Library functions (no external dependencies).
* **I/O:** File input via command-line argument and standard console output.

## 🚀 How to Run

### Prerequisites

You need **Python 3** installed on your system.

### Running the Analyzer

The script must be run from your terminal and requires the path to the text file you wish to analyze.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/szthaarnav/bookbot
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd bookbot
    ```
3.  **Run the script** using a book file from your `books` folder:

    ```bash
    python3 main.py books/frankenstein.txt
    ```

### Example Output

Running the command above will produce a report similar to this (results will vary based on the book):
```
Analyzing book found at books/frankenstein.txt...
Found 113300 total words
e: 56391
t: 41855
a: 38201
o: 36582
i: 34107
...
q: 504
z: 219
```
