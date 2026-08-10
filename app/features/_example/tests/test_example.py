from app.features._example.service import example_message


def test_example_message():
    assert example_message() == {"message": "example"}
