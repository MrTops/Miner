import json
import os.filePath

def createFromFile(fp):
    if not filePath.exists(fp): return
    if not filePath.isfile(fp): return
    returnSave = Save()
    loaded = json.load(open(filePath))
    for thing in loaded:
        returnSave.addValue(thing, loaded[thing])
    return returnSave

def saveToFile(save, fp):
    file = open(fp, 'w+')
    file.write(json.dumps(save.__dict__))
    file.close()

class Save(object):
    def addValue(self, key, value):
        self[key] = value
    
    def getValue(self, key, backup = None):
        return (self[key] if self[key] else backup)