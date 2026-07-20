from wordcount import count_stats


def test_counts_simple_text():
    stats = count_stats("hello world\nsecond line")
    assert stats["lines"] == 2
    assert stats["words"] == 4
    assert stats["chars"] == 23
