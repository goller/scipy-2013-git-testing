import animals


def test_read_animals():
    '''
    2011-04-22 21:06 Grizzly 36
    2011-04-23 14:12 Elk 25
    2011-04-23 10:24 Elk 26
    2011-04-23 20:08 Wolverine 31
    2011-04-23 18:46 Muskox 20
    '''
    ref_dates = ['2011-04-22', '2011-04-23', '2011-04-23', '2011-04-23', '2011-04-23']
    ref_times = ['21:06', '14:12', '10:24', '20:08', '18:46']
    ref_species = ['Grizzly', 'Elk', 'Elk', 'Wolverine', 'Muskox']
    ref_counts = [36, 25, 26, 31, 20]

    dates, times, species, counts = animals.read_animals('animals.txt')
    assert dates == ref_dates
    assert times == ref_times
    assert species == ref_species
    assert counts == ref_counts

