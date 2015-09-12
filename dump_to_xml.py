import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supportNotebook.settings')

import django
django.setup()

from django.db import models

from responseTemplates.models import ResponseTemplate
from taggit.managers import TaggableManager

import xml.etree.ElementTree as ET


def dumpToXml():
    top = ET.Element('root')
    qr = ResponseTemplate.objects.all()
    for obj in qr:
        entry = ET.SubElement(top, 'Entry')
        tagsNode = ET.SubElement(entry, 'tags')
        tagsNode.text = str(obj.tags.names())
        textNode = ET.SubElement(entry, 'text')
        for p in obj.paragraph_set.all():
            pnode = ET.SubElement(textNode, 'p')
            pnode.text = p.text
    ET.ElementTree(top).write('DB_DUMP.xml')


if __name__ == '__main__':
    print("Starting dump")
    dumpToXml()
