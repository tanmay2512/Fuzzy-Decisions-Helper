# 🧠 CLI Decision Assistant  

A simple and fun **Python-based command-line decision-making tool**.  
Ask any question and choose how you want your answer:

- 🎲 **Best of 1** – Get a single True/False response  
- 🎲🎲🎲 **Best of 3** – Generates three independent results and decides by majority  
- 📖 **Book of Answers** – Gives a wisdom-style random message  
- 🚪 **Exit** – Leave the program

This project is lightweight, beginner-friendly, and fully customizable.

---

## ✨ Features
- Interactive CLI interface  
- Pure Python (no external dependencies needed)  
- Randomized answers for unpredictability  
- Multiple modes of decision-making  
- Easy to extend and modify  
- Editable “Book of Answers” list

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/tanmay2512/Fuzzy-Decisions-Helper.git
cd Fuzzy-Decisions-Helper
```
Run the program:
```python
python Fd_intermediate.py
```
## ▶️ Usage Example
### Best of 1
```python
enter your question: is chatgpt good?
Enter your choice: 1
True
```
### Best of 3
```python
enter your question: is chatgpt good?
Enter your choice: 2
All results are False, False, True
Final result is False
```
### Book of Answers
```python
enter your question: is chatgpt good?
Enter your choice: 3
Your answer from the book is: The answer will come in a dream.
```
### (Optional) If you add dependencies later, you can include:
```bash
requirements.txt
```
## 🔧 Customization
Modify the Book of Answers txt and add your custom answers in a new line 

## 🧩 Dependencies
This program need colorama to run install it with:
```bash
pip install colorama
```
The core program uses only Python’s standard library (random).
Additional packages are optional.
