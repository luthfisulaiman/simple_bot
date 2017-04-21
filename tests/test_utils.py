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

    def test_taurus_lower_bound(self):
        res = zodiac.lookup_zodiac(4, 20)
        assert res == 'taurus'

    def test_taurus_upper_bound(self):
        res = zodiac.lookup_zodiac(5, 20)
        assert res == 'taurus'

    def test_taurus_in_between(self):
        res = zodiac.lookup_zodiac(4, 30)
        assert res == 'taurus'

    def test_not_taurus(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'taurus'

    def test_gemini_lower_bound(self):
        res = zodiac.lookup_zodiac(5, 21)
        assert res == 'gemini'

    def test_gemini_upper_bound(self):
        res = zodiac.lookup_zodiac(6, 20)
        assert res == 'gemini'

    def test_gemini_in_between(self):
        res = zodiac.lookup_zodiac(6, 6)
        assert res == 'gemini'

    def test_not_gemini(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'gemini'

    def test_cancer_lower_bound(self):
        res = zodiac.lookup_zodiac(6, 21)
        assert res == 'cancer'

    def test_cancer_upper_bound(self):
        res = zodiac.lookup_zodiac(7, 22)
        assert res == 'cancer'

    def test_cancer_in_between(self):
        res = zodiac.lookup_zodiac(7, 7)
        assert res == 'cancer'

    def test_not_cancer(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'cancer'

    def test_leo_lower_bound(self):
        res = zodiac.lookup_zodiac(7, 23)
        assert res == 'leo'

    def test_leo_upper_bound(self):
        res = zodiac.lookup_zodiac(8, 22)
        assert res == 'leo'

    def test_leo_in_between(self):
        res = zodiac.lookup_zodiac(8, 8)
        assert res == 'leo'

    def test_not_leo(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'leo'

    def test_virgo_lower_bound(self):
        res = zodiac.lookup_zodiac(8, 23)
        assert res == 'virgo'

    def test_virgo_upper_bound(self):
        res = zodiac.lookup_zodiac(9, 22)
        assert res == 'virgo'

    def test_virgo_in_between(self):
        res = zodiac.lookup_zodiac(9, 9)
        assert res == 'virgo'

    def test_not_virgo(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'virgo'

    def test_libra_lower_bound(self):
        res = zodiac.lookup_zodiac(9, 23)
        assert res == 'libra'

    def test_libra_upper_bound(self):
        res = zodiac.lookup_zodiac(10, 22)
        assert res == 'libra'

    def test_libra_in_between(self):
        res = zodiac.lookup_zodiac(10, 10)
        assert res == 'libra'

    def test_not_libra(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'libra'

     def test_scorpio_lower_bound(self):
        res = zodiac.lookup_zodiac(10, 23)
        assert res == 'scorpio'

    def test_scorpio_upper_bound(self):
        res = zodiac.lookup_zodiac(11, 21)
        assert res == 'scorpio'

    def test_scorpio_in_between(self):
        res = zodiac.lookup_zodiac(11, 11)
        assert res == 'scorpio'

    def test_not_scorpio(self):
        res = zodiac.lookup_zodiac(11, 27)
        assert res != 'scorpio'

    def test_sagittarius_lower_bound(self):
        res = zodiac.lookup_zodiac(11, 22)
        assert res == 'sagittarius'

    def test_sagittarius_upper_bound(self):
        res = zodiac.lookup_zodiac(12, 21)
        assert res == 'sagittarius'

    def test_sagittarius_in_between(self):
        res = zodiac.lookup_zodiac(12, 12)
        assert res == 'sagittarius'

    def test_not_sagittarius(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'sagittarius'

     def test_capricorn_lower_bound(self):
        res = zodiac.lookup_zodiac(12, 22)
        assert res == 'capricorn'

    def test_capricorn_upper_bound(self):
        res = zodiac.lookup_zodiac(1, 19)
        assert res == 'capricorn'

    def test_capricorn_in_between(self):
        res = zodiac.lookup_zodiac(1, 1)
        assert res == 'capricorn'

    def test_not_capricorn(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'capricorn'

    def test_aquarius_lower_bound(self):
        res = zodiac.lookup_zodiac(1, 20)
        assert res == 'aquarius'

    def test_aquarius_upper_bound(self):
        res = zodiac.lookup_zodiac(2, 18)
        assert res == 'aquarius'

    def test_aquarius_in_between(self):
        res = zodiac.lookup_zodiac(2, 2)
        assert res == 'aquarius'

    def test_not_aquarius(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'aquarius'

    def test_pisces_lower_bound(self):
        res = zodiac.lookup_zodiac(2, 19)
        assert res == 'pisces'

    def test_pisces_upper_bound(self):
        res = zodiac.lookup_zodiac(3, 20)
        assert res == 'pisces'

    def test_pisces_in_between(self):
        res = zodiac.lookup_zodiac(3, 3)
        assert res == 'pisces'

    def test_not_pisces(self):
        res = zodiac.lookup_zodiac(11, 17)
        assert res != 'pisces'

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
