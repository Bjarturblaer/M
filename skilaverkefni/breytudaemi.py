"""Þú ert að framleiða x mörg egg á ári. Þú ert að finna út hve marga eggjabakka og kassa þú þarft að panta á 3 mánaða fresti. Öll þau egg sem komast ekki í heilan kassa gefur þú til góðgerðarmála. Þú villt finna hversu marga kassa þú villt panta, hversu marga bakka þú villt panta, hve margir eggjarbakkar og stök eggfara fara til góðgerðarmála á þriggja mánaða fresti
Í hverjum eggjarbakka eru 12 egg og í hverjum kassa eru 8 eggjarbakkar.
Þar sem í hverjum mánuði er smá breytileg framleiðsla þá helduru einusinni á ári fjölskyldu partý með afgangs eggjum sem fara ekki í kassa eða til góðgerðarmála
"""
# Dæmi um innslátt 2000000 og útkoman er 
# Kassar á 3 mánaða fresti: 5208
# bakkar á 3 mánaða fresti: 41666
# bakkar til góðgerðarmála: 2
#stök egg til góðgerðarmála: 6
# Egg í fjölskyldupartý: 8

eggs_in_carton = 12
eggs_in_boxes = eggs_in_carton*8

eggs_in_one_year = int(input("Hve mörg egg eru framleidd á ári: "))
monthly_prod = eggs_in_one_year//12
three_month_production = monthly_prod *3
total_boxes = three_month_production//eggs_in_boxes
total_cartons = three_month_production//eggs_in_carton
egg_outside_boxes = three_month_production%eggs_in_boxes
cartons_to_charity = egg_outside_boxes//eggs_in_carton
single_eggs_to_charity = egg_outside_boxes%eggs_in_carton
family_party = eggs_in_one_year-(three_month_production)*4
print("Kassar á 3 mánaða fresti: " + str(total_boxes))
print("Bakkar á 3 mánaða fresti: " + str(total_cartons))
print("Bakkar til góðgerðarmála á 3 mánaða fresti: " + str(cartons_to_charity))
print("Stök egg til góðgerðarmála á 3 mánaða fresti: " + str(single_eggs_to_charity))
print("Egg í fjölskyldupartý: " + str(family_party))
