import requests
from bs4 import BeautifulSoup
import re
import os
from textwrap import TextWrapper
from io import StringIO
from html.parser import HTMLParser
import string


def __main__():
    """Script parses API documentation into Google style docstrings.

    End output is the 'Object Model Auto-Generated Docstrings.md' file
    containing all class docstrings which are then added to all SpotiBot
    classes that directly mirror the Spotify object model.
    """

    def next_element(elem):
        while elem is not None:
            # Find next element, skip NavigableString objects
            elem = elem.next_sibling
            if hasattr(elem, 'name'):
                return elem

    def get_pages(tags, header='h3'):
        pages = []
        for tag in tags:
            page = [str(tag)]
            elem = next_element(tag)
            while elem and elem.name != header:
                page.append(str(elem))
                elem = next_element(elem)
            pages.append('\n'.join(page))

        return pages

    def get_table_val_dict(pages, header):

        table_dict = {}
        for page in pages:

            id = re.findall(f'>(.*)</{header}>', page)
            if id:
                soupified = BeautifulSoup(page, 'html.parser')
                table_dict[id[0]] = soupified
            else:
                pass

        table_dict = {k: v for k, v in table_dict.items()
                      if not re.findall('/', k) and k != 'Example'}

        table_val_dict = {}
        for head, soup in table_dict.items():
            cols = soup.find_all('tr').__str__().split(r'</tr>')
            cols = [re.findall(r'<td\>(.*)</td>', col) for col in cols
                    if re.findall(r'<td\>(.*)</td>', col)]
            fields = {}
            for col in cols:

                if len(col) == 3:
                    name, typ, desc = col
                    desc = \
                        desc.__str__() \
                            .replace(r'<code class="highlighter-rouge">', '``') \
                            .replace(r'</code>', '``')
                    fields[name] = {'type': typ,
                                    'description': desc}

            if fields:
                table_val_dict[head] = fields
            else:
                pass

        return table_val_dict

    def field_dict_from_href(href, header='h3'):
        response = requests.get(href)

        soup = BeautifulSoup(response.text, 'html.parser')

        tags = soup.find_all(header)

        pages = get_pages(tags, header=header)

        field_dict = get_table_val_dict(pages, header=header)

        return field_dict, soup

    class MLStripper(HTMLParser):
        """
        Note: Code directly vendor'd in from the following link
            https://stackoverflow.com/questions/753052/strip
            -html-from-strings-in-python
        """

        def __init__(self):
            super().__init__()
            self.reset()
            self.strict = False
            self.convert_charrefs = True
            self.text = StringIO()

        def handle_data(self, d):
            self.text.write(d)

        def get_data(self):
            return self.text.getvalue()

    def strip_tags(html):
        s = MLStripper()
        s.feed(html)
        return s.get_data()

    class Desc:

        def __init__(self, desc: str):
            # self.desc = desc
            # TODO: Do all the stripping of links and stuff at this level

            self.original = \
                desc

            self.stripped = \
                strip_tags(''.join(
                    char for char in desc if char in string.printable))

    class Typ:

        def __init__(self, typ):
            self.types = \
                {'boolean': 'bool',
                 'string': 'str',
                 'integer': 'int'}

            self.original = \
                typ

            self.revised = \
                self.types.get(typ, typ)

    class Name:

        def __init__(self, name):
            self.original = \
                name

            self.stripped = \
                strip_tags(''.join(
                    char for char in name if char in string.printable))

    class Attr(Name):

        def __init__(self, name: str, attrs):
            super().__init__(name)

            self.type: Typ = \
                Typ(attrs.get('type'))

            self.desc = \
                Desc(attrs.get('description'))

    class Wrapper:
        attr_wrapper = \
            TextWrapper(width=66, fix_sentence_endings=True, tabsize=4,
                        initial_indent='\t\t',
                        subsequent_indent='\t\t\t')
        other_wrapper = \
            TextWrapper(width=66, fix_sentence_endings=True,
                        initial_indent='\t', subsequent_indent='\t', tabsize=4)

        def __init__(self, raw: str):
            self.stripped = strip_tags(raw)

            self.attr = \
                '\n'.join(self.attr_wrapper.wrap(self.stripped))

            self.other = \
                '\n'.join(self.other_wrapper.wrap(self.stripped)). \
                    lstrip(' ').rstrip(' ')

    class Doc(Attr):
        wrapper = TextWrapper(width=66, fix_sentence_endings=True,
                              initial_indent='\t\t',
                              subsequent_indent='\t\t\t',
                              tabsize=4)

        def __init__(self, name, attrs):
            super().__init__(name, attrs)

            self.full = \
                f"{self.stripped} ({self.type.revised}): {self.desc.stripped}"

            self.param = Wrapper(self.full).attr

    class Item:

        def __init__(self, name, attrs: dict):
            self.name = \
                name

            self.spotibot_api_xref = \
                {}

            self.spotibot = \
                self.spotibot_api_xref.get(name)

            self.docs = [Doc(k, v) for k, v in attrs.items()]

            self.header = \
                Wrapper(
                    f'"""Auto-generated attribute instantiation docstring for '
                    f'{name}').other + '\n\n'

            self.disclaimer = \
                Wrapper(
                    f"Note: Parameter description in below docstring is "
                    f"populated based on the\n descriptions at the following "
                    f"link:\n\thttps://developer.spotify.com/documentation/web"
                    f"-api/reference/object-model").other + '\n\n'

            self.guidance = \
                Wrapper(
                    f"Please consult their official documentation for more "
                    f"in-depth information & full-linking across pages.") \
                    .other + '\n\n'

            self.attrs = [attr.param for attr in self.docs]

            self.docstring = \
                self.header + self.disclaimer + self.guidance \
                + '\tAttributes:\n' + '\n'.join(self.attrs)

            self.md = \
                f'### {name.title()}' \
                f'\n```python\n{self.docstring}\n\t"""\n```'

    class Model:

        def __init__(self, objects: dict):

            self.objs = {}
            for obj_name, obj_attrs in objects.items():
                self.objs[obj_name] = Item(obj_name, obj_attrs)

            self.markdowns = \
                [obj.md for obj in self.objs.values()]

        def to_md(self, path_to_write='') -> None:
            """Combines all markdown objects and writes to a .md file.

            Args:
                path_to_write: Full file path to write to
            """
            self.path_to_write = path_to_write

            if not self.path_to_write:
                self.path_to_write = \
                    os.path.join(os.getcwd(),
                                 'Object Model Auto-Generated Docstrings.md')

            with open(self.path_to_write, 'w') as f:
                f.write('\n\n'.join(self.markdowns))

            return None

    href = r'https://developer.spotify.com/documentation' \
           r'/web-api/reference/object-model/#track-object-' \
           r'full'

    href2 = r'https://developer.spotify.com/documentation/web' \
            r'-api/reference/player/get-information-about-the-' \
            r'users-current-playback/'

    # Url to API documentation for majority of objects
    track, soup1 = \
        field_dict_from_href(href, header='h2')

    # Url to API documentation for current playback objects
    other, soup2 = \
        field_dict_from_href(href2, header='h3')

    # Combining all docs
    total = {**track, **other}

    # Exporting to 'Object Model Auto-Generated Docstrings.md'
    Model(total).to_md()


if __name__ == '__main__':
    __main__()
