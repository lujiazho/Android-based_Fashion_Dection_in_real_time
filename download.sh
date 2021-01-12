FILE_NAME='./data'
FILE_ID='1tWdEzXjUa2i23Nl5is9QhXFmff3n2AM8'

curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=$FILE_ID" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=$FILE_ID" -o $FILE_NAME
