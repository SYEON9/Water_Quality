'''html file 생성하기'''

html_text = """
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    <h1>#3_MongoDB와 연결하기</h1>
    <div>
        <p>연결이 성공되면 아래에 데이터가 뜰거야!</p>
        <p>---------------------------------------<p>
        {% for i in data %}
            <p>지역: {{i.name}}</p>
            <p>정수장: {{i.purification_plant[0]}}</p>
            <p>다목적댐: {{i.multiPurpose_dam[0]}}</p>
            <p>---------------</p>
        {% endfor %}
    </div>
</body>
</html>
"""


html_file = open('templates/html_file2.html','w')
html_file.write(html_text2)
html_file.close()
