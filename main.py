#!/usr/bin/env python

import csv


def main():
    FORMAT = '* [{user}/{name}]({link}) - {description}'
    dr = csv.DictReader(open('projects.csv'),
                        ['link', 'description'],
                        delimiter=';')

    projects = []
    for project in dr:
        project['user'], project['name'] = project['link'].split('/')[-2:]

        for k, v in project.items():
            project[k] = v.strip()
        projects.append(project)

    projects.sort(key=lambda x: x['name'])
    formatted = []
    for project in projects:
        formatted.append(FORMAT.format(**project))

    projects = '\n'.join(formatted)
    with open('template.tpl') as f:
        tpl = f.read()
    with open('README.md', 'w') as f:
        f.write(tpl.format(projects=projects))


if __name__ == "__main__":
    main()
