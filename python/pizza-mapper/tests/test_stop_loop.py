
def test_loop():
    switch = True 
    loop_count = 0
    while switch:
        loop_count+=1
        if loop_count > 5:
            print(f"Loop count stopped at: {loop_count} iterations")
        switch = False
    assert loop_count == 1
