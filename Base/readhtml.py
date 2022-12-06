import os
from datetime import datetime

from bs4 import BeautifulSoup
import urllib.request
idcounter=1
li_idcounter=[]
def printPassMsgWscreenshot(doc,scriptstatus,msg,screenName):
    #scriptstatus = doc.find('ul', id="scriptstatus")
    # <li hidden><i>user_screen_snapshot = </i><a href=""><img src="" height="100" width="160" align="middle"> Click to view full size</a></li>

    new_li = doc.new_tag("li")
    temp_li = doc.new_tag("li")
    temp_li['style'] = 'color: yellowgreen; font-size: 12pt; font-weight: bold;'
    temp_li.string = "Step Status: PASS   Message: "+msg
    scriptstatus.append(temp_li)
    br = doc.new_tag("br")
    scriptstatus.append(br)
    new_i = doc.new_tag("i")
    new_i.string = 'user_screen_snapshot = '
    new_li.append(new_i)
    new_a = doc.new_tag("a")
    new_a['href'] = screenName
    new_img = doc.new_tag("img")
    new_img['height'] = "100"
    new_img['width'] = "160"
    new_img['align'] = "middle"
    new_img.string = 'Click to view full size'
    new_a.append(new_img)
    new_li.append(new_a)
    # new_div.string="New Element"
    scriptstatus.append(new_li)

    br = doc.new_tag("br")
    scriptstatus.append(br)
    return doc
def printFailMsgWscreenshot(doc,scriptstatus,msg,screenName):
    global idcounter;
    global li_idcounter;
    new_li = doc.new_tag("li")
    temp_li = doc.new_tag("li")
    temp_li['style'] = 'color: red; font-size: 12pt; font-weight: bold;'
    temp_li['id']="Screen_"+str(idcounter)
    li_idcounter.append("Screen_" + str(idcounter))
    idcounter+=1
    temp_li.string = "Step Status: FAIL   Message: " + msg

    scriptstatus.append(temp_li)
    br = doc.new_tag("br")
    scriptstatus.append(br)
    new_i = doc.new_tag("i")
    new_i.string = 'user_screen_snapshot = '
    new_li.append(new_i)
    new_a = doc.new_tag("a")
    new_a['href'] = screenName
    new_img = doc.new_tag("img")
    new_img['height'] = "100"
    new_img['width'] = "160"
    new_img['align'] = "middle"
    new_img.string = 'Click to view full size'
    new_a.append(new_img)
    new_li.append(new_a)
    # new_div.string="New Element"
    scriptstatus.append(new_li)

    br = doc.new_tag("br")
    scriptstatus.append(br)
    return doc
def printFailMsgWoscreenshot(doc,scriptstatus,msg):
    global idcounter;
    global li_idcounter;
    temp_li = doc.new_tag("li")
    temp_li['style'] = 'color: red; font-size: 12pt; font-weight: bold;'
    temp_li['id'] = "Screen_" + str(idcounter)
    li_idcounter.append("Screen_" + str(idcounter))
    idcounter += 1
    temp_li.string = "Step Status: FAIL   Message: " + msg
    scriptstatus.append(temp_li)
    br = doc.new_tag("br")
    scriptstatus.append(br)
    return doc
def printPassMsgWoscreenshot(doc,scriptstatus,msg):
    temp_li = doc.new_tag("li")
    temp_li['style'] = 'color: yellowgreen; font-size: 12pt; font-weight: bold;'
    temp_li.string = "Step Status: PASS   Message: " + msg
    scriptstatus.append(temp_li)
    br = doc.new_tag("br")
    scriptstatus.append(br)
    return doc
def printInfoMsg(doc,scriptstatus,msg):
    temp_li = doc.new_tag("li")
    temp_li['style'] = 'color: blue; font-size: 12pt;'
    temp_li.string = "Step Status: PASS   Message: " + msg
    scriptstatus.append(temp_li)
    br = doc.new_tag("br")
    scriptstatus.append(br)
    return doc
def addTestcaseStatus(doc,tcDetails):
    status = doc.find('div', id="status")


    for i,data in enumerate(tcDetails):
        br1 = doc.new_tag("p")
        br1.string = data

        status.append(br1)
def addTestcasedetails(doc,starttime,endtime,logName):
    log = doc.find('table', id="log")
    tr = doc.new_tag("tr")
    td=doc.new_tag("td")
    tr.append(td)
    log.append(tr)
    #------------------------------
    #tr = doc.new_tag("tr")
    td = doc.new_tag("td")
    td['CLASS']="time"
    #td['id']='scripttime'
    td.string='Start Time:'+starttime
    tr.append(td)
    td = doc.new_tag("td")
    td['CLASS'] = "note"
    #td['id'] = 'scriptstart'
    td.string = 'Script Start: '+logName
    tr.append(td)
    log.append(tr)

    #-----------------------------
    tr = doc.new_tag("tr")
    td = doc.new_tag("td")
    td['COLSPAN']=3
    ul = doc.new_tag("ul")
    #scriptstatus = doc.find('ul', id="scriptstatus")
    printPassMsgWscreenshot(doc,ul,"It is a  Pass Message", "rational_ft_user1.jpg")
    printFailMsgWscreenshot(doc,ul,"It is a  Fail Message", "rational_ft_user1.jpg")
    printInfoMsg(doc,ul,"In is an Info Message")
    printPassMsgWoscreenshot(doc,ul,"It is a  Pass Message")
    printFailMsgWoscreenshot(doc, ul, "It is a  Fail Message")
    printInfoMsg(doc,ul,"In is an Info Message")
    td.append(ul)
    tr.append(td)
    log.append(tr)
    tr = doc.new_tag("tr")
    td = doc.new_tag("td")
    td['CLASS'] = "pass"
    td.string="Pass"
    tr.append(td)
    log.append(tr)
    td = doc.new_tag("td")
    td['CLASS'] = "time"
    td.string = "End Time: "+endtime
    tr.append(td)
    log.append(tr)
    td = doc.new_tag("td")
    td['CLASS'] = "note"
    td.string = "Script End: "+logName
    tr.append(td)
    log.append(tr)
    tr = doc.new_tag("tr")
    td = doc.new_tag("td")
    td['COLSPAN']=3
    ul = doc.new_tag("ul")
    li = doc.new_tag("li")
    i = doc.new_tag("i")
    i.string="script_name = "+logName
    li.append(i)
    ul.append(li)
    td.append(ul)
    tr.append(td)
    log.append(tr)
    return log

def addFailureDetails(doc,TestcaseDetails,logName):
    failures = doc.find('div', id="failures")

    br1=None
    for i, data in enumerate(TestcaseDetails):
        br1 = doc.new_tag("a")
        br1['href']="#"+data
        br1.string = logName + ": " + data
        br = doc.new_tag("br")
        br1.append(br)

        failures.append(br1)

def generateHtml(doc,filename):
    with open(filename, "w") as f:
        f.write(str(doc))
def readtemplate():
    print(os.getcwd())
    with open("../Template/log.html", "r") as f:
        doc = BeautifulSoup(f, "html.parser")
    return doc

def generateHtmlLog():
    doc=readtemplate()
    dateString = datetime.today().strftime('%d %m %Y')
    logscript=doc.find('td', id = "logscript")
    logscript.string=logscript.string+"Test Suit"
    tcDetails=["Pass: Testcase1","Pass: Testcase2","Pass: Testcase3","Fail: Testcase1","Fail: Testcase2","Fail: Testcase3","Fail: Testcase4"]
    tcDetails.sort()
    addTestcaseStatus(doc,tcDetails)
    addTestcasedetails(doc,dateString,dateString,"Script1")
    addTestcasedetails(doc,dateString,dateString,"Script2")
    addFailureDetails(doc,li_idcounter,"Script1")
    generateHtml(doc,"../Logs/test_signup/mynewfile.html")
generateHtmlLog()
