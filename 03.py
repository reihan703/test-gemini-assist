def risky():
    try:
        x = 1 / 0
    except Exception:
        pass  # Silent failure: worst practice

    print("Still running even though something went wrong!")

risky()