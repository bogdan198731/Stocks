from openpyxl import load_workbook
import win32com.client


def openExcel(filename):
    xl = win32com.client.Dispatch("Excel.Application")  # instantiate excel app

#    wb = xl.Workbooks.Open(r'C:/Users/bogda/Desktop/stocks4.xlsm')
    wb = xl.Workbooks.Open('C:/Users/bogda/Desktop/stocks4.xlsm')
    #    comanda=filename +
    xl.Application.Run('stocks4.xlsm!Module1.Copy')
    wb.Save()
    xl.Application.Quit()


def openExcel2(filename):
    xl = win32com.client.Dispatch("Excel.Application")  # instantiate excel app

    wb = xl.Workbooks.Open(r'C:/Users/bogda/Desktop/stocks4.xlsm')
    #    comanda=filename +
    xl.Application.Run('stocks4.xlsm!Module1.Delete')
    wb.Save()
    xl.Application.Quit()

def closeExcel(filename):
    xl = win32com.client.Dispatch("Excel.Application")  # instantiate excel app
    wb = xl.Workbooks.Open('C:/Users/bogda/Desktop/stocks4.xlsm')
    wb.Save()
    xl.Application.Quit()


