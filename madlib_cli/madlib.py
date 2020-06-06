import re


def parse(raw_paragraph: str) -> [str]:
    """
    function that takes in a path to text file and returns a stripped string of the file’s contents.
    """
    entries = re.findall(r'\{.*?\}', raw_paragraph)            
    return entries


def read_template(path: str) -> str:
    try:
        with open(path, "r") as file:
            raw_paragraph = file.read()
    except FileNotFoundError:
        print("incorrect path")
    """
    function that takes in a template string and returns a string with language parts removed and a separate list of those language parts
    """
    return raw_paragraph


def merge(template: str, user_entries: list) -> str:
    """
    function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template
    """
    template = re.sub(r'\{.*?\}', '{}', template).format(*user_entries)
    return template


def prompt_user(blanks: [str]) -> [str]:
    responses = []
    for blank in blanks:
        new = input(f"Please enter a/an {blank}: ")
        responses.append(new)
    return responses


def main():
    path = input("file path for template?:")
    raw_template = read_template(path)
    entries = parse(raw_template)
    responses = prompt_user(entries)
    output = merge(raw_template, responses)
    print(output)


if __name__ == "__main__":
    main()