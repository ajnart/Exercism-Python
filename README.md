![](https://github.com/ajnart/Exercism-Python/workflows/Python/badge.svg)
# Exercism-Python
This repo is about all my exercices from https://exercism.io/my/tracks/python

# My journey with python and exercism.io
## Why did I chose to do some code exercises ?
I'll soon have to look for an internship and with the current competencies that I've got at Epitech, I don't feel like it's enough to ask for a good internship. And i wanted to learn a bunch of cool stuff.
## Why python ?
### Because it's simple and fast (to code).
When coding, I like to keep my main focus on the problem solving part and after a bit of research I found out that python was a good tool for that usage.
### Because it was going to be useful to me
Python is one of the main programming languages used in *"AI"* which is the field I'd like to work in.
### Because it's fun !
Learning a new programming language looks like hard work but it turns out its often fun *(at least it is for me)*
## Why Exercism ?
### Because it has an API
Exercism has an api that integrates into your computer with a packet you install. It allows you to download exercises via simple terminal commands like ''exercism download --exercise=space-age --track=python''
Where ``--exercise=`` is the exercise and ``--track=`` is the programming language.
### It's fast to verify is you're doing the right thing
Exercism allows you to run test files by using the **pytest** command in your terminal, the exercises come with a test suite that once ran, allow you to see if you're passing the tests the exercise was made for.
### An understandable readme.md
A readme.me allows you to understand the exercise and show you what you need to code to make it work. It is often well formatted and helps to have a clear understanding of the subject
### It doesn't want an Std output
Unlike many other coding-exercice website, Exercism doesn't require you to print something, it just requires what your code is supposed to return when called, meaning you have to return a list if you're supposed to return one and can't cheat the system by printing the supposed output.
## My workflow
### Git
I've chosen to upload all my exercices to Github <i class="fa fa-github"></i> once completed [here](https://github.com/ajnart/Exercism-Python) to that recruiters can look at my code and just be astonished by the sheere size of my brain and my huge algorithmitic solving capabilities.
### VsCode
Visual Studio Code is the editor i've chosen to code these in. It allows me to have a direct keybind to run the tests and check where i'm at.
Also the linter [MagicPython](https://github.com/MagicStack/MagicPython) is just **the best.**
### Do whatever you want, whenever you want to do it
This website allows me to work on the exercice **I want** whenever **I want**. There's a lot of exercices for me to work on so if one bores me I can just switch to another exercice instead. And that's a big plus. <i class="fa fa-heart"></i>

## Some examples of what i've learned
One exercice that particularly stood out to me was the **isogram** exercice, where you needed to code a program that would return ``True`` is a given string was an isogram or not. An isogram is a string or a word that only contains a letter once.

```python
def is_isogram(string: str):
    string = string.lower().replace(' ', '').replace('-', '')
    return len(string) == len(set(string))
```
### How does it work ?
The function called ``is_isogram`` will return True is the string passed (namely ``string``) is an isogram.
The ``return`` statement, with double equals **==** means that it will return **True** if the condition named after is also **True** . If not, it will return **False**

```python
string = string.lower().replace(' ', '').replace('-', '')
```
This means I **redefine** the string by setting it to lowercase letters only, replacing the blankspaces and dashes with nothing.

```python
return len(string) == len(set(string))
```
Here the condition has to be true to return **True**.
The function ``len()`` will get the lenght of the evaluated string (string) and return its value as an integer
This ``len()`` function has to be equal to the ``len()`` of the ``set()`` of string. ``set()`` is a function that will return an iterable without the duplicated in it. ``abbc -> abc``
Therefore, if our string passed as argument **contains a duplicate**, the ``len()`` of the ``set()`` and the normal string wouldn't be equal and the program would return False.

## Conclusion
**This coding journey has been really beneficial.**
I've learned loads and loads of things and am still learning new things each day. Code that used to take me 20 lines could now only take me about 4 or 5 and i've also learned a lot about the logic behind the resolution of problems and also the structure of the python programming language.

# Thank you
For taking the time to read all of this article. If you have any questions or suggestions about it feel free to send me an email at: [thomas.camlong@epitech.eu](mailto:thomas.camlong@epitech.eu)
