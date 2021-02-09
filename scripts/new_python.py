import os
import requests
import argparse


PROG = "new-python-project"
VERSION = "1.0.0"

SETUP_PY = "https://raw.githubusercontent.com/olichose123/scripts-and-files/main/templates/setup.py"  # noqa E501
PYPROJECT_TOML = "https://raw.githubusercontent.com/olichose123/scripts-and-files/main/templates/pyproject.toml"  # noqa E501
README_MD = "https://raw.githubusercontent.com/olichose123/scripts-and-files/main/templates/readme.md"  # noqa E501
LICENSE = "https://raw.githubusercontent.com/olichose123/scripts-and-files/main/licenses/MIT-license.txt"  # noqa E501


class Error(Exception):
    pass


def fetch(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Error("failed to download file at {}".format(url))
    else:
        return response.text


def create_file(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as file:
        file.write(content)


parser = argparse.ArgumentParser(
    prog=PROG,
    description="Start a new python project",
)
parser.add_argument("-n", "--name", help="package name")
parser.add_argument("-u", "--username", help="pypi username", default=None)
parser.add_argument("-a", "--author", help="package author", default=None)
parser.add_argument("-e", "--email", help="author email", default=None)
parser.add_argument("-d", "--desc", help="package description", default=None)
parser.add_argument("-v", "--pkgver", help="package version", default="0.0.1")
parser.add_argument("--pyver", help="python version", default=">=3.6")
parser.add_argument(
    "--version", action="version", version="{} {}".format(PROG, VERSION)
)


def input_if_null(value, term):
    if value is None:
        return input(term + ": ")
    else:
        return value


def run():
    args = parser.parse_args()
    args.name = input_if_null(args.name, "Package name")
    if not args.name.isidentifier():
        raise Error("name {} is not a valid package name".format(args.name))
    args.desc = input_if_null(args.desc, "Package description")
    args.username = input_if_null(args.username, "Pypi username")
    args.author = input_if_null(args.author, "Package author")
    args.email = input_if_null(args.email, "Author email")

    data = {
        "year": "",
        "author": args.author,
        "holder": args.author,
        "package_name": args.name,
        "username": args.username,
        "email": args.email,
        "description": args.desc,
        "url": "",
        "version": args.pkgver,
        "python_version": args.pyver,
    }

    folder = "{}-{}/".format(args.name, args.username)
    src = "{}/{}/".format(folder, args.name)
    tests = "{}/tests/".format(folder)

    create_file(src + "__init__.py", "")
    create_file(tests + "__init__.py", "")
    create_file(folder + "README.md", fetch(README_MD).format(**data))
    create_file(folder + "LICENSE", fetch(LICENSE).format(**data))
    create_file(folder + "setup.py", fetch(SETUP_PY).format(**data))
    create_file(
        folder + "pyproject.toml",
        fetch(PYPROJECT_TOML).format(**data),
    )

    print("package created")


run()
