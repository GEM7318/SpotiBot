
import os
import re


def __main__():
    """One time utility script ran for changes in attribute instantiation.

    This script performs the below, one-time conversion on all attributes of
    SpotiBot classes - this is done so that the same codes can instantiate
    json API responses and serialized objects stored in MongoDB without any
    other changes to the data model.

        .. code-block:: python

               class.get('attr')  # original

               object_handler(class, 'attr')  # revised


    Date: 2020-06-11
    """
    spotibot_root = os.path.join(os.getcwd(), 'spotibot')

    files_to_convert = \
        [os.path.join(dirpath, file) for dirpath, dirnames, files
         in os.walk(spotibot_root, topdown=False) for file in files
         if file not in [r'__init__.py', r'__main__.py']
         and 'cache' not in re.escape(dirpath)
         and 'utils' not in re.escape(dirpath)]

    # / Exporting list of files to convert into autodocs directory /
    wr_path = os.path.join(os.getcwd(), 'src_autodoc', '20200610~1.txt')
    assert not os.path.isfile(wr_path)
    with open(wr_path, 'w') as f:
        f.write('\n'.join([re.escape(file) for file in files_to_convert]))

    # / Continuing replacement logic /
    pattern = re.compile(r"(.*self\.\w+:\s\w+\s=\s\\\n\s+)[^self]"
                         r"\s+(\w+)\.get\(('\w+')\)")

    for file in files_to_convert:
        with open(file, 'r') as r:
            obj_py = r.read()

        conv_py = pattern.sub(r"\1object_handler(\2, \3)", obj_py)

        with open(file, 'w') as w:
            w.write(conv_py)
        print(f"Written modified file to:\n\t{file}\n")


if __name__ == '__main__':
    __main__()
