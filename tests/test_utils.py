from csuibot.utils import zodiac


class TestZodiac:

    def test_aries_lower_bound(self):
        res = zodiac.lookup_zodiac(3, 21)
        assert res == 'aries'

    def test_aries_upper_bound(self):
        res = zodiac.lookup_zodiac(4, 19)
        assert res == 'aries'

    def test_aries_in_between(self):
        res = zodiac.lookup_zodiac(4, 1)
        assert res == 'aries'

    def test_not_aries(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'aries'

    # Implement the mandatory task in here

    def test_unknown_zodiac(self, mocker):
        class FakeZodiac():
            def date_includes(self, *args, **kwargs):
                return False

        mocker.patch('csuibot.utils.zodiac.Scorpio', return_value=FakeZodiac())

        res = zodiac.lookup_zodiac(11, 17)

        assert res == 'Unknown zodiac'


class TestChineseZodiac:

    def run_test(self, expected_zodiac, years):
        res = [zodiac.lookup_chinese_zodiac(y) == expected_zodiac for y in years]

        assert all(res)

    def test_rat(self):
        years = [1996, 1984, 1972, 1960, 2008, 2020]
        self.run_test('rat', years)

    # Implement the mandatory task in here

    def test_unknown_zodiac(self):
        years = [2005, 1993, 1981, 1969, 2017, 2029]
        self.run_test('Unknown chinese zodiac', years)
