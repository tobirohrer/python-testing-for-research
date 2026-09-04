def snapshot_test():
    sample_data = get_sample_data()
    results = run_simulation(sample_data)
    assert results["grid_import"].sum() == 1076
    assert results["bat_cycles"].sum() == 107