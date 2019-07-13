
import requests
import json
import re



post_url = "http://www.mtzendo.com/wp-json/wp/v2/posts?per_page=100"

# print("hello world!")

r = requests.get(url=post_url)

# extracting data in json format
blog_data = r.json()

# print(data)
# print(json.dumps(data, indent=4, sort_keys=True))

index = 0
for aPost in blog_data:
    # print(aPost['date'])
    dateString = aPost['date']

    dateString = re.split("T", dateString)[0]
    print(dateString)

    filename = dateString+'-mtzendo-wordpres-'+str(index)+'.md'
    # print(aPost['title']['rendered'])
    title = aPost['title']['rendered']
    # print(aPost['content']['rendered'])
    content = aPost['content']['rendered']

    f = open(filename, "a")
    f.write("---\n")
    f.write("layout: post\n")
    f.write("title: "+title+"\n")
    f.write("date: "+dateString+"\n")
    f.write("---\n")
    f.write("\n")
    f.write(content+"\n")
    f.close()


    index += 1

    # if index == 2:
    #     break
