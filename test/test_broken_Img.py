from test import actions

def test_img(driver, wait):
    results = actions.broken_img(driver, wait)
    for url, status in results:
        assert status != 404, f"Broken image found: {url}"
    print("All images loaded correctly.")
