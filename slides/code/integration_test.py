def test_storage_delivered_what_was_promised_on_market():
    sample_data = get_sample_data()
    trader, market, storage = setup_test_components(sample_data)
    results = Simulation(trader, market, storage).run()
    energy_delivered = results['storage_delivered']
    energy_promised = results['market_promised']
    assert np.allclose(energy_delivered, energy_promised, atol=0.1)
