class HeavyInit:
    def __init__(self):
        # Doing everything in constructor
        import time
        time.sleep(2)
        print("Heavy logic in __init__ executed!")

HeavyInit()