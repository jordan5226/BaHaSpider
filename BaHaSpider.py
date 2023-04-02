import requests
from bs4 import BeautifulSoup
import datetime
from CAniDB import CAniDB


# ================================================================
#
# ================================================================
class CAnimateData:
    def __init__(self, sn, animate_name, score, score_people):
        self.sn = sn
        self.animate_name = animate_name
        self.score = score
        self.score_people = score_people


def export_rank_list(file_name, list_score_rank, list_people_rank):
    print("============================================================")
    f = open(file_name, "w", encoding='UTF-8')
    if f:
        f.write("<html>\n\t<head>")
        f.write("\n\t\t<meta name=\"viewport\" content=\"width=device-width, user-scalable=yes, initial-scale=1\">")
        f.write("\n\t\t<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">")
        f.write("\n\t\t<style>\n\t\t\ttable, th, td {border: 1px solid black; border-collapse: collapse;} \
    th, td {padding: 3px;}\n\t\t\t.table_row_odd {background: #F3F4F6;}\n\t\t</style>")
        f.write("\n\t\t<title>動畫評分列表 - 巴哈姆特動畫瘋</title>")
        f.write("\n\t\t<script type=\"text/javascript\">")
        f.write("\n\t\tfunction reload() {")
        f.write("\n\t\t\thref = window.location.href.split(\"?time=\");")
        f.write("\n\t\t\ttime = (new Date()).getTime();")
        f.write("\n\t\t\tif( href[1] == null || ( time - href[1] > 1800000 ) )")
        f.write("\n\t\t\t\twindow.location.href = href[0] + \"?time=\" + time;")
        f.write("\n\t\t}")
        f.write("\n\t\tfunction showPeopleRankList() {")
        f.write("\n\t\t\tdocument.getElementById(\"table_score\").style.display = 'none';")
        f.write("\n\t\t\tdocument.getElementById(\"table_people\").style.display = '';")
        f.write("\n\t\t}")
        f.write("\n\t\tfunction showScoreRankList() {")
        f.write("\n\t\t\tdocument.getElementById(\"table_people\").style.display = 'none';")
        f.write("\n\t\t\tdocument.getElementById(\"table_score\").style.display = '';")
        f.write("\n\t\t}")
        f.write("\n\t\t</script>")
        f.write("\n\t</head>\n\t<body onload=\"reload();\">\n\t\t")
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # Write Score-Rank Data
        f.write("\n\t\t<table id=\"table_score\" style=\"margin:0 auto;\">")
        f.write("\n\t\t\t<tr>")
        f.write("\n\t\t\t\t<th>排名</th>")
        f.write("<th style=\"width:500px;\">動畫名稱</th>")
        f.write("<th style=\"background: #C3C3C3;\" onclick=\"showScoreRankList()\">評分 &nabla;</th>")
        f.write("<th onclick=\"showPeopleRankList()\">評分人數</th>")
        f.write("\n\t\t\t</tr>")
        odd = True
        for idxData, data in enumerate(list_score_rank):
            if odd:
                f.write("\n\t\t\t<tr class=\"table_row_odd\">")
            else:
                f.write("\n\t\t\t<tr>")
            f.write("\n\t\t\t\t<td>" + str(idxData + 1) + "</td>")
            f.write("<td style=\"text-align:center;\"><a href=\"" + urlBase + str(
                data.sn) + "\" target=\"_blank\">" + data.animate_name + "</a></td>")
            f.write("<td style=\"text-align:center;\">" + str(data.score) + "</td>")
            f.write("<td style=\"text-align:center;\">" + str(data.score_people) + "</td>")
            f.write("\n\t\t\t</tr>")
            odd = not odd
        f.write("\n\t\t</table>")

        # Write People-Rank Data
        f.write("\n\t\t<table id=\"table_people\" style=\"margin:0 auto;display:none;\">")
        f.write("\n\t\t\t<tr>")
        f.write("\n\t\t\t\t<th>排名</th>")
        f.write("<th style=\"width:500px;\">動畫名稱</th>")
        f.write("<th onclick=\"showScoreRankList()\">評分</th>")
        f.write("<th style=\"background: #C3C3C3;\" onclick=\"showPeopleRankList()\">評分人數 &nabla;</th>")
        f.write("\n\t\t\t</tr>")
        odd = True
        for idxData, data in enumerate(list_people_rank):
            if odd:
                f.write("\n\t\t\t<tr class=\"table_row_odd\">")
            else:
                f.write("\n\t\t\t<tr>")
            f.write("\n\t\t\t\t<td>" + str(idxData + 1) + "</td>")
            f.write("<td style=\"text-align:center;\"><a href=\"" + urlBase + str(
                data.sn) + "\" target=\"_blank\">" + data.animate_name + "</a></td>")
            f.write("<td style=\"text-align:center;\">" + str(data.score) + "</td>")
            f.write("<td style=\"text-align:center;\">" + str(data.score_people) + "</td>")
            f.write("\n\t\t\t</tr>")
            odd = not odd
        f.write("\n\t\t</table>")

        f.write(
            "\n\t\t<nobr><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><tbody><tr><td><a href=\"https://www.free-counter.jp/\"><img src=\"https://www.f-counter.net/ani1/48/1644728724/\" alt=\"カウンター\" border=\"0\" style=\"margin:0px; padding:0px; border:0px; vertical-align:bottom\"></a></td>")
        f.write(
            "\n\t\t<td><a href=\"https://www.free-counter.jp/\"><img src=\"https://www.f-counter.net/ani2/48/1644728724/\" alt=\"カウンター\" border=\"0\" style=\"margin:0px; padding:0px; border:0px; vertical-align:bottom\"></a></td>");
        f.write("\n\t\t</tr></tbody></table></nobr>")
        f.write("\n\t</body>\n</html>")
        f.close()


# ================================================================
# Global Declaration
# ================================================================
totalSN = 34000
listSN = []
listScoreRank = []
listPeopleRank = []
urlBase = "https://ani.gamer.com.tw/animeVideo.php?sn="
oAniDB = CAniDB()

# ================================================================
#
# ================================================================
oAniDB.create_table_animate_list()
oAniDB.create_table_episode()

maxSN = oAniDB.get_max_sn()

if maxSN >= totalSN:
    totalSN = maxSN + 300

for i in range(max(1, (maxSN + 1)), totalSN):
    listSN.append(str(i))

# ================================================================
# Crawl existing animate in DB
# ================================================================
listDBSN = oAniDB.query_animate_sn_list()
i = 0
lenSN = len(listDBSN)

while len(listDBSN) != 0:
    row = listDBSN.pop(0)
    sn = row[0]
    url = urlBase + str(sn)

    # Get HTML
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Get Data
    divs = soup.select(".anime_name")
    if len(divs) == 0:
        continue

    for div_name in divs:
        name = div_name.select_one("h1").getText()
        names = name.split(" [")
        name = names[0]
        for index, strName in enumerate(names):
            if index == 0:
                continue
            if not strName[0].isnumeric():
                if strName.find("特別篇]") > -1:
                    continue
                else:
                    name += " [" + strName

    divs = soup.select(".score-overall-number")
    for div_num in divs:
        num = div_num.getText()

    divs = soup.select(".score-overall-people")
    for div_people in divs:
        people = div_people.getText().replace(',', '')
        people = people.replace("人評價", "")

    # Update Data to DB
    rowid = oAniDB.update_animate(name, str(sn), float(num), int(people))

    # Update Animate Episode
    divs = soup.select(".season")
    for div in divs:
        lis = div.select("li")
        for li in lis:
            ep = li.select_one("a").getText()
            strSN = li.select_one("a").get("href")
            strSN = strSN.split("?sn=")
            oAniDB.update_episode(rowid, ep, strSN[1])

    oAniDB.commit()

    # os.system('cls' if os.name=='nt' else 'clear')
    i += 1
    print("Process: %.2f%% ( sn: %d )" % (float(i)/float(lenSN)*100, sn))
    print(name + " / " + str(num) + " / " + str(people) + "人")

# ================================================================
# Crawl new animate on web
# ================================================================
while len(listSN) != 0:
    sn = listSN.pop(0)
    url = urlBase + sn

    # Get HTML
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Get Data
    divs = soup.select(".anime_name")
    if len(divs) == 0:
        continue

    for div_name in divs:
        name = div_name.select_one("h1").getText()
        names = name.split(" [")
        name = names[0]
        for index, strName in enumerate(names):
            if index == 0:
                continue
            if not strName[0].isnumeric():
                if strName.find("特別篇]") > -1:
                    continue
                else:
                    name += " [" + strName

    divs = soup.select(".score-overall-number")
    for div_num in divs:
        num = div_num.getText()

    divs = soup.select(".score-overall-people")
    for div_people in divs:
        people = div_people.getText().replace(',', '')
        people = people.replace("人評價", "")

    # Update Data to DB
    rowid = oAniDB.update_animate(name, sn, float(num), int(people))

    # Remove Duplicated Animate
    divs = soup.select(".season")
    for div in divs:
        lis = div.select("li")
        for li in lis:
            ep = li.select_one("a").getText()
            strSN = li.select_one("a").get("href")
            strSN = strSN.split("?sn=")
            if int(strSN[1]) == 28423:
                print("warn")
            if strSN[1] in listSN:
                listSN.remove(strSN[1])
            oAniDB.update_episode(rowid, ep, strSN[1])

    oAniDB.commit()

    # os.system('cls' if os.name=='nt' else 'clear')
    print("Process: %.2f%% ( %s / %d )" % (float(sn)/float(totalSN)*100, sn, totalSN))
    print(sn + ": " + name + " / " + str(num) + " / " + str(people) + "人")

# Query Score-Rank data from DB
listScore = [5.0, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4.0, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1, 3.0,
              2.9, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0]
while len(listScore) != 0:
    score = listScore.pop(0)
    rows = oAniDB.query_animates_by_score(score)
    for row in rows:
        listScoreRank.append(CAnimateData(row[1], row[0], row[2], row[3]))

# Query People-Rank data from DB
rows = oAniDB.query_animates_by_score_people()
for row in rows:
    listPeopleRank.append(CAnimateData(row[1], row[0], row[2], row[3]))

# Export Result
export_rank_list("C:\\Users\\Jordan\\我的雲端硬碟\\巴哈動畫瘋\\AniRank.html", listScoreRank, listPeopleRank)

oAniDB.close()
