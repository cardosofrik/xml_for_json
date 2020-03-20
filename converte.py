from xml.etree.ElementTree import parse
import json

def simpleScript(xml):
    data=[]
    xmldoc = parse(xml)
    for item in xmldoc.iterfind('IDRECORD'):
        goods_name = item.findtext('description')
        goods_code = item.findtext('id_tx')
        parent_code = item.findtext('class_id')

        notes = item.findtext('notes')
        print(" [ 1 ] =  Reading XML")
        data.append({   
          'notes': notes,
          'parent_code':parent_code,
          'level':'2',
          'goods_code': goods_code,
          'goods_name': goods_name, })
        print(" [ 2 ] = Writing format JSON")
        with open('new.json', 'w') as outfile:
            json.dump(data, outfile)
    print("I finished")


xml="idmanual (1).xml"
simpleScript(xml)


