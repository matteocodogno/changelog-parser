#!/usr/local/bin/python

import re
import argparse

from markdown_to_json.markdown_to_json import Renderer, CMarkASTNester
from markdown_to_json.scripts.md_to_json import get_markdown_ast


def convert_changelog_to_json(file_name):
    nester = CMarkASTNester()
    renderer = Renderer()
    ast = get_markdown_ast(file_name)
    nested = nester.nest(ast)

    return renderer.stringify_dict(nested)


def release_dict_to_markdown(release_dict):
    lines = ['# CHANGELOG', '']
    for key, values in release_dict.items():
        lines.append(f'## {key}')
        for value in values:
            lines.append(f' - {value}')
        lines.append('')

    return '\n'.join(lines)


def extract_release_by_name(changelog_dict, partial_name='1.0.0'):
    changelog_regex = rf'^\[{partial_name.strip("[]")}[^]]*\]'
    release_dict, = [value for key, value in changelog_dict.items() if re.match(changelog_regex, key, re.IGNORECASE)]

    return release_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract a specific release from changelog')
    parser.add_argument('--project-version', default='Unreleased',
                        help='Project version to be extracted (default: Unreleased)')
    parser.add_argument('--filename', default='./CHANGELOG.md',
                        help='Path to CHANGELOG file')

    args = parser.parse_args()

    changelog_dict, = list(convert_changelog_to_json(args.filename).values())
    release_dict = extract_release_by_name(changelog_dict, args.project_version)
    print(release_dict_to_markdown(release_dict))

