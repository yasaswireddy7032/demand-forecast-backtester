import unittest
from app import *

class ForecastTests(unittest.TestCase):
    def test_future_is_excluded(self):
        y=series(60);a=backtest(y,40);y[50:]+=1000;b=backtest(y,40)
        # Independently verify the first fold cannot depend on any future point.
        a=backtest(series(41),40);b=backtest(np.append(series(41),[9999]),40)
        self.assertAlmostEqual(a['last_predictions'][0]['prediction'],b['last_predictions'][0]['prediction'])
    def test_constant_baseline(self):self.assertEqual(backtest(np.ones(45),40)['seasonal_naive_mae'],0)
    def test_short_input(self):
        with self.assertRaises(ValueError):feature([1])
    def test_fold_count(self):self.assertEqual(backtest(series(50),40)['folds'],10)

if __name__ == '__main__': unittest.main()
