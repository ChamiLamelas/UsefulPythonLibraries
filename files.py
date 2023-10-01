from pathlib import Path
import shutil
import pickle
import os

def read_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(data, file, append=False):
    if not isinstance(data, dict):
        raise TypeError(f"data was {type(data)}, must be dict")
    new_data = read_json(file) if append and os.path.isfile(file) else list()
    new_data.append(data)
    with open(file, 'w+', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)





def add_extension(file, extension):
    if not extension.startswith('.'):
        extension = '.' + extension
    return (file + extension) if not file.lower().endswith(extension) else file


def drop_extension(file):
    return file[:file.index('.')] if '.' in file else file


def file_exists(filepath, errmsg=None):
    """Enforces that filepath is a file"""

    if errmsg is None:
        errmsg = f"{filepath} is not a file!"
    assert os.path.isfile(filepath), errmsg


def dir_exists(dirpath):
    """Enforces that dirpath is a directory"""

    assert os.path.isdir(dirpath), f"{dirpath} is not a directory!"


def mkdir(dirpath):
    Path(dirpath).mkdir(exist_ok=True, parents=True)


def prep_paths(*files):
    for file in files:
        mkdir(os.path.dirname(file))


def check_and_make(*dirpaths, overwrite=False):
    for dirpath in dirpaths:
        if os.path.isdir(dirpath):
            if overwrite:
                shutil.rmtree(dirpath)
        if not os.path.isdir(dirpath):
            mkdir(dirpath)


def clear_files(*files):
    for file in files:
        Path(file).write_text("")


def read_pickle(filepath):
    """Reads a pickle file into appropriate object"""

    with open(filepath, 'rb') as f:
        return pickle.load(f)


def write_pickle(filepath, obj):
    """Writes an object to a pickle file"""

    with open(filepath, 'wb+') as f:
        pickle.dump(obj, f)


def add_line(path, line):
    """Adds a line to the end of a text file"""

    with open(path, 'a', encoding='utf-8') as f:
        f.write(line + '\n')
