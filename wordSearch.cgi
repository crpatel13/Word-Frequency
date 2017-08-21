#!/bin/bash
# Written by Chirag Patel, Student Id : 104699582, User Id : patel1ha, January 30, 2017
# CGI file for finding total no. of occurrences for specific word

# Add required library functions
source ./lab3lib.cgi

# taking entire input from textarea to one string named "part" in proper format
part=$(echo $texts | tr -s [:space:] '\n')

# initialize counter as 0
count=0

# for loop starts for searching particular keyword
for i in $part
do
        if [[ "$i" == "$keyword" ]];        # main logic to compare keyword from textbox
        then
                let count=count+1
        fi
done

# store final count answer to "answer" field
answer=$count


# starting of HTML code for webpage design
cat <<EOF
<html>
<head>
<!-- Defining CSS for good look -->
<style>
.display {
	background-color : #e9f7ff;
}
div.box {					<!--CSS can be apply using class name -->
	width : 450px;
	height : 300px;
        background-color : #145880;
        color : white;
	position : absolute;
        top : 50%;
	left : 50%;
	margin-top : -150px;
	margin-left : -225px;
    
}
input.keyword {
	position : relative;
	color : #145880;
	background-color : #d0dee6;
	width : 450px; 
}
textarea.texts {
	position : relative;
	color : #145880;
	background-color : #d0dee6;
	width : 450px;
}
input.answer {
	position : relative;
	color : #145880;
	background-color : #d0dee6;
	width : 450px;
}
input.search {
	color : #145880;
	position : relative;
	background-color : #d0dee6;
	width : 100px;
	margin-left : 175px;
}
h1 {
	color : #084a6f;
	text-align : center;
}
</style>
</head>
<!-- main page starts from body tag -->
<body class="display">
        <h1>Find total no. of Occurrences for specific word</h1> <br/><br/>
	<div class="box">
        <form action="?version=${version:=1}" method="POST" enctype="application/x-www-form-urlencoded">		<!-- start form tag using post method -->

			Enter Keyword to search <br/>
			<input type="text" name="keyword" value="$keyword" placeholder="keyword" class="keyword"/> <br/> <br/>
			<textarea rows="5" cols="50" name="texts" value="$texts" class="texts" placeholder="enter your text here"></textarea> <br/> <br/>
			Total No. of occurrences: <br/>
                        <input type="text" name="answer" value="$answer" class="answer"/> <br/> <br/>
			<input type="submit" name="search" value="search" class="search">		
        </form>
	</div>
</body>
</html>
EOF

# ending of HTML code as well as CGI file
