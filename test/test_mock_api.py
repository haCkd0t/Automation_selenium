from pages.api import api

mock_data = {"Mock": "Successful"}

def test_api(mocker,mock_driver):
    mock_response = mocker.Mock()
    mock_response.json.return_value = mock_data
    mocker.patch('pages.api.requests.get',return_value=mock_response)
    ob = api(mock_driver)
    r = ob.api_covid()
    assert r == mock_data, "Test Failed"

