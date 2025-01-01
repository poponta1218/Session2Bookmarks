#!/usr/bin/env python
# vim: set ft=python:
import json
import sys
import time
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# TODO(poponta): split main function into smaller functions
# TODO(poponta): handle errors
# TODO(poponta): add docstrings to functions
# TODO(poponta): add help message


def main():
    with Path(sys.argv[1]).open() as f:  # TODO(poponta): parse command line arguments, use argparse module
        data = json.load(f)[0]

    windows = []
    for window in data["windows"]:
        tabs = [
            {"title": data["windows"][window][tab]["title"], "url": str(data["windows"][window][tab]["url"])}
            for tab in data["windows"][window]
        ]
        windowtitle = data["windowsInfo"][window]["title"]
        windows.append({"title": windowtitle, "tabs": tabs})

    env = Environment(loader=FileSystemLoader(Path(__file__).parent.joinpath("template")), autoescape=True)
    template = env.get_template("template.html")

    render_data = {
        "time": round(time.time() * 1000),
        "timestamp": time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()),
        "windows": windows,
    }

    with Path(f"bookmarks-{render_data["timestamp"]}.html").open("w") as f:
        f.write(template.render(render_data))


if __name__ == "__main__":
    main()
