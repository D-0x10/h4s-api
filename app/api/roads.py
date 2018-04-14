from app import app
from app.tsn import accidents
import json
from app.common.sortedList import sortedList

@app.route('/api/roads')
def roads():
    return sortedList(20, lambda item: item['Olycksvag'], True)

@app.route('/api/roads2')
def municipality():
    return sortedList(20, lambda item: item['Kommun'], True)