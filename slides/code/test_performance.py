def test_performance():   
    start = time.perf_counter()
    result = run_simulation(...)
    elapsed = time.perf_counter() - start

    assert elapsed < 0.1