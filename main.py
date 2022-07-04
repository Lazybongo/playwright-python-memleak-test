#!/usr/bin/python3

import time


def fetch_url(url):
    from playwright.sync_api import sync_playwright
    command_executor = "ws://browserless-chrome:3000"
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(command_executor)

        context = browser.new_context(
            bypass_csp=True,
            accept_downloads=False
        )

        page = context.new_page()
        page.set_default_navigation_timeout(30000)
        page.set_default_timeout(30000)
        now = time.time()
        with page.expect_navigation():
            response = page.goto(url, wait_until='commit')
        body = response.body()
        print("Loaded in {}, body len {}".format(time.time() - now, len(body)))
        page.close()
        context.close()
        browser.close()


# Wait for browserless to come up
print("Waiting 10 sec for startup..")
time.sleep(10)
print("Running...")
i=0
try:
    while True:
        print("Fetching.. {}",i)
        fetch_url("https://gearheadworks.com/product/tailhook-adapter-to-fix-sig-spin-brace/")
        fetch_url("https://www.rainierarms.com/gear-head-works-tailhook-mod-1-sig-sauer-brace-adapter/")
        fetch_url("https://www.robertrtg.com/store/pc/GEAR-HEAD-WORKS-TAILHOOK-MOD-1-SIG-BRACE-SPIN-FIX-351p9726.htm")
        fetch_url("https://redriverrange.com/product/gear-head-works-sig-mp-series-sig-spin-adapter")
        fetch_url("https://shootingsurplus.com/gear-head-works-head-works-sig-spin-brace-adapter/")
        fetch_url("https://www.getyourgunsamerica.com/gear-head-works-sig-spin-brace-adapter.html")
        fetch_url("https://gunzonedeals.com/product/gear-head-works-sig-spin-brace-adapter")
        fetch_url("https://littlecreektrading.com/ghw-th1-adapter-for-sig-spin-brace/")
        fetch_url("https://www.rrarms.com/gear-head-works-sig-spin-brace-adapter.html")
        fetch_url("https://www.htxtactical.com/ghw-th1-adapter-for-sig-spin-brace")
        fetch_url("https://www.b-tactical.com/product/294715/GHWTH1ADAPTERFORSIGSPINBRACE")
        fetch_url("https://www.ak-103.com/ghw-th1-adapter-for-sig-spin-brace")
        fetch_url("https://www.familyfirearms.com/product/gear-head-works-sig-spin-brace-adapter#product_detail")
        fetch_url("https://totalimpactguns.com/ghw-th1-adapter-for-sig-spin-brace/")
        fetch_url("https://www.straptarmory.com/ghw-th1-adapter-for-sig-spin-brace")
        fetch_url("https://gun.deals/search/apachesolr_search/856534007516")

        time.sleep(2)
        i+=1
except Exception as e:
    print(e)
