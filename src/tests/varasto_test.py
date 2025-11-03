import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasdo = Varasto(-1, -1)
        self.varasto3 = Varasto(-1, 10000)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_tilavuus_korjattu(self):
        self.assertAlmostEqual(self.varasdo.tilavuus, 0)

    def test_uudella_varastolla_saldo_korjattu(self):
        self.assertAlmostEqual(self.varasdo.saldo, 0)

    def test_uudella_varastolla_saldo_korjattud(self):
        self.assertAlmostEqual(self.varasto3.saldo, -1)


    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

    def test_lisays_lisaa_saldoa_liikaa(self):
        self.varasto.lisaa_varastoon(9000)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)



    def test_lisays_lisaa_eisaldoa(self):
        old = self.varasto.saldo 
        self.varasto.lisaa_varastoon(-1)
        new = self.varasto.saldo 

        self.assertAlmostEqual(old-new, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_ottaminen_nolla(self):
        self.varasto.saldo = 0
        r = self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(r, 0)


    def test_ottaminen_allenolla(self):
        self.varasto.saldo = 10
        r = self.varasto.ota_varastosta(-1)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(r, 0)


    def tulosta(self):
        self.varasto.saldo = 0
        self.varasto.tilavuus = 0
        r = self.varasto.paljonko_mahtuu()
        f = self.varasto.__str__()
        self.assertEqual(f, f"saldo = {self.varasto.saldo}, vielä tilaa {r}")
