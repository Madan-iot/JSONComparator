import requests
import re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def comparator(url1_data, url2_data):
    def compare(url1_resp_data, url2_resp_data):
        # typelist
        if (type(url1_resp_data) is list):
            # is [url2_resp_data] a list and of same length as [url1_resp_data]?
            if (
                    (type(url2_resp_data) != list) or
                    (len(url1_resp_data) != len(url2_resp_data))
            ):
                return False

            # iterate over list items
            for list_index, list_item in enumerate(url1_resp_data):
                # compare [url1_resp_data] list item against [url2_resp_data] at index
                if (not compare(list_item, url2_resp_data[list_index])):
                    return False

            # list identical
            return True

        # typedictionary
        if (type(url1_resp_data) is dict):
            # is [url2_resp_data] a dictionary?
            if (type(url2_resp_data) != dict):
                return False

            # iterate over dictionary keys
            for dict_key, dict_value in url1_resp_data.items():
                # key exists in [url2_resp_data] dictionary, and same value?
                if (
                        (dict_key not in url2_resp_data) or
                        (not compare(dict_value, url2_resp_data[dict_key]))
                ):
                    return False

            # dictionary identical
            return True

        # simple value - compare both value and type for equality
        return (
                (url1_resp_data == url2_resp_data) and
                (type(url1_resp_data) is type(url2_resp_data))
        )

        # compare a to b, then b to a

    return (
            compare(url1_data, url2_data) and
            compare(url2_data, url1_data)
    )


class Compare(object):
    def json_comparator(self, File1, File2):
        try:
            with open(File1) as Fp1 , open(File2) as Fp2:
                for url1, url2 in zip(Fp1,Fp2):
                    #validating the URL
                    status1 = re.match(regex, url1) is not None
                    assert status1 is True, "Invalid URL format"
                    status2 = re.match(regex, url2) is not None
                    assert status2 is True, "Invalid URL format"

                    #Get the response of the URL
                    file1_url = requests.get(url=url1, headers={'content-type':'application/json'})
                    file1_url_resp = file1_url.json()

                    file2_url = requests.get(url=url2, headers={'content-type': 'application/json'})
                    file2_url_resp = file2_url.json()

                    #call the comparator funtion which compares the responses
                    test = comparator(file1_url_resp, file2_url_resp)

                    if test is True:
                        print(url1 + "equals " + url2)
                    else:
                        print(url1 + "not equals " + url2)
                    #print(test)

        except (IOError, FileNotFoundError) as fileError:
            print("Error occured while accessing the file, {}". format(str(fileError)))
