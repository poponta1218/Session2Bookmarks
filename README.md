# Session2Bookmarks

This Python script processes JSON data exported from [Tab-Session-Manager](https://github.com/sienori/Tab-Session-Manager).  
This tool converts browser session JSON files exported from Tab-Session-Manager into a bookmarks HTML file.

## Prerequisites

### Python Version

- Python 3.7 or higher is required to run this script.

### Python Packages

- `jinja2`
- and its dependencies

Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

Generate the virtual environment using uv:

```bash
uv sync
```

## Usage

### Command-Line Arguments

The script expects the following arguments:

- **Input JSON file**: Path to the JSON file containing the session data.

### Example

```bash
python session2bookmark.py [INPUT FILE]
```

This will generate an HTML file named `bookmarks-<YY-MM-DD_HH:mm:ss>.html` in the current directory.

## License

This script is distributed under the MIT License. See `LICENSE` for more details.
