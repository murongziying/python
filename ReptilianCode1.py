#-*- coding:utf-8 -*-
#! /usr/bin/python3
import sys, time, os,string
import mechanize
import urlparse
from BeautifulSoup import BeautifulSoup
import re
import MySQLdb
import logging
import cgi
from optparse import OptionParser
#----------------------------------------------------------------------------#
# Name:    TySpider.py                              #
# Purpose:   WebSite Spider Module                     #
# Author:   刘天斯                                   #
# Email:    liutiansi@gamil.com                         #
# Created:   2010/02/16                              #
# Copyright:  (c) 2010                                #
#----------------------------------------------------------------------------#
 
 
"""
|--------------------------------------------------------------------------
| 定义 loging class;
|--------------------------------------------------------------------------
|
| 功能：记录系统相关日志信息。
| 
|
"""
class Pubclilog():
  def __init__(self):
    self.logfile = 'website_log.txt'
 
  def iniLog(self):
    logger = logging.getLogger()
    filehandler = logging.FileHandler(self.logfile)
    streamhandler = logging.StreamHandler()
    fmt = logging.Formatter('%(asctime)s, %(funcName)s, %(message)s')
    logger.setLevel(logging.DEBUG) 
    logger.addHandler(filehandler) 
    logger.addHandler(streamhandler)
    return [logger,filehandler]
 
 
"""
|--------------------------------------------------------------------------
| 定义 tySpider class;
|--------------------------------------------------------------------------
|
| 功能：抓取分类、标题等信息
| 
|
"""
class BaseTySpider:
 
  #初始化相关成员方法
  def __init__(self,X,log_switch):
 
    #数据库连接
    self.conn = MySQLdb.connect(db='dbname',host='192.168.0.10', user='dbuser',passwd='SDFlkj934y5jsdgfjh435',charset='utf8')
 
    #分类及标题页面Community
    self.CLASS_URL = 'http://test.abc.com/aa/CommTopicsPage?'
 
    #发表回复页
    self.Content_URL = 'http://test.bac.com/aa/CommMsgsPage?'
 
    #开始comm值
    self.X=X
 
    #当前comm id取模，方面平均到表
    self.mod=self.X%5
 
    #Community文件下载页
    self.body=""
 
    #self.bodySoup对象
    self.soup=None
 
    #发表回复页下载内容变量
    self.Contentbody=""
 
    #发表回复页内容self.ContentbodySoup对象
    self.Contentsoup=None
 
    #日志开关
    self.log_switch=log_switch
 
 
  #======================获取名称及分类方法==========================
  def _SpiderClass(self,nextpage=None):
    if nextpage==None:
      FIXED_QUERY = 'cmm='+str(self.X)
    else:
      FIXED_QUERY = nextpage[1:]
 
    try:
      rd = mechanize.Browser()
      rd.addheaders = [("User-agent", "Tianya/2010 (compatible; MSIE 6.0;Windows NT 5.1)")]
      rd.open(self.CLASS_URL + FIXED_QUERY)
      self.body=rd.response().read()
      #rd=mechanize.Request(self.CLASS_URL + FIXED_QUERY)
      #response = mechanize.urlopen(rd)
      #self.body=response.read()
 
    except Exception,e:
      if self.log_switch=="on":
        logapp=Pubclilog()
        logger,hdlr = logapp.iniLog()
        logger.info(self.CLASS_URL + FIXED_QUERY+str(e))
        hdlr.flush()
        logger.removeHandler(hdlr)
        return
    self.soup = BeautifulSoup(self.body)
    NextPageObj= self.soup("a", {'class' : re.compile("fs-paging-item fs-paging-next")})
    self.cursor = self.conn.cursor()
    if nextpage==None:
      try:
        Ttag=str(self.soup.table)
        #print Ttag
 
        """
        ------------------分析结构体-----------------
        <table cellspacing="0" cellpadding="0">
          <tr>
            <td>
              <h1 title="Dunhill">Dunhill</h1>
            </td>
            <td valign="middle">
              <div class="fs-comm-cat">
                <span class="fs-icons fs-icon-cat"> </span> <a href="TopByCategoryPage?cid=211&ref=commnav-cat">中国</a> » <a href="TopByCategoryPage?cid=211&subcid=273&ref=commnav-cat">人民</a>
              </div>
            </td>
          </tr>
        </table>
        """
 
        soupTable=BeautifulSoup(Ttag)
 
        #定位到第一个h1标签
        tableh1 = soupTable("h1")
        #print self.X
        #print "Name:"+tableh1[0].string.strip().encode('utf-8')
 
        #处理无类型的
        try:
          #定位到表格中符合规则“^TopByCategory”A链接块，tablea[0]为第一个符合条件的连接文字，tablea[1]...
          tablea = soupTable("a", {'href' : re.compile("^TopByCategory")})
          if tablea[0].string.strip()=="":
            pass
          #print "BigCLass:"+tablea[0].string.strip().encode('utf-8')
          #print "SubClass:"+tablea[1].string.strip().encode('utf-8')
        except Exception,e:
          if self.log_switch=="on":
            logapp=Pubclilog()
            logger,hdlr = logapp.iniLog()
            logger.info("[noClassInfo]"+str(self.X)+str(e))
            hdlr.flush()
            logger.removeHandler(hdlr)
          self.cursor.execute("insert into baname"+str(self.mod)+" values('%d','%d','%s')" %(self.X,-1,tableh1[0].string.strip().encode('utf-8')))
          self.conn.commit() 
          self._SpiderTitle()
          if NextPageObj:
            NextPageURL=NextPageObj[0]['href']
            self._SpiderClass(NextPageURL)
            return
          else:
            return
 
 
        #获取链接二对象的href值
        classlink=tablea[1]['href']
        par_dict=cgi.parse_qs(urlparse.urlparse(classlink).query)
        #print "CID:"+par_dict["cid"][0]
        #print "SubCID:"+par_dict["subcid"][0]
        #print "---------------------------------------"
         
        #插入数据库
        self.cursor.execute("insert into class values('%d','%s')" %(int(par_dict["cid"][0]),tablea[0].string.strip().encode('utf-8')))
        self.cursor.execute("insert into subclass values('%d','%d','%s')" %(int(par_dict["subcid"][0]),int(par_dict["cid"][0]),tablea[1].string.strip().encode('utf-8'))) 
        self.cursor.execute("insert into baname"+str(self.mod)+" values('%d','%d','%s')" %(self.X,int(par_dict["subcid"][0]),tableh1[0].string.strip().encode('utf-8')))
        self.conn.commit() 
         
        self._SpiderTitle()
        if NextPageObj:
          NextPageURL=NextPageObj[0]['href']
          self._SpiderClass(NextPageURL)
 
        self.body=None
        self.soup=None
        Ttag=None
        soupTable=None
        table=None
        table1=None
        classlink=None
        par_dict=None
      except Exception,e:
        if self.log_switch=="on":
          logapp=Pubclilog()
          logger,hdlr = logapp.iniLog()
          logger.info("[ClassInfo]"+str(self.X)+str(e))
          hdlr.flush()
          logger.removeHandler(hdlr)
    else:
      self._SpiderTitle()
      if NextPageObj:
        NextPageURL=NextPageObj[0]['href']
        self._SpiderClass(NextPageURL)
 
 
 
 
  #====================获取标题方法=========================
  def _SpiderTitle(self):
    #查找标题表格对象(table)
    soupTitleTable=self.soup("table", {'class' : "fs-topic-list"})
     
    #查找标题行对象(tr)
    TitleTr = soupTitleTable[0]("tr", {'onmouseover' : re.compile("^this\.className='fs-row-hover'")})
    """
    -----------分析结构体--------------
    <tr class="fs-alt-row" onmouseover="this.className='fs-row-hover'" onmouseout="this.className='fs-alt-row'">
      <td valign="middle" class="fs-hot-topic-dots-ctn">
        <div class="fs-hot-topic-dots" style="background-position:0 -0px" title="点击量：12"></div>
      </td>
      <td valign="middle" class="fs-topic-name">
        <a href="CommMsgsPage?cmm=16081&tid=2718969307756232842&ref=regulartopics" id="a53" title="【新人报到】欢迎美国人民加入" target="_blank">【新人报到】欢迎美国人民加入</a>
        <span class="fs-meta">
        <span class="fs-icons fs-icon-mini-reply"> </span>0
         /
         <span class="fs-icons fs-icon-pageview"> </span>12</span>
      </td>
      <td valign="middle">
        <a class="fs-tiny-user-avatar umhook " href="ProfilePage?uid=8765915421039908242" title="中国人"><img src="http://img1.sohu.com.cn/aa/images/138/0/P/1/s.jpg" /></a>
      </td>
      <td valign="middle" style="padding-left:4px">
        <a href="Profile?uid=8765915421039908242" id="b53" title="中国人" class="umhook">中国人</a>
      </td>
      <td valign="middle" class="fs-topic-last-mdfy fs-meta">2-14</td>
    </tr>
    """
    for CurrTr in TitleTr:
      try:
        #初始化置顶及精华状态
        Title_starred='N'
        Title_sticky='N'
 
        #获取当前记录的BeautifulSoup对象
        soupCurrTr=BeautifulSoup(str(CurrTr))
 
        #BeautifulSoup分析HTML有误，只能通过span的标志数来获取贴子状态，会存在一定误差
        #如只有精华时也会当成置顶来处理。
        TitleStatus=soupCurrTr("span", {'title' : ""})
        TitlePhotoViewer=soupCurrTr("a", {'href' : re.compile("^PhotoViewer")})
        if TitlePhotoViewer.__len__()==1:
          TitlePhotoViewerBool=0
        else:
          TitlePhotoViewerBool=1
        if TitleStatus.__len__()==3-TitlePhotoViewerBool:
          Title_starred='Y'
          Title_sticky='Y'
        elif TitleStatus.__len__()==2-TitlePhotoViewerBool:
          Title_sticky='Y'
 
        #获取贴子标题
        Title=soupCurrTr.a.next.strip()
 
        #获取贴子ID
        par_dict=cgi.parse_qs(urlparse.urlparse(soupCurrTr.a['href']).query)
 
        #获取回复数及浏览器
        TitleNum=soupCurrTr("td", {'class' : "fs-topic-name"})
        TitleArray=string.split(str(TitleNum[0]),'\n')
        Title_ReplyNum=string.split(TitleArray[len(TitleArray)-4],'>')[2]
        Title_ViewNum=string.split(TitleArray[len(TitleArray)-2],'>')[2][:-6]
 
        #获取贴子作者
        TitleAuthorObj=soupCurrTr("td", {'style' : "padding-left:4px"})
        Title_Author=TitleAuthorObj[0].next.next.next.string.strip().encode('utf-8')
 
 
        #获取回复时间
        TitleTime=soupCurrTr("td", {'class' : re.compile("^fs-topic-last-mdfy fs-meta")})
 
        """
        print "X:"+str(self.X)
        print "Title_starred:"+Title_starred
        print "Title_sticky:"+Title_sticky
        print "Title:"+Title
 
        #获取贴子内容连接URL
        print "Title_link:"+soupCurrTr.a['href']
        print "CID:"+par_dict["tid"][0]
        print "Title_ReplyNum:"+Title_ReplyNum
        print "Title_ViewNum:"+Title_ViewNum
        print "Title_Author:"+Title_Author
        print "TitleTime:"+TitleTime[0].string.strip().encode('utf-8')
        """
 
        #入库
        self.cursor.execute("insert into Title"+str(self.mod)+" values('%s','%d','%s','%d','%d','%s','%s','%s','%s')" %(par_dict["tid"][0], \
                                     self.X,Title,int(Title_ReplyNum),int(Title_ViewNum),Title_starred,Title_sticky, \
                                     Title_Author.decode('utf-8'),TitleTime[0].string.strip().encode('utf-8')))
        self.conn.commit()
        self._SpiderContent(par_dict["tid"][0])
      except Exception,e:
        if self.log_switch=="on":
          logapp=Pubclilog()
          logger,hdlr = logapp.iniLog()
          logger.info("[Title]"+str(self.X)+'-'+par_dict["tid"][0]+'-'+str(e))
          hdlr.flush()
          logger.removeHandler(hdlr)
 
 
  #======================获取发表及回复方法=======================
  def _SpiderContent(self,ID,nextpage=None):
    if nextpage==None:
      FIXED_QUERY = 'cmm='+str(self.X)+'&tid='+ID+'&ref=regulartopics'
    else:
      FIXED_QUERY = nextpage[9:]
 
    rd = mechanize.Browser()
    rd.addheaders = [("User-agent", "Tianya/2010 (compatible; MSIE 6.0;Windows NT 5.1)")]
    rd.open(self.Content_URL + FIXED_QUERY)
    self.Contentbody=rd.response().read()
 
    #rd=mechanize.Request(self.Content_URL + FIXED_QUERY)
    #response = mechanize.urlopen(rd)
    #self.Contentbody=response.read()
 
    self.Contentsoup = BeautifulSoup(self.Contentbody)
    NextPageObj= self.Contentsoup("a", {'class' : re.compile("fs-paging-item fs-paging-next")})
    try:
      Tdiv=self.Contentsoup("div", {'class' : "fs-user-action"})
      i=0
      for Currdiv in Tdiv:
        if i==0:
          Ctype='Y'
        else:
          Ctype='N'
        #发表时间
        soupCurrdiv=BeautifulSoup(str(Currdiv))
        PosttimeObj=soupCurrdiv("span", {'class' : "fs-meta"})
        Posttime=PosttimeObj[0].next[1:]
        Posttime=Posttime[0:-3]
        #IP地址
        IPObj=soupCurrdiv("a", {'href' : re.compile("CommMsgAddress")})
        if IPObj:
          IP=IPObj[0].next.strip()
        else:
          IP=''
 
 
        #发表／回复内容
        ContentObj=soupCurrdiv("div", {'class' :"fs-user-action-body"})
        Content=ContentObj[0].renderContents().strip()
        """
        print "ID:"+str(self.X)
        print "ID:"+ID
        print "Ctype:"+Ctype
        print "POSTTIME:"+Posttime
        print "IP:"+IP
        print "Content:"+Content
        """
 
        self.cursor.execute("insert into Content"+str(self.mod)+" values('%s','%d','%s','%s','%s','%s')" %(ID,self.X,Ctype,Posttime,IP,Content.decode('utf-8')))
        self.conn.commit() 
        i+=1
 
    except Exception,e:
      if self.log_switch=="on":
        logapp=Pubclilog()
        logger,hdlr = logapp.iniLog()
        logger.info("[Content]"+str(self.X)+'-'+ID+'-'+str(e))
        hdlr.flush()
        logger.removeHandler(hdlr)
 
    #如“下一页”有链接刚继续遍历
    if NextPageObj:
      NextPageURL=NextPageObj[0]['href']
      self._SpiderContent(ID,NextPageURL)
 
 
  def __del__(self):
    try:
      self.cursor.close()
      self.conn.close()
    except Exception,e:
      pass
 
#遍历comm范围
def initapp(StartValue,EndValue,log_switch):
  for x in range(StartValue,EndValue): 
    app=BaseTySpider(x,log_switch)
    app._SpiderClass()
    app=None
 
if __name__ == "__main__":
   
  #定义命令行参数
  MSG_USAGE = "TySpider.py [ -s StartNumber EndNumber ] -l [on|off] [-v][-h]"
  parser = OptionParser(MSG_USAGE)
  parser.add_option("-s", "--set", nargs=2,action="store", 
      dest="comm_value",
      type="int",
      default=False, 
      help="配置名称ID值范围。".decode('utf-8'))
  parser.add_option("-l", "--log", action="store", 
      dest="log_switch",
      type="string",
      default="on", 
      help="错误日志开关".decode('utf-8'))
  parser.add_option("-v","--version", action="store_true", dest="verbose",
      help="显示版本信息".decode('utf-8'))
  opts, args = parser.parse_args()
 
  if opts.comm_value:
    if opts.comm_value[0]>opts.comm_value[1]:
      print "终止值比起始值还小？"
      exit();
    if opts.log_switch=="on":
      log_switch="on"
    else:
      log_switch="off"
    initapp(opts.comm_value[0],opts.comm_value[1],log_switch)
    exit();
 
  if opts.verbose:
    print "WebSite Scider V1.0 beta."
    exit;
