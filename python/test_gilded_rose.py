# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    '''
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_legendary(self):
        items = [Item("Sulfurus, Hand of Ragnaros", 30, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)
        self.assertEquals(30, items[0].sell_in)

    def test_conjured(self):
        items = [Item("Luminous Cloth", 30, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(23, items[0].quality)
        self.assertEquals(29, items[0].sell_in)

    def test_quality_increase(self):
        items = [Item("Aged Brie", 30, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(26, items[0].quality)
        self.assertEquals(29, items[0].sell_in)
    '''
    def test_backstage_quality_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(31, items[0].quality)
        self.assertEquals(14, items[0].sell_in)

    def test_backstage_quality_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(32, items[0].quality)
        self.assertEquals(9, items[0].sell_in)

    def test_backstage_quality_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(33, items[0].quality)
        self.assertEquals(4, items[0].sell_in)

    def test_backstage_quality_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
        self.assertEquals(-2, items[0].sell_in)

    def test_quality_max(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 50), Item("Aged Brie", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for item in items:
            self.assertEquals(50, item.quality)
            self.assertEquals(19, item.sell_in)

    def test_other_items(self):
        items = [Item("Plated Vest", 30, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(29, items[0].quality)
        self.assertEquals(29, items[0].sell_in)

    def test_other_items_double_quality(self):
        items = [Item("Plated Vest", -1, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(28, items[0].quality)
        self.assertEquals(-2, items[0].sell_in)

    def test_conjured_double_quality(self):
        items = [Item("Twisted Frog Legs", -1, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(26, items[0].quality)
        self.assertEquals(-2, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
