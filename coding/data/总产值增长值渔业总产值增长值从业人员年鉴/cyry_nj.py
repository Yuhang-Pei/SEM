#从业人员及构成
import time
from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
import pymysql


def saveData(city, year, kind, num):
    count = pymysql.connect(
        host='127.0.0.1',  # 数据库地址
        port=3306,  # 数据库端口
        user='root',  # 数据库账号
        password='20011109wf',  # 数据库密码
        db='yv'  # 数据库名
    )
    # 创建数据库对象
    cur = count.cursor()
    # 写入sql
    # print("写入数据:"+DataObject.to_string())
    sql = "insert into cyry_nj( city, year, kind, num) values ('%s',%d,'%s',%d)" % (
        city, (year), kind, (num))
    # 执行sql
    print(sql)
    cur.execute(sql)
    # 保存修改内容
    count.commit()
    cur.close()
    count.close()
# 爬取数据的方向


option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
driver = webdriver.Chrome(options=option)
driver.get("http://data.cnfm.com.cn/web/moa/fishTotal/dataSearch_s.aspx")
p_input1 = driver.find_element(By.ID, 'l_zb').click()
time.sleep(1)
p_input2 = driver.find_element(By.XPATH, '//*[@id="376"]').click()
time.sleep(1)
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="ItemsList"]/dd[4]/input').click()
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="ItemsList"]/dd[6]/input').click()
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="ItemsList"]/dd[7]/input').click()
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="ItemsList"]/dd[9]/input').click()
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="ItemsList"]/dd[10]/input').click()
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="ItemsList"]/dd[11]/input').click()

time.sleep(1)
p_input1 = driver.find_element(By.ID, 'l_reg').click()
time.sleep(1)
p_input2 = driver.find_element(By.XPATH, '//*[@id="option3"]/input[1]').click()
time.sleep(1)
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="DistList"]/dd[33]/input').click()

time.sleep(1)
p_input1 = driver.find_element(By.ID, 'l_year').click()
time.sleep(1)
p_input2 = driver.find_element(By.XPATH, '//*[@id="option4"]/input[1]').click()
time.sleep(1)
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="YearsList"]/dd[8]/input').click()
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="YearsList"]/dd[9]/input').click()

time.sleep(1)
p_input2 = driver.find_element(
    By.XPATH, '//*[@id="form1"]/div[7]/div[1]/div/input').click()

time.sleep(2)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(2)
page_text = driver.page_source
# with open('3-.html', 'w', encoding='utf-8')as fp:
#     fp.write(page_text)
# 进行解析
tree = etree.HTML(page_text)
tr = tree.xpath('//*[@id="content"]/tbody/tr')

listData = []
i = 0
for j in tr[0:192]:  # tr2[1:]遍历第1列到最后一列，表头为第0列
    # city='全国'
    td = j.xpath('td')
    if i % 6 == 0:
        yvj = '//*[@id = "content"]/tbody/tr[%d]/th[1]/div' % (i+1)
        city = tree.xpath(yvj)[0].text
        hh = '渔业人口（人）'
    if i % 6 == 1:
        hh = '专业从业人员（人）'
    if i % 6 == 2:
        hh = '渔业从业人员（人）'
    if i % 6 == 3:
        hh = '捕捞（人）'
    if i % 6 == 4:
        hh = '养殖（人）'
    if i % 6 == 5:
        hh = '其它（人）'
    y2013 = int(td[0].text)
    y2014 = int(td[1].text)
    y2015 = int(td[2].text)
    y2016 = int(td[3].text)
    y2017 = int(td[4].text)
    y2018 = int(td[5].text)
    y2019 = int(td[6].text)
    i = i+1
    saveData(city, 2013, hh,  y2013)
    saveData(city, 2014, hh,  y2014)
    saveData(city, 2015, hh,  y2015)
    saveData(city, 2016, hh,  y2016)
    saveData(city, 2017, hh,  y2017)
    saveData(city, 2018, hh,  y2018)
    saveData(city, 2019, hh,  y2019)
   # listData.append([city, hh, 2013, y2013])
    #listData.append([city, hh, 2014, y2014])
    #listData.append([city, hh, 2015, y2015])
    #listData.append([city, hh, 2016, y2016])
    #listData.append([city, hh, 2017, y2017])
    #listData.append([city, hh, 2018, y2018])
   # listData.append([city, hh, 2019, y2019])
# print(listData)
