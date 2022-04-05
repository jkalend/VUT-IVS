import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(calc.eval_str("0!"), 1)
        self.assertEqual(calc.eval_str("(-0)!"), 1)
        self.assertEqual(calc.eval_str("3!"), 6)
        self.assertEqual(calc.eval_str("5!"), 120)
        self.assertEqual(calc.eval_str("-5!"), -120)
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
        self.assertEqual(calc.eval_str("4^002"), 16)
        self.assertEqual(calc.eval_str("3^6"), 729)
        self.assertEqual(calc.eval_str("(-3)^8"), 6561)
        self.assertEqual(calc.eval_str("2^5"), 32)
        self.assertAlmostEqual(calc.eval_str("-2^-5"), -0.03125)
        self.assertAlmostEqual(calc.eval_str("2^-5"), 0.03125)
        self.assertEqual(calc.eval_str("1^258219307541029834"), 1)
        self.assertEqual(calc.eval_str("189080341243102090^0"), 1)

        self.assertAlmostEqual(calc.eval_str("1.7^5"), 14.19857)
        self.assertAlmostEqual(calc.eval_str("(-1.7)^5"), -14.19857)
        self.assertAlmostEqual(calc.eval_str("1.7^-5"), 0.070429628)
        self.assertAlmostEqual(calc.eval_str("0.05^3"), 0.000125)
        self.assertAlmostEqual(calc.eval_str("12.34^3"), 1879.080904)
        self.assertAlmostEqual(calc.eval_str("(-1.7)^2"), 2.89)
        self.assertAlmostEqual(calc.eval_str("-1.7^2"), -2.89)
        self.assertAlmostEqual(calc.eval_str("-3.14159265^4"), -97.40909059)
        self.assertAlmostEqual(calc.eval_str("2,71828182846^6"), 403.4287935)

        self.assertRaises(ValueError, calc.eval_str, "0^-5")
        self.assertRaises(ValueError, calc.eval_str, "0^-1.723")

    def test_root(self):
        self.assertEqual(calc.eval_str("√4"), 2)
        self.assertEqual(calc.eval_str("1√4"), 4)
        self.assertEqual(calc.eval_str("2√4"), 2)
        self.assertEqual(calc.eval_str("002√4"), 2)
        self.assertEqual(calc.eval_str("3√8"), 2)
        self.assertEqual(calc.eval_str("7√16384"), 4)
        self.assertEqual(calc.eval_str("6√0"), 0)
        self.assertEqual(calc.eval_str("231√0"), 0)
        self.assertEqual(calc.eval_str("√1"), 1)
        self.assertEqual(calc.eval_str("3424√1"), 1)

        self.assertEqual(calc.eval_str("3√-8"), -2)
        self.assertEqual(calc.eval_str("7√-16384"), -4)
        self.assertEqual(calc.eval_str("3√-343"), -7)

        self.assertAlmostEqual(calc.eval_str("3√4"), 1.587401052)
        self.assertAlmostEqual(calc.eval_str("14√7"), 1.149116725)
        self.assertAlmostEqual(calc.eval_str("123429750√3"), 1)
        self.assertAlmostEqual(calc.eval_str("4√19"), 2.08779763)
        self.assertAlmostEqual(calc.eval_str("√33"), 5.744562647)

        self.assertAlmostEqual(calc.eval_str("3√0.4"), 0.73680629)
        self.assertAlmostEqual(calc.eval_str("6√13.69"), 1.546680374)

        self.assertAlmostEqual(calc.eval_str("0.3√4"), 101.5936673)
        self.assertAlmostEqual(calc.eval_str("12.71√36"), 1.325705594)
        self.assertAlmostEqual(calc.eval_str("3.14159265√3.14159265"), 1.439619496)

        self.assertAlmostEqual(calc.eval_str("(-3)√4"), 0.6299605249)
        self.assertAlmostEqual(calc.eval_str("(-3)√27"), 0.333333333)
        self.assertAlmostEqual(calc.eval_str("(-12)√36"), 0.7418363756)
        self.assertAlmostEqual(calc.eval_str("(-1)√36"), 0.027777777)
        self.assertAlmostEqual(calc.eval_str("(-7.25)√0.456"), 1.114395455)
        self.assertAlmostEqual(calc.eval_str("(-0.01)√100.0"), 0)
        self.assertAlmostEqual(calc.eval_str("(-0.73)√42.947"), 0.00579569749)

        self.assertRaises(ValueError, calc.eval_str, "0√0")
        self.assertRaises(ValueError, calc.eval_str, "0√-5")
        self.assertRaises(ValueError, calc.eval_str, "6√-13")
        self.assertRaises(ValueError, calc.eval_str, "22√-3.14159265")
        self.assertRaises(ValueError, calc.eval_str, "7√-5")
        self.assertRaises(ValueError, calc.eval_str, "3√-0")


    def test_abs(self):
        self.assertEqual(calc.eval_str("|0|"), 0)
        self.assertEqual(calc.eval_str("|-0|"), 0)
        self.assertEqual(calc.eval_str("|9|"), 9)
        self.assertEqual(calc.eval_str("|-9|"), 9)
        self.assertEqual(calc.eval_str("|0.123|"), 0.123)
        self.assertEqual(calc.eval_str("|-0.123|"), 0.123)
        self.assertEqual(calc.eval_str("|-1243|"), 1243)
        self.assertEqual(calc.eval_str("|17.0|"), 17)
        self.assertEqual(calc.eval_str("|-17.0|"), 17)

    def test_brackets(self):
        self.assertEqual(calc.eval_str("(2+7)*13"), 117)
        self.assertEqual(calc.eval_str("2+(7*13)"), 93)
        self.assertEqual(calc.eval_str("(2+7)/18"), 0.5)
        self.assertEqual(calc.eval_str("2+(27/18)"), 3.5)
        self.assertEqual(calc.eval_str("(2+7*13)"), 93)
        self.assertEqual(calc.eval_str("2+27/18"), 3.5)
        self.assertEqual(calc.eval_str("(15-5)/5)"), 2)
        self.assertEqual(calc.eval_str("15-(5/5)"), 14)
        self.assertEqual(calc.eval_str("15-5/5"), 14)
        self.assertEqual(calc.eval_str("21-(4+6*5)"), -13)
        self.assertEqual(calc.eval_str("21-((4+6)*5)"), -29)
        self.assertEqual(calc.eval_str("(21-4+6)*5"), 115)
        self.assertEqual(calc.eval_str("35-(4+6-9)"), 34)
        self.assertEqual(calc.eval_str("35-(4+6)-9"), 16)

        self.assertEqual(calc.eval_str("-(2)^4"), -16)
        self.assertEqual(calc.eval_str("(-2)^4"), 16)
        self.assertEqual(calc.eval_str("-(2^3)!"), -40320)
        self.assertEqual(calc.eval_str("-(2^4!)"), -16777216)
        self.assertEqual(calc.eval_str("-(|-(2^3)|!)"), -40320)
        self.assertEqual(calc.eval_str("(|-2^3)|)!"), 40320)
        self.assertEqual(calc.eval_str("|-(2^3)|!"), 40320)
        self.assertEqual(calc.eval_str("|-(2^3)|!)"), 40320)
        self.assertAlmostEqual(calc.eval_str("(7-3)√64*5/3!"), 2.357022604)
        self.assertAlmostEqual(calc.eval_str("7-(-3√(64*5))/3!"), 6.975633186)
        self.assertAlmostEqual(calc.eval_str("7√((64*√5)/3!)/(5√17)"), 0.8926842879)
        self.assertAlmostEqual(calc.eval_str("7√(13^2.3)*(5/3)√17-6^(3√9)+3"), -25.84075382)
        self.assertEqual(calc.eval_str("9-(2-6)^(9/3)+1*(1-5)"), 69)
        self.assertEqual(calc.eval_str("((9-2)-6)^9/(3+1*1-5)"), -1)


        self.assertRaises(ValueError, calc.eval_str, "(-(2^4))!")
        self.assertRaises(ValueError, calc.eval_str, "25/(5-5)")
        self.assertRaises(ValueError, calc.eval_str, "-2√(17-19)")
        self.assertRaises(ValueError, calc.eval_str, "(124*0-3-(-3))√13")

if __name__ == '__main__':
    unittest.main()
