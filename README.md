# Project Title

Python script to extract the piece of the changelog that match with a specific project version 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

- Python 3
- pip
- virtualenv

### Installing

- `virtualenv -p python3 venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

Run the project

```bash
$ python main.py --help
$ python main.py --project-version=1.0.0 --filename=CHANGELOG.md
```

## Running the tests

The project does not currently include a test suite.
We will gladly accept contributions in this regard.

## Built With

* [pip](https://pypi.org/project/pip/) - The PyPA recommended tool for installing Python packages.
* [markdown_to_json](https://github.com/njvack/markdown-to-json) - A tool to turn Markdown into a nested JSON structure.

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Matteo Codogno** - *Initial work* - [papasmurf](https://github.com/papasmurf17)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


