# -*- coding: utf-8 -*-
import json
import gspread
#from oauth2client.client import SignedJwtAssertionCredentials

def openWorkBook():
    # where is the authentication file
    file = 'PartialTrialData-84690d0d6711.json'
    # read the authentication file
    json_key = json.load(open((file)))
    scope = ['https://spreadsheets.google.com/feeds']
    # get my credentials
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
    # apply credentials
    gc = gspread.authorize(credentials)
    # what spreadsheet am I working with.
    # Note, I had to share this with myself.
    SS = '1hAVmDKE1rli9me-VJWSAJCBoxtvfgvrXF_RhQqcawUk'
    # See here for details: https://github.com/burnash/gspread
    # open workbook
    wkB = gc.open_by_key(SS)
    return wkB

def createWorksheet(workBook, subid):
    
    # Create a worksheet for this participant
    #subid = '2001'
    worksheetName = 'behData_%s'%(subid)
    workBook.add_worksheet(title=worksheetName, rows="100", cols="20")
    # select the worksheet
    wkS = workBook.worksheet(worksheetName)
    # Write subid to worksheet
    wkS.update_cell(1, 1, 'subid')
    wkS.update_cell(1, 2, subid)
    return wkS

def writeData(workSheet, data, col, rowStart,colTitle):
    # write a title for this colume of data
    workSheet.update_cell(rowStart, col, colTitle)
    count = 1
    for i in data:
        workSheet.update_cell(rowStart + count, col, i)
        count = count + 1
        


#Go to Google Sheets and share your spreadsheet with an email you have in your json_key['client_email']. Otherwise you’ll get a SpreadsheetNotFound exception when trying to open it.