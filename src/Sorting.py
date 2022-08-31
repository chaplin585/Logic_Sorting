from openpyxl import Workbook
import openpyxl

def sort_main_file():
   

    
    i = 2
    j = 2
    m = 1
    z = 0
    end = 0
    cnt1 = 0
    cnt2 = 1
    test1 = ''
    test2 = ''
    wb1 = openpyxl.reader.excel.load_workbook(filename = 'Google Data.xlsx')
    wb2 = openpyxl.reader.excel.load_workbook(filename = 'Main.xlsx')
    ws2 = wb2.active
    ws1 = wb1.active
    while ws1['A'+str(i)].value or ws1['A'+str(i+1)].value != None:
        i+=1
        if ws1['A'+str(i)].value == None:
            i+=1
        else:
            if ws1['B'+str(i)].value == 'Начало маршрута':
                cnt1 = 0  
                ws2['A'+str(j)].value = ws1['A'+str(i)].value
                ws2['B'+str(j)].value = ws1['C'+str(i)].value
                ws2['C'+str(j)].value = ws1['D'+str(i)].value
                ws2['D'+str(j)].value = ws1['E'+str(i)].value
                ws2['E'+str(j)].value = int(ws1['F'+str(i)].value)
                m = i                
                while ws1['A'+str(m)].value or ws1['A'+str(m+1)].value != None :
                    if ws1['A'+str(m)].value == None:
                        m+=1
                    else:
                        if ws1['B'+str(m)].value == 'Конец маршрута'and cnt1 == 0:
                            ws2['H'+str(j)].value = ws1['A'+str(m)].value
                            ws2['I'+str(j)].value = ws1['J'+str(m)].value
                            ws2['J'+str(j)].value = ws1['K'+str(m)].value
                            ws2['K'+str(j)].value = ws1['L'+str(m)].value
                            z = i
                            while z < m:
                                if ws1['A'+str(z)].value == None:
                                    z+=1
                                else:
                                    if ws1['B'+str(z)].value == 'Заправка авто':
                                        if cnt2 == 1:
                                            pass
                                        else:
                                            j+=1
                                        ws2['F'+str(j)].value = ws1['A'+str(z)].value
                                        ws2['G'+str(j)].value = ws1['H'+str(z)].value                                        
                                        cnt2+=1
                                    z+=1       
                            cnt2 = 1  
                            cnt1+=1
                    m+=1
                j+=1
    wb1.save("sample.xlsx")
    wb2.save("main.xlsx")
    wb1.close()
    wb2.close()
    print(1)


