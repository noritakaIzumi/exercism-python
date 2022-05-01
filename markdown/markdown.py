"""Markdown"""
import re


def get_heading_rank(line: str) -> int:
    """

    :param line:
    :return:
    """
    m = re.match('(#{1,6}) (.*)', line)
    if m is not None:
        return len(m.group(1))
    return 0


def convert_heading(curr: str) -> str:
    """

    :param curr:
    :return:
    """
    r = get_heading_rank(curr)
    if r > 0:
        return f'<h{r}>{curr[r + 1:]}</h{r}>'
    return curr


def convert_bold(curr: str) -> str:
    """

    :param curr:
    :return:
    """
    m = re.match('(.*)__(.*)__(.*)', curr)
    if m:
        return m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
    return curr


def convert_italic(curr: str) -> str:
    """

    :param curr:
    :return:
    """
    m = re.match('(.*)_(.*)_(.*)', curr)
    if m:
        return m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
    return curr


def convert_bold_and_italic(curr: str) -> str:
    """

    :param curr:
    :return:
    """
    return convert_italic(convert_bold(curr))


def surround_by_tag_name(line: str, tag_name: str) -> str:
    """

    :param line:
    :param tag_name:
    :return:
    """
    return f'<{tag_name}>{line}</{tag_name}>'


def parse(markdown: str) -> str:
    """

    :param markdown:
    :return:
    """
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        i = convert_heading(i)
        m = re.match(r'\* (.*)', i)
        if m is not None:
            tmp = ''
            if not in_list:
                tmp = '<ul>'
                in_list = True
            i = tmp + surround_by_tag_name(m.group(1), 'li')
        else:
            if in_list:
                in_list_append = True
                in_list = False
            if not re.match('<h|<ul|<p|<li', i):
                i = surround_by_tag_name(i, 'p')
            if in_list_append:
                i = '</ul>' + i
                in_list_append = False
        res += convert_bold_and_italic(i)
    if in_list:
        res += '</ul>'
    return res
