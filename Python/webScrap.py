# ================================Web Scraping===========================================
class webInfo:
        def webscrap(self):
                try:
                    while True:
                        import requests
                        from bs4 import BeautifulSoup
                        print()
                        print()
                        url=input("enter your url with http/https:>")
                        print("""
                        1 ->website all anchors tag.
                        2 ->whole website html format.
                        3 ->Get all paragraph and title of website.
                        """)
                        info=int(input("[+]Enter what you want to geather:> "))
                        r = requests.get(url)
                        htmlContent = r.content
                        soup = BeautifulSoup(htmlContent, 'html.parser')
                        anchors = soup.find_all('a')
                        all_links = set()
                        if info==1:
                            print("Please wait a sec..............")
                            # Get all the links on the page:
                            for link in anchors:
                                if (link.get('href') != '#'):
                                    linkText = url + link.get('href')
                                    all_links.add(link)
                                    print(linkText)

                            navbarSupportedContent = soup.find(id='navbarSupportedContent')
                        elif info == 2:
                            print(soup)
                        elif info == 3:
                            # get title of website
                            title = soup.title
                            # Get all the paragraphs from the page
                            para = soup.find_all('p')
                            print(para)
                            print(title)

                except TypeError:
                    print("got some error")
                except ValueError:
                    print("please type complete url....")

obj=webInfo()
obj.webscrap()