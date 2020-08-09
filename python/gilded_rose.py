# -*- coding: utf-8 -*-

legendary_items = ["Sulfuras, Hand of Ragnaros"]
quality_increase_items = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]
conjured_items = ["Twisted Frog Legs", "Luminous Cloth", "Conjured Mana Cake"]

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            is_conjured = item.name in conjured_items
            is_legendary = item.name in legendary_items
            is_quality_increase = item.name in quality_increase_items

            # Do nothing for legendary items
            if is_legendary:
                continue

            # For all other item types, handle case where there is still time to sell
            if item.sell_in >= 0 and item.quality < 50 and item.quality >= 0:
                if is_quality_increase:
                    # Special case for Backstage passes
                    if item.name.startswith("Backstage passes"):
                        if item.sell_in <= 10 and item.sell_in > 5:
                            item.quality += 2
                        elif item.sell_in <= 5 and item.sell_in >= 0:
                            item.quality += 3
                        else:
                            item.quality += 1

                    # For other quality increase items, just increase quality by 1
                    else:
                        item.quality += 1
                # Decrease quality by 2 for conjured items
                elif is_conjured:
                    item.quality -= 2
                else:
                    item.quality -= 1

            # Handle case where the sell_in date is < 0, quality values double
            else:
                if item.quality < 50 and item.quality >= 0:
                    if is_quality_increase:
                        if item.name.startswith("Backstage passes"):
                            item.quality = 0
                        else:
                            item.quality += 2
                    elif is_conjured:
                        item.quality -= 4
                    else:
                        item.quality -= 2

            # Always decrease sell_in date by 1
            item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
