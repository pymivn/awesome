#!/usr/bin/env python

import csv


def main():
    FORMAT = '* [{user}/{name}]({link}) - {description}'
    dr = csv.DictReader(open('projects.csv'),
                        ['link', 'description'],
                        delimiter=';')

    projects = []
    for project in dr:
        cleaned = project['link'].strip('/')
        project['user'], project['name'] = cleaned.split('/')[-2:]

        for k, v in project.items():
            project[k] = v.strip()
        projects.append(project)

    projects.sort(key=lambda x: x['name'].lower())
    formatted = []
    for project in projects:
        formatted.append(FORMAT.format(**project))

    projects = '\n'.join(formatted)

    blogs = []
    blogdr = csv.DictReader(open('blogs.csv'),
                            ['user', 'bloglink', 'description'],
                            delimiter=';')
    for blog in blogdr:
        cleaned = blog['user'].strip('/')
        blog['github'] = cleaned
        blog['user'] = cleaned.split('/')[-1]
        for k, v in blog.items():
            blog[k] = v.strip()
        blogs.append(blog)

    blogs.sort(key=lambda x: x['user'].lower())
    BLOG_FORMAT = '* [{user}]({github}) - {bloglink}: {description}'
    blogs = '\n'.join(BLOG_FORMAT.format(**blog) for blog in blogs)

    with open('template.tpl') as f:
        tpl = f.read()
    with open('README.md', 'w') as f:
        f.write(tpl.format(projects=projects, blogs=blogs))


if __name__ == "__main__":
    main()
