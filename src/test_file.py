from entity import summarize

if __name__ == "__main__":
    test_page_id = "1c5a18c9-996a-801c-b67b-c848bd135675"
    result = summarize(test_page_id)
    print("\n--- Summary Output ---\n")
    print(result)