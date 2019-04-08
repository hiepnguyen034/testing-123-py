from app.my_script import enlarge # <-- NOTE this modification (app.my_script)

def test_enlarge():
    result = enlarge(3)
    assert result == 3*100000