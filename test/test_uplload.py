from pages.file_upload import upload

def test_upload(driver):
    ob = upload(driver)
    ob.Upload()