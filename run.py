from youdigest.agent import summarize

if __name__ == "__main__":
    test_text = """
    This is a long video transcript.
    It explains how AI agents work, the importance of LangChain, and the value of using open protocols like MCP.
    The video discusses practical use cases and trade-offs.
    """
    summary = summarize(test_text)
    print("Summary:")
    print(summary)
