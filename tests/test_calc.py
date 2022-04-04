import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(calc.eval_str("0!"), 1)
        self.assertEqual(calc.eval_str("(-0)!"), 1)
        self.assertEqual(calc.eval_str("3!"), 6)
        self.assertEqual(calc.eval_str("5!"), 120)
        self.assertEqual(calc.eval_str("13!"), 6227020800)
        self.assertEqual(calc.eval_str("7.0!"), 5040)

        self.assertRaises(ValueError, calc.eval_str, "(-1)!")
        self.assertRaises(ValueError, calc.eval_str, "3.19!")
        self.assertRaises(ValueError, calc.eval_str, "(-3.0)!")
        self.assertRaises(ValueError, calc.eval_str, "-8.5!")
        self.assertRaises(ValueError, calc.eval_str, "0.35!")
        self.assertRaises(ValueError, calc.eval_str, "-0.35!")

    def test_exponent(self):
        self.assertEqual(calc.eval_str("0^0"), 1)
        self.assertEqual(calc.eval_str("0^-0"), 1)
        self.assertEqual(calc.eval_str("7^0"), 1)
        self.assertEqual(calc.eval_str("7^-0"), 1)
        self.assertEqual(calc.eval_str("(-7)^0"), 1)
        self.assertEqual(calc.eval_str("0^7"), 0)
        self.assertEqual(calc.eval_str("4^2"), 16)
        self.assertEqual(calc.eval_str("3^6"), 729)
        self.assertEqual(calc.eval_str("(-3)^8"), 6561)
        self.assertEqual(calc.eval_str("2^5"), 32)
        self.assertAlmostEqual(calc.eval_str("-2^-5"), -0.03125)
        self.assertAlmostEqual(calc.eval_str("2^-5"), 0.03125)
        self.assertEqual(calc.eval_str("1^258219307541029834"), 1)
        self.assertEqual(calc.eval_str("189080341243102090^0"), 1)

        self.assertAlmostEqual(calc.eval_str("1.7^5"), 14.19857)
        self.assertAlmostEqual(calc.eval_str("-1.7^5"), -14.19857)
        self.assertAlmostEqual(calc.eval_str("1.7^-5"), 0.070429628)
        self.assertAlmostEqual(calc.eval_str("0.05^3"), 0.000125)
        self.assertAlmostEqual(calc.eval_str("12.34^3"), 1879.080904)
        self.assertAlmostEqual(calc.eval_str("(-1.7)^2"), -2.89)
        self.assertAlmostEqual(calc.eval_str("-3.14159265^4"), 97.40909059)
        self.assertAlmostEqual(calc.eval_str("2,71828182846^6"), 403.4287935)

        self.assertRaises(ValueError, calc.eval_str, "0^-5")
        self.assertRaises(ValueError, calc.eval_str, "0^-1.723")

    def test_root(self):
        self.assertEqual(calc.str_eval(), )

    def test_abs(self):
        self.assertEqual(calc.str_eval("|0|"), 0)
        self.assertEqual(calc.str_eval("|-0|"), 0)
        self.assertEqual(calc.str_eval("|9|"), 9)
        self.assertEqual(calc.str_eval("|-9|"), 9)
        self.assertEqual(calc.str_eval("|0.123|"), 0.123)
        self.assertEqual(calc.str_eval("|-0.123|"), 0.123)
        self.assertEqual(calc.str_eval("|-1243|"), 1243)
        self.assertEqual(calc.str_eval("|17.0|"), 17)
        self.assertEqual(calc.str_eval("|-17.0|"), 17)

    def test_brackets(self):
        self.assertEqual(calc.str_eval("(2+7)*13"), 117)
        self.assertEqual(calc.str_eval("2+(7*13)"), 93)
        self.assertEqual(calc.str_eval("(2+7)/18"), 0.5)
        self.assertEqual(calc.str_eval("2+(27/18)"), 3.5)
        self.assertEqual(calc.str_eval("(2+7*13)"), 93)
        self.assertEqual(calc.str_eval("2+27/18"), 3.5)
        self.assertEqual(calc.str_eval("(15-5)/5)"), 2)
        self.assertEqual(calc.str_eval("15-(5/5)"), 14)
        self.assertEqual(calc.str_eval("15-5/5"), 14)
        self.assertEqual(calc.str_eval("21-(4+6*5)"), -13)
        self.assertEqual(calc.str_eval("21-((4+6)*5)"), -29)
        self.assertEqual(calc.str_eval("(21-4+6)*5"), 115)
        self.assertEqual(calc.str_eval("35-(4+6-9)"), 34)
        self.assertEqual(calc.str_eval("35-(4+6)-9"), 16)

        self.assertEqual(calc.str_eval("-(2)^4"), -16)
        self.assertEqual(calc.str_eval("(-2)^4"), 16)
        self.assertEqual(calc.str_eval("-(2^3)!"), -40320)
        self.assertEqual(calc.str_eval("-(2^4!)"), -16777216)
        self.assertEqual(calc.str_eval("-(|-(2^3)|!)"), -40320)
        self.assertEqual(calc.str_eval("(|-2^3)|)!"), 40320)
        self.assertEqual(calc.str_eval("|-(2^3)|!"), 40320)
        self.assertEqual(calc.str_eval("|-(2^3)|!)"), 40320)
        #TODO ODMOCNINY

        self.assertEqual(calc.str_eval("9-(2-6)^(9/3)+1*(1-5)"), 69)
        self.assertEqual(calc.str_eval("((9-2)-6)^9/(3+1*1-5)"), -1)

        self.assertRaises(ValueError, calc.eval_str, "(-(2^4))!")
        self.assertRaises(ValueError, calc.eval_str, "25/(5-5)")

if __name__ == '__main__':
    unittest.main()
