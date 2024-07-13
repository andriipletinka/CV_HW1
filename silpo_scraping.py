from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

products = pd.DataFrame(columns=['Desc', 'Image'])

page = 1
while len(products) < 300:
    print('Page', page)
    driver.get(f"https://silpo.ua/category/frukty-ovochi-4788?page={page}")
    try:
        for j in range(50):
            element = driver.find_element("xpath", f'/html/body/sf-shop-silpo-root/shop-silpo-root-shell/silpo-shell-main/div/div[3]/silpo-category/silpo-catalog/div/div[2]/product-card-skeleton/silpo-products-list/div/div[{j+1}]/shop-silpo-common-product-card/div/a/div[1]/div/img')
            desc = element.get_attribute('alt')
            img = element.get_attribute('src')
            product = {'Desc': desc, 'Image': img}
            products = products._append(product, ignore_index=True)
            print(desc, len(products))
    except NoSuchElementException:
        print('not found\n')
    page += 1

driver.quit()
products.to_csv('products.csv', index=False)
