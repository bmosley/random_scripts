import requests
import concurrent.futures


def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status


# url = "https://en.wikipedia.org/wiki/Ocean"
# print(get_wiki_page_existence(wiki_page_url=url))

# sourcery skip: list-comprehension
wiki_page_urls = [
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/this_page_does_not_exist",
    "https://en.wikipedia.org/wiki/Shark",
]
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = []
#     for url in wiki_page_urls:
#         futures.append(executor.submit(get_wiki_page_existence, wiki_page_url=url))
#     for future in concurrent.futures.as_completed(futures):
#         print(future.result())

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = []
#     for url in wiki_page_urls:
#         futures.append(
#             executor.submit(get_wiki_page_existence, wiki_page_url=url, timeout=0.00001)
#         )
#     for future in concurrent.futures.as_completed(futures):
#         try:
#             print(future.result())
#         except requests.ConnectTimeout:
#             print("ConnectTimeout.")

wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(100)]
import time


# print("Running without threads:")
# without_threads_start = time.time()
# for url in wiki_page_urls:
#     print(get_wiki_page_existence(wiki_page_url=url))
# print("Without threads time:", time.time() - without_threads_start)


print("Running threaded:")
threaded_start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in wiki_page_urls:
        futures.append(executor.submit(get_wiki_page_existence, wiki_page_url=url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
print("Threaded time:", time.time() - threaded_start)
