def test_schedule_does_not_exeed_cycle_limit():
    solver = get_solver()
    optimisation_problem = build_optimisation_problem(battery_cycle_limit=5,
                                                      prices=[...],
                                                      battery_capacity_kwh=10
                                                      )
    schedule = solver.solve(optimisation_problem)
    actual_cycles = calculate_cycles_from_schedule(schedule)
    assert actual_cycles <= 5


@pytest.mark.parametrize("prices, soc_init, expected_actions", 
                         [
                            ([-10, 10], 0.5, [-5, 10]),
                            ([-10, 10], 1, [-10, 10]),   
                         ])
def test_day_ahead_schedule_is_optimal(prices, soc_init, expected_actions):
    solver = get_solver()
    optimisation_problem = build_daa_optimisation_problem(prices=prices, 
                                                          soc_init=soc_init,
                                                          ...)
    schedule = solver.solve(optimisation_problem)
    assert list(schedule) == pytest.approx(expected_actions, abs=1e-6)