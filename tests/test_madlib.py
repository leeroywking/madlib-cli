import pytest
from madlib_cli.madlib import read_template, parse, merge, prompt_user


def test_wiring():
    assert True == True


def test_read_file():
    path = "./resources/template_example.txt"
    raw_text = read_template(path)
    assert isinstance(raw_text, str)


def test_read_blank_file():
    path = "./resources/blank.txt"
    raw_text = read_template(path)
    assert raw_text == ""


def test_parse():
    path = "./resources/template_example.txt"
    raw_text = read_template(path)
    list_entries = parse(raw_text)
    assert isinstance(list_entries, list)


def test_merge_istext():
    path = "./resources/template_example.txt"
    raw_text = read_template(path)
    list_entries = parse(raw_text)
    merged_text = merge(raw_text, list_entries)
    assert isinstance(merged_text, str)


def test_merge_hasNoCurlys():
    path = "./resources/template_example.txt"
    raw_text = read_template(path)
    list_entries = [i for i in range(22)]
    merged_text = merge(raw_text, list_entries)
    assert "{" not in merged_text
    assert "}" not in merged_text


def test_full_integ():
    path = './resources/one.txt'
    raw_text = read_template(path)
    list_entries = ["Lee-Roy"]
    merged_text = merge(raw_text, list_entries)
    assert merged_text == "Hello, my name is Lee-Roy!"


def test_bad_string_input():
    bad_string = "{ My name is {Name}"
    list_entries = parse(bad_string)
    merged_text = merge(bad_string, ["Lee-Roy"])
    assert merged_text != "My name is Lee-Roy"
