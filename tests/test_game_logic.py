from logic_utils import check_guess, get_range_for_difficulty

# Bug fix tests
# FIX: Wrote the following 4 tests with agent to test range and hints
def test_normal_difficulty_range():
    # Bug: Normal was 1-100 (should be 1-50)
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_hard_difficulty_range():
    # Bug: Hard was 1-50 (should be 1-100)
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_too_high_gives_go_lower_hint():
    # Bug: guess > secret was returning "Go HIGHER!" instead of "Go LOWER!"
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_gives_go_higher_hint():
    # Bug: guess < secret was returning "Go LOWER!" instead of "Go HIGHER!"
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"
