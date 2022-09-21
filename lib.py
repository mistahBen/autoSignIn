"""Page elements to find/interact"""


class config:
    '''edit as needed'''
    SITE = "https://accounts.google.com"
    domain = "district65.net"


class elements:
    g_email = str(
        "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div/div/div[2]")
    g_confirm = str(
        "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div")
    
    g_confirm_button = str(
        "//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    
    #"//*[@id="confirm"]"
    account_button = str("//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a")
