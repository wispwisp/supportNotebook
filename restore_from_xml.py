import ast

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supportNotebook.settings')

import django
django.setup()

from django.db import models
from responseTemplates.models import ResponseTemplate, Paragraph
from taggit.managers import TaggableManager

import xml.etree.ElementTree as ET

def restoreFromXml():
    tree = ET.parse('DB_DUMP.xml')
    root = tree.getroot()
    for entry in root.findall('Entry'):

        # template:
        tmpl = ResponseTemplate()
        tmpl.save()

        for tag in ast.literal_eval(entry.find('tags').text):
            tmpl.tags.add(tag)
        tmpl.save()

        # paragraphs:
        for p in entry.find('text'):
            _text = p.text
            p = Paragraph(
                template = tmpl,
                text = _text
            )
            p.save()

if __name__ == '__main__':
    print("Starting dump")
    restoreFromXml()
