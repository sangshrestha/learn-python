from watch import parse


def test_minimal():
    assert (
        parse("<iframe src='http://www.youtube.com/embed/xvFZjo5PgG0'></iframe>")
        == "https://youtu.be/xvFZjo5PgG0"
    )


def test_long():
    assert (
        parse(
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )


def test_none():
    assert (
        parse(
            '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
        )
        is None
    )
