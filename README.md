# BHSTW_python_scripts
## This is an extension of the Writing scripts in Python module exercise, which can be found at [BrainHack School](https://school-brainhack.github.io/modules/python_scripts/).
- `useful_functions.py` has three functions `enc`, `dec`, and `process`, corresponding to `encrypt_letter(letter, key)`, `decrypt_letter(letter, key)`, and `process_message(message, key, encrypt)`. In addition, the function `instructions(show)` will print out the follwoing only if `show` takes the value `yes`
> cypher_script.py is a script for encrypting/decrupting messages...
> But only when it is run as a script, not imported as a module... 
- `cypher_script.py` has three functions: `cypher_main` which encrypts/decrypts message files and corresponds to the `main` function in the original exercise; `sort_names` is a function that sorts the words in a text file in ascending or descending order, depending on whether `--mode` is `ascend` or `descend`; `argparse` objects and methods are put under the `argpars_func` function, which gets imported into `third_script.py` 
- `third_script.py` imports `cypher_script` and calls the functions `argparse_func` and `sort_names`. This establishes how `cypher_main`, put under `if __name__ == "__main__"`, is not executed when one runs `third_scrip.py` in the terminal.
