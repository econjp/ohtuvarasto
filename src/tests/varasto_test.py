import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # edge caset + haarat

    def test_konstruktori_negatiivinen_tilavuus(self):
        v = Varasto(-1)
        self.assertAlmostEqual(v.tilavuus, 0)
        # tämän toteutuksen mukaan saldo menee negatiiviseksi -> mahtuu = 1
        self.assertAlmostEqual(v.paljonko_mahtuu(), 1)
        self.assertAlmostEqual(v.saldo, -1)

    def test_konstruktori_negatiivinen_alkusaldo(self):
        v = Varasto(10, -5)
        self.assertAlmostEqual(v.saldo, 0)
        self.assertAlmostEqual(v.paljonko_mahtuu(), 10)

    def test_konstruktori_alkusaldo_yli_tilavuuden(self):
        v = Varasto(10, 50)
        self.assertAlmostEqual(v.saldo, 10)
        self.assertAlmostEqual(v.paljonko_mahtuu(), 0)

    def test_lisays_negatiivinen_ei_muuta(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yli_kapasiteetin_tayttaa(self):
        self.varasto.lisaa_varastoon(1000)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_otto_negatiivinen_palauttaa_nollan_ei_muuta(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_otto_yli_saldon_tyhjentaa(self):
        self.varasto.lisaa_varastoon(6)
        saatu = self.varasto.ota_varastosta(999)
        self.assertAlmostEqual(saatu, 6)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijono_muoto(self):
        self.varasto.lisaa_varastoon(4)
        s = str(self.varasto)
        self.assertIn("saldo = 4", s)
        self.assertIn("vielä tilaa 6", s)
